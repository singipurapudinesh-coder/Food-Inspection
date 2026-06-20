from flask import send_file

from reportlab.platypus import (

SimpleDocTemplate,

Paragraph,

Spacer

)

from reportlab.lib.styles import (

getSampleStyleSheet

)


def create_pdf(

report

):

    filename = "Food_Report.pdf"

    pdf = SimpleDocTemplate(

    filename

    )

    styles = getSampleStyleSheet()

    story = []


    story.append(

    Paragraph(

    "AI Food Inspection Report",

    styles["Title"]

    )

    )


    story.append(

    Spacer(

    1,

    10

    )

    )


    for key,value in report.items():

        story.append(

        Paragraph(

        f"<b>{key}</b> : {value}",

        styles["BodyText"]

        )

        )


    pdf.build(

    story

    )


    return send_file(

        filename,

        as_attachment=True

    )