from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_info(image_path, doc_type):
    result = ocr.ocr(image_path, cls=True)
    text_lines = [line[1][0] for line in result[0]]

    extracted = {}
    for line in text_lines:
        lower = line.lower()
        if doc_type == "cedula":
            if "nombre" in lower:
                extracted["Nombre"] = line.split(":")[-1].strip()
            elif "número" in lower or "identidad" in lower:
                extracted["ID"] = line.split(":")[-1].strip()
        elif doc_type == "factura":
            if "nit" in lower:
                extracted["NIT"] = line.split(":")[-1].strip()
            elif "total" in lower:
                extracted["Total"] = line.split(":")[-1].strip()

    return extracted or {"Mensaje": "No se encontraron campos reconocibles."}