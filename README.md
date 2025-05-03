# Sistema OCR Inteligente con PaddleOCR

EL PROYECTO implementa un sistema de Reconocimiento Óptico de Caracteres (OCR) basado en **PaddleOCR**, capaz de identificar automáticamente el tipo de documento (como cédulas o facturas) y extraer información clave como número de identificación, nombre, entre otros. El sistema cuenta con una interfaz gráfica interactiva desarrollada con **Gradio**.

## Características

- 🔍 Detección automática del tipo de documento.
- 🧠 Extracción inteligente de campos clave (nombre, número de cédula, NIT, etc.).
- 🖼️ Soporte para imágenes o fotografías escaneadas de documentos.
- 💻 Interfaz web interactiva construida con Gradio.
- ⚙️ Basado en PaddleOCR, un motor de OCR de alto rendimiento.

## Estructura del proyecto

OCR_PADDLE_PROJECT/
│
├── __pycache__/
│   └── *.pyc                         # Archivos compilados
│
├── .venv/                            # Entorno virtual
│   └── Include, Lib, Scripts, ...
│
├── examples/
│   ├── cedula.jpg                    # Imagen de ejemplo
│   └── README.txt                    # Descripción de ejemplos
│
├── app.py                            # Aplicación principal con interfaz Gradio
├── app_old.py                        # Versión anterior de la aplicación
├── document_classifier.py            # Clasificación de tipo de documento
├── extract_fields.py                 # Extracción de campos específicos del documento
├── test_ocr.py                       # Script de prueba del sistema OCR
├── README.md                         # Este archivo
└── requirements.txt                  # Dependencias del proyecto



## Tecnologías utilizadas

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - Motor OCR basado en PaddlePaddle.
- [Gradio](https://www.gradio.app/) - Framework para crear interfaces de usuario en Python.
- Python 3.10+ (recomendado: 3.10 o 3.11)

## Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu_usuario/ocr_paddle_ready.git
cd ocr_paddle_ready
```

2. **Crear entorno virtual (opcional pero recomendado):**

```bash
python -m venv venv
venv\Scripts\activate   # En Windows
```

3. **Instalar PaddlePaddle:**

> Verifica que tu CPU sea compatible con AVX.

```bash
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
```

4. **Instalar dependencias restantes:**

```bash
pip install -r requirements.txt
```

## Ejecución

Para lanzar la aplicación, ejecuta:

```bash
python app.py
```

Esto abrirá una interfaz web local donde podrás subir imágenes de documentos y ver los resultados del OCR.

## Ejemplo de uso

- Subes una imagen de una **cédula** o **factura**.
- El sistema detecta automáticamente el tipo de documento.
- Extrae los campos relevantes y los muestra en la interfaz.

## Capturas

![Ejemplo de OCR](screenshots/ejemplo_ocr_cedula.png)

## Recomendaciones

- Las imágenes deben ser claras y estar enfocadas.
- Formatos soportados: JPG, PNG, JPEG.

## Licencia

MIT License.

## Autor

Juan Ardila – Bitcode IT Services  
Desarrollador de Software.