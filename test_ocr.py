from paddleocr import PaddleOCR
import cv2

# Inicializa OCR en español
ocr = PaddleOCR(use_angle_cls=True, lang='es')

# Ruta a la imagen de prueba (ajusta según dónde esté tu ejemplo)
IMAGE_PATH = "examples/cedula.jpg"

# Carga la imagen
img = cv2.imread(IMAGE_PATH)

# Ejecuta OCR
result = ocr.ocr(img, cls=True)

# Imprime las líneas detectadas
print("=== Texto detectado ===")
for line in result[0]:
    print(line[1][0])
