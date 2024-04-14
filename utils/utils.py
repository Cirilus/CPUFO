import base64
import io
import json
import re

import numpy as np
from PIL import Image


def base642nparray(base64_image: str):
    base64_decoded = base64.b64decode(base64_image)

    image = Image.open(io.BytesIO(base64_decoded))
    return np.array(image)


def str2json(string: str) -> dict:
    json_pattern = r'({[^{}]+})'
    json_match = re.search(json_pattern, string)

    try:
        if json_match:
            json_str = json_match.group()
            json_obj = json.loads(json_str)
            return json_obj
    except Exception as e:
        raise ValueError(f"error json loading: {string}")

    raise ValueError(f"there is no json in str {string}")
