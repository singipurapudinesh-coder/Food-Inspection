from PIL import Image

import numpy as np


def detect_freshness(

image_path

):

    image = Image.open(

    image_path

    )

    image = image.resize(

    (300,300)

    )

    image = np.array(

    image

    )

    brightness = image.mean()


    if brightness > 170:

        return "Fresh"


    elif brightness > 110:

        return "Moderately Fresh"


    return "Not Fresh"