import gradio as gr
from document_classifier import classify_document
from extract_fields import extract_info

def ocr_pipeline(image):
    doc_type = classify_document(image)
    extracted_data = extract_info(image, doc_type)
    return f"Tipo de documento: {doc_type}\n\nDatos extraídos:\n" + "\n".join(f"{k}: {v}" for k, v in extracted_data.items())

iface = gr.Interface(fn=ocr_pipeline,
                     inputs=gr.Image(type="filepath"),
                     outputs="text",
                     title="OCR Document Analyzer",
                     description="Sube una imagen de un documento para identificar el tipo y extraer información relevante.")
iface.launch()