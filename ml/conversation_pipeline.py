from ml.core.document_conversion import extract_images
from ml.llm.utiils import pipeline
from ml.core.utilities import preprocess_image
from ml.core.document_generator import generate_output_text
import numpy as np
from PIL import Image
import io


def get_data(files: list[np.array] = None):
    image_np = files
    image_np = preprocess_image(image_np)
    image_np = (image_np * 255).astype(np.uint8)
    with io.BytesIO() as output:
        Image.fromarray(image_np).save(output, format='PNG')
        files = output.getvalue()
    return files


def result_pipeline(files: list[np.array]) -> str:
    if len(files) == 1:
        files = [files]

    preprocess_files = []
    for file in files:
        preprocess_files.append(get_data(file))

    images = extract_images(files=preprocess_files)
    text_from_ocr = generate_output_text(images)
    rules, json = pipeline(text_from_ocr)
    return json, rules


if __name__ == '__main__':
    print(result_pipeline(None))
