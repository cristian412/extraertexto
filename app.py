from flask import Flask, request, jsonify
import requests
import pytesseract
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/procesar", methods=["POST"])
def procesar():
    # Recibe la URL de la imagen
    data = request.get_json()
    imagen_url = data.get("imagen_url")
    
    if not imagen_url:
        return jsonify({"error": "Falta la URL de la imagen"}), 400
    
    try:
        # Descargar la imagen
        response = requests.get(imagen_url)
        image = Image.open(BytesIO(response.content))
        
        # Extraer texto con OCR
        texto = pytesseract.image_to_string(image)
        
        # Simulación de procesamiento del texto
        resultado = {"texto_extraido": texto, "mensaje": "Procesamiento exitoso"}
        
        # Enviar resultados a tu backend (simulado)
        requests.post("https://tu-backend.com/api/guardar", json=resultado)
        
        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
