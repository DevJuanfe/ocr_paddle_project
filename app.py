import gradio as gr
from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='es')

def procesar_imagen(imagen):
    # Gradio entrega ruta o array; manejamos ambos casos
    if isinstance(imagen, str):
        img = cv2.imread(imagen)
    else:
        img = imagen[:, :, ::-1]  # RGB a BGR

    result = ocr.ocr(img, cls=True)
    texto = [line[1][0] for line in result[0]]
    return "\n".join(texto)

gr.Interface(
    fn=procesar_imagen,
    inputs=gr.Image(type="filepath"),
    outputs="textbox",
    title="App JF",
    description="Sube una imagen para convertir de imagen a texto"
).launch()
