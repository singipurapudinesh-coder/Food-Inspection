from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from flask_bcrypt import Bcrypt

from werkzeug.utils import secure_filename

import os

from config import Config

from models.database import get_cursor

from models.user import User

from utils.gemini_ai import analyze_food

from utils.pdf_generator import create_pdf


print("MYSQL_HOST =", Config.MYSQL_HOST)
print("MYSQL_USER =", Config.MYSQL_USER)
print("MYSQL_DATABASE =", Config.MYSQL_DATABASE)
print("MYSQL_PASSWORD SET =", bool(Config.MYSQL_PASSWORD))


app = Flask(__name__)

app.config.from_object(Config)

bcrypt = Bcrypt(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@login_manager.user_loader
def load_user(user_id):

    return User.get_by_id(user_id)


@app.route("/")
def home():

    if current_user.is_authenticated:

        return redirect(
            url_for("dashboard")
        )

    return redirect(
        url_for("login")
    )


# ================= LOGIN =================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = User.get_by_email(email)

        if user:

            if bcrypt.check_password_hash(
                user["password"],
                password
            ):

                login_user(

                    User(

                        user["id"],

                        user["name"],

                        user["email"],

                        user["role"]

                    )

                )

                return redirect(
                    url_for("dashboard")
                )

        flash(
            "Invalid email or password"
        )

    return render_template(
        "login.html"
    )


# ================= REGISTER =================

@app.route(
    "/register",
    methods=["GET", "POST"]
)

def register():

    if request.method == "POST":

        name = request.form.get("name")

        email = request.form.get("email")

        password = request.form.get("password")

        if User.get_by_email(email):

            flash(
                "Email already exists"
            )

            return redirect(
                url_for("register")
            )

        hashed = bcrypt.generate_password_hash(

            password

        ).decode(

            "utf-8"

        )

        User.create_user(

            name,

            email,

            hashed

        )

        flash(
            "Registration successful"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "register.html"
    )


# ================= DASHBOARD =================

@app.route("/dashboard")

@login_required

def dashboard():

    connection, cursor = get_cursor()

    cursor.execute(
        "SELECT COUNT(*) AS count FROM users"
    )

    users = cursor.fetchone()["count"]

    cursor.execute(
        "SELECT COUNT(*) AS count FROM inspections"
    )

    inspections = cursor.fetchone()["count"]

    cursor.execute(

        """
        SELECT COUNT(*) AS count

        FROM inspections

        WHERE healthy_status='Healthy'
        """

    )

    healthy = cursor.fetchone()["count"]

    cursor.execute(

        """
        SELECT COUNT(*) AS count

        FROM inspections

        WHERE healthy_status='Unhealthy'
        """

    )

    unhealthy = cursor.fetchone()["count"]

    cursor.close()

    connection.close()

    stats = {

        "users": users,

        "inspections": inspections,

        "healthy": healthy,

        "unhealthy": unhealthy

    }

    return render_template(

        "dashboard.html",

        stats=stats

    )


# ================= INSPECT =================

@app.route(

    "/inspect",

    methods=["GET", "POST"]

)

@login_required

def inspect():

    if request.method == "POST":

        try:

            mode = request.form.get(

                "mode",

                "OFF"

            )

            prompt = request.form.get(

                "prompt"

            )

            image = request.files.get(

                "image"

            )

            if not image:

                flash(

                    "Upload an image"

                )

                return redirect(

                    url_for(

                        "inspect"

                    )

                )

            filename = secure_filename(

                image.filename

            )

            filepath = os.path.join(

                app.config["UPLOAD_FOLDER"],

                filename

            )

            image.save(

                filepath

            )

            result = analyze_food(

                prompt,

                filepath

            )

            session["report"] = result

            connection, cursor = get_cursor()

            cursor.execute(

                """
                INSERT INTO inspections(

                user_id,

                food_name,

                healthy_status,

                health_score,

                calories,

                protein,

                fat,

                carbohydrates,

                freshness,

                temperature_risk,

                recommendation,

                summary,

                image_name

                )

                VALUES(

                %s,%s,%s,%s,%s,

                %s,%s,%s,%s,%s,

                %s,%s,%s

                )
                """,

                (

                    current_user.id,

                    result.get(

                        "food_name",

                        "Unknown"

                    ),

                    result.get(

                        "healthy_status",

                        "Unknown"

                    ),

                    result.get(

                        "health_score",

                        0

                    ),

                    result.get(

                        "calories",

                        0

                    ),

                    result.get(

                        "protein",

                        0

                    ),

                    result.get(

                        "fat",

                        0

                    ),

                    result.get(

                        "carbohydrates",

                        0

                    ),

                    result.get(

                        "freshness",

                        "Unknown"

                    ),

                    result.get(

                        "temperature_risk",

                        "Unknown"

                    ),

                    result.get(

                        "recommendation",

                        ""

                    ),

                    result.get(

                        "summary",

                        ""

                    ),

                    filename

                )

            )

            connection.commit()

            cursor.close()

            connection.close()

            return render_template(

                "inspect.html",

                result=result,

                mode=mode

            )

        except Exception as e:

            flash(

                str(e)

            )

            return redirect(

                url_for(

                    "inspect"

                )

            )

    return render_template(

        "inspect.html",

        mode="OFF"

    )


# ================= PDF =================

@app.route("/download")

@login_required

def download():

    report = session.get(

        "report"

    )

    return create_pdf(

        report

    )


# ================= HISTORY =================

@app.route("/history")

@login_required

def history():

    connection, cursor = get_cursor()

    cursor.execute(

        """
        SELECT

        food_name,

        health_score,

        healthy_status,

        created_at

        FROM inspections

        WHERE user_id=%s

        ORDER BY created_at DESC
        """,

        (

            current_user.id,

        )

    )

    history = cursor.fetchall()

    cursor.close()

    connection.close()

    return render_template(

        "history.html",

        history=history

    )


# ================= ADMIN =================

@app.route("/admin")

@login_required

def admin():

    if current_user.role != "admin":

        flash(

            "Access denied"

        )

        return redirect(

            url_for(

                "dashboard"

            )

        )

    connection, cursor = get_cursor()

    cursor.execute(

        "SELECT COUNT(*) AS count FROM users"

    )

    users = cursor.fetchone()["count"]

    cursor.execute(

        "SELECT COUNT(*) AS count FROM inspections"

    )

    inspections = cursor.fetchone()["count"]

    cursor.execute(

        """
        SELECT COUNT(*) AS count

        FROM inspections

        WHERE healthy_status='Healthy'
        """

    )

    healthy = cursor.fetchone()["count"]

    cursor.execute(

        """
        SELECT COUNT(*) AS count

        FROM inspections

        WHERE healthy_status='Unhealthy'
        """

    )

    unhealthy = cursor.fetchone()["count"]

    cursor.execute(

        """
        SELECT

        food_name,

        health_score,

        healthy_status

        FROM inspections

        ORDER BY created_at DESC

        LIMIT 10
        """

    )

    recent = cursor.fetchall()

    cursor.close()

    connection.close()

    admin_data = {

        "users": users,

        "inspections": inspections,

        "healthy": healthy,

        "unhealthy": unhealthy,

        "recent": recent

    }

    return render_template(

        "admin.html",

        admin=admin_data

    )


# ================= LOGOUT =================

@app.route("/logout")

@login_required

def logout():

    logout_user()

    return redirect(

        url_for(

            "login"

        )

    )


if __name__ == "__main__":

    app.run(

        debug=True

    )