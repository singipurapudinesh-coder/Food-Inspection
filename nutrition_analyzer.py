def estimate_nutrition(

food_name

):

    food = food_name.lower()


    database = {

        "biryani":{

            "calories":750,

            "protein":28,

            "fat":34,

            "carbohydrates":82

        },


        "pizza":{

            "calories":900,

            "protein":32,

            "fat":42,

            "carbohydrates":96

        },


        "salad":{

            "calories":220,

            "protein":8,

            "fat":6,

            "carbohydrates":18

        },


        "apple":{

            "calories":95,

            "protein":1,

            "fat":0,

            "carbohydrates":25

        }

    }


    return database.get(

        food,

        {

        "calories":0,

        "protein":0,

        "fat":0,

        "carbohydrates":0

        }

    )