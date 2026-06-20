from flask_login import UserMixin

from models.database import get_connection


class User(UserMixin):

    def __init__(
        self,
        id,
        name,
        email,
        role
    ):

        self.id = id
        self.name = name
        self.email = email
        self.role = role


    @staticmethod
    def get_by_id(user_id):

        connection = get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(

            """
            SELECT *
            FROM users
            WHERE id=%s
            """,

            (user_id,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            return User(

                user["id"],
                user["name"],
                user["email"],
                user["role"]

            )

        return None


    @staticmethod
    def get_by_email(email):

        connection = get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(

            """
            SELECT *
            FROM users
            WHERE email=%s
            """,

            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user


    @staticmethod
    def create_user(
        name,
        email,
        hashed_password
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO users(
                name,
                email,
                password
            )
            VALUES(
                %s,
                %s,
                %s
            )
            """,

            (
                name,
                email,
                hashed_password
            )

        )

        connection.commit()

        cursor.close()
        connection.close()


    @staticmethod
    def total_users():

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            SELECT COUNT(*)
            FROM users
            """
        )

        count = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return count