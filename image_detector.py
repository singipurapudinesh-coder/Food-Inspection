import cv2


def detect_food(image_path):

    image = cv2.imread(image_path)

    image = cv2.resize(

        image,

        (500,500)

    )

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    return gray