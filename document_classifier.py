import cv2
import numpy as np
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def classify_document(image_path):
    result = ocr.ocr(image_path, cls=True)
    text = " ".join([line[1][0] for line in result[0]]).lower()

    if "cédula" in text or "número de identidad" in text:
        return "cedula"
    elif "factura" in text or "nit" in text:
        return "factura"
    else:
        return "desconocido"