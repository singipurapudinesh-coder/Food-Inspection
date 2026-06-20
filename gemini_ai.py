# utils/gemini_ai.py

import json
import os
import mimetypes

import google.generativeai as genai

from config import Config


genai.configure(
    api_key=Config.GEMINI_API_KEY
)


def get_default_result(error_message="Unable to analyze."):

    return {

        "food_name": "Unknown",

        "healthy_status": "Unknown",

        "health_score": 0,

        "calories": 0,

        "protein": 0,

        "fat": 0,

        "carbohydrates": 0,

        "freshness": "Unknown",

        "temperature_risk": "Unknown",

        "advantages": [],

        "disadvantages": [],

        "recommendation": "Unable to analyze.",

        "summary": error_message

    }


def analyze_food(prompt, image_path):

    try:

        if not os.path.exists(image_path):

            return get_default_result(

                "Image file not found."

            )

        mime_type, _ = mimetypes.guess_type(

            image_path

        )

        if mime_type is None:

            mime_type = "image/jpeg"

        with open(

            image_path,

            "rb"

        ) as image:

            image_data = image.read()

        model = genai.GenerativeModel(

            "gemini-2.5-flash"

        )

        ai_prompt = f"""
You are an AI food inspector.

Analyze BOTH:

1. The uploaded food image.
2. The user statement.

User statement:

{prompt}

Detect the food from the image.

Return ONLY VALID JSON.

Do not add explanations.

JSON format:

{{
"food_name":"",
"healthy_status":"",
"health_score":0,
"calories":0,
"protein":0,
"fat":0,
"carbohydrates":0,
"freshness":"",
"temperature_risk":"",
"advantages":[],
"disadvantages":[],
"recommendation":"",
"summary":""
}}

Rules:

healthy_status:

Healthy or Unhealthy

health_score:

0 to 100

freshness:

Fresh
Moderate
Not Fresh

temperature_risk:

Safe
Moderate Risk
High Risk

advantages:

minimum 3 items

disadvantages:

minimum 3 items

summary:

short paragraph

Return JSON only.
"""

        response = model.generate_content(

            [

                ai_prompt,

                {

                    "mime_type": mime_type,

                    "data": image_data

                }

            ]

        )

        text = response.text.strip()

        text = text.replace(

            "```json",

            ""

        )

        text = text.replace(

            "```",

            ""

        )

        text = text.strip()

        start = text.find("{")

        end = text.rfind("}")

        if start == -1 or end == -1:

            return get_default_result(

                "Gemini did not return JSON."

            )

        text = text[start:end + 1]

        data = json.loads(

            text

        )

        defaults = get_default_result()

        for key in defaults:

            if key not in data:

                data[key] = defaults[key]

        return data

    except Exception as e:

        print(

            "Gemini Error:",

            e

        )

        return get_default_result(

            str(e)

        )