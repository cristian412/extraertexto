from flask import Flask, request, jsonify
import requests
from PIL import Image
from io import BytesIO
import pytesseract
from g4f.client import Client

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"mensaje": "¡Hola, mundo!"})


@app.route("/test", methods=["GET"])
def test():
    # Texto de ejemplo
    test_texto = f"""
    EL OFICIAL DE JUSTICIA, a quien fuere entregado el presente mandamiento de INTIMACIÓN DE PAGO Y EMBARGO EJECUTIVO, acompañado de un Escribano Público o en su d
    efecto de dos (2) testigos hábiles, se constituirá ante la parte demandada, los Sres. HUGO JAVIER FRUTOS VILLALBA, con C.I. Nº 3.774.033; y 
    GABRIEL EUSEBIO QUINTANA CAPDEVILA, con C.I. Nº 3.836.802, ambos con domicilio en la calle Nanawa esq. Kuarahy (a media cuadra del colegio San Antonio), 
    Barrio Laurelty, de la ciudad de Luque, y les intimará a que den y paguen en el acto de requerimiento la suma de GUARANÍES TREINTA Y CINCO MILLONES 
    OCHOCIENTOS OCHENTA Y NUEVE MIL SEISCIENTOS SETENTA NUEVE (Gs.35.889.679,-), que se les reclama en el juicio caratulado: "UNIÓN NEGOCIOS Y COBRANZAS 
    SOCIEDAD ANÓNIMA C/ HUGO JAVIER FRUTOS VILLALBA Y OTRO S/ ACCIÓN PREPARATORIA DE JUICIO EJECUTIVO"; Nº 371; AÑO: 2023; SECRETARÍA Nº 39.- 
    NO VERIFICÁNDOSE el pago, procederá a trabar EMBARGO EJECUTIVO, decretado por A.I. Nº 487 de fecha 21 de agosto de 2024, sobre bienes suficientes de la 
    parte demandada hasta cubrir la suma reclamada, más la de GUARANÍES TRES MILLONES QUINIENTOS OCHENTA Y OCHO MIL NOVECIENTOS SESENTA Y SIETE (Gs.3.588.967,-), 
    que el Juzgado fija provisoriamente para gastos de justicia.- PARA el mejor cumplimiento de su cometido, podrá solicitar y obtener el auxilio de la fuerza 
    pública y allanar domicilio si necesario fuere, debiendo actuar en todo conforme a derecho. Dejará además en poder del demandado el duplicado firmado, 
    con la indicación del día y hora de su diligenciamiento, de conformidad con el Art. 451 del C.P.C. e importa la obligación de constituir, en el mismo 
    plazo y domicilio dentro del radio de esta ciudad, bajo apercibimiento de lo dispuesto en el Art. 48 del C.P.C.- DADO, FIRMADO Y SELLADO en la Sala de 
    Audiencias y Público despacho de S.S., el Señor JUEZ DE PRIMERA INSTANCIA EN LO CIVIL Y COMERCIAL DEL VIGÉSIMO TURNO, en la ciudad de Asunción, 23 de 
    agosto de 2024.- Ante mí:
    """

    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                    {"role": "user", "content": f"""
                        Extraé los siguientes datos del mandamiento:
                        - Nombre del afectado
                        - Cédula de identidad
                        - Domicilio
                        - Tipo de acción (Ej: embargo, notificación, etc.)
                        - Juzgado interviniente
                        - caratula
                        - monto
                        - gastos de justicia

                        Texto del mandamiento:
                        {test_texto}
                        
                        Formateá la respuesta en JSON con las claves 'nombre', 'cedula_identidad','domicilio', 'accion', 'caratula', 'monto','gastos_justicia','juzgado_interviniente'.
                    """}

        ],
        web_search=False
    )
    return response.choices[0].message.content

@app.route("/procesar", methods=["GET"])
def procesar():
    # Obtener la URL de la imagen desde los parámetros de la consulta
    imagen_url = request.args.get("url")
    
    if not imagen_url:
        return jsonify({"error": "Falta la URL de la imagen"}), 400
    
    try:
        # Descargar la imagen
        response = requests.get(imagen_url)
        
        # Verificar que la respuesta fue exitosa y que el contenido es una imagen
        if response.status_code != 200:
            return jsonify({"error": "No se pudo descargar la imagen. Código de estado: " + str(response.status_code)}), 400
        
        # Verificar el tipo de contenido
        if "image" not in response.headers.get("Content-Type", ""):
            return jsonify({"error": "La URL proporcionada no apunta a una imagen válida."}), 400
        
        # Intentar abrir la imagen
        image = Image.open(BytesIO(response.content))
        
        # Extraer texto con OCR
        texto = pytesseract.image_to_string(image)
        
        # Llamada a la API para procesar el texto
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"""
                    Extraé los siguientes datos del mandamiento:
                    - Nombre del afectado
                    - Cédula de identidad
                    - Domicilio
                    - Tipo de acción (Ej: embargo, notificación, etc.)
                    - Juzgado interviniente
                    - caratula
                    - monto
                    - gastos de justicia

                    Texto del mandamiento:
                    {texto}
                    
                    Formateá la respuesta en JSON con las claves 'nombre', 'cedula_identidad', 'domicilio', 'accion', 'caratula', 'monto', 'gastos_justicia', 'juzgado_interviniente'.
                """}
            ],
            web_search=False
        )
        return jsonify({"respuesta": response.choices[0].message.content})
    
    except Exception as e:
        return jsonify({"error": f"Error al procesar la imagen: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"mensaje": "¡Hola, mundo!"})


@app.route("/test", methods=["GET"])
def test():
    # Texto de ejemplo
    test_texto = f"""
    EL OFICIAL DE JUSTICIA, a quien fuere entregado el presente mandamiento de INTIMACIÓN DE PAGO Y EMBARGO EJECUTIVO, acompañado de un Escribano Público o en su d
    efecto de dos (2) testigos hábiles, se constituirá ante la parte demandada, los Sres. HUGO JAVIER FRUTOS VILLALBA, con C.I. Nº 3.774.033; y 
    GABRIEL EUSEBIO QUINTANA CAPDEVILA, con C.I. Nº 3.836.802, ambos con domicilio en la calle Nanawa esq. Kuarahy (a media cuadra del colegio San Antonio), 
    Barrio Laurelty, de la ciudad de Luque, y les intimará a que den y paguen en el acto de requerimiento la suma de GUARANÍES TREINTA Y CINCO MILLONES 
    OCHOCIENTOS OCHENTA Y NUEVE MIL SEISCIENTOS SETENTA NUEVE (Gs.35.889.679,-), que se les reclama en el juicio caratulado: "UNIÓN NEGOCIOS Y COBRANZAS 
    SOCIEDAD ANÓNIMA C/ HUGO JAVIER FRUTOS VILLALBA Y OTRO S/ ACCIÓN PREPARATORIA DE JUICIO EJECUTIVO"; Nº 371; AÑO: 2023; SECRETARÍA Nº 39.- 
    NO VERIFICÁNDOSE el pago, procederá a trabar EMBARGO EJECUTIVO, decretado por A.I. Nº 487 de fecha 21 de agosto de 2024, sobre bienes suficientes de la 
    parte demandada hasta cubrir la suma reclamada, más la de GUARANÍES TRES MILLONES QUINIENTOS OCHENTA Y OCHO MIL NOVECIENTOS SESENTA Y SIETE (Gs.3.588.967,-), 
    que el Juzgado fija provisoriamente para gastos de justicia.- PARA el mejor cumplimiento de su cometido, podrá solicitar y obtener el auxilio de la fuerza 
    pública y allanar domicilio si necesario fuere, debiendo actuar en todo conforme a derecho. Dejará además en poder del demandado el duplicado firmado, 
    con la indicación del día y hora de su diligenciamiento, de conformidad con el Art. 451 del C.P.C. e importa la obligación de constituir, en el mismo 
    plazo y domicilio dentro del radio de esta ciudad, bajo apercibimiento de lo dispuesto en el Art. 48 del C.P.C.- DADO, FIRMADO Y SELLADO en la Sala de 
    Audiencias y Público despacho de S.S., el Señor JUEZ DE PRIMERA INSTANCIA EN LO CIVIL Y COMERCIAL DEL VIGÉSIMO TURNO, en la ciudad de Asunción, 23 de 
    agosto de 2024.- Ante mí:
    """

    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                    {"role": "user", "content": f"""
                        Extraé los siguientes datos del mandamiento:
                        - Nombre del afectado
                        - Cédula de identidad
                        - Domicilio
                        - Tipo de acción (Ej: embargo, notificación, etc.)
                        - Juzgado interviniente
                        - caratula
                        - monto
                        - gastos de justicia

                        Texto del mandamiento:
                        {test_texto}
                        
                        Formateá la respuesta en JSON con las claves 'nombre', 'cedula_identidad','domicilio', 'accion', 'caratula', 'monto','gastos_justicia','juzgado_interviniente'.
                    """}

        ],
        web_search=False
    )
    return response.choices[0].message.content

@app.route("/procesar", methods=["GET"])
def procesar():
    # Obtener la URL de la imagen desde los parámetros de la consulta
    imagen_url = request.args.get("url")
    
    if not imagen_url:
        return jsonify({"error": "Falta la URL de la imagen"}), 400
    
    try:
        # Descargar la imagen
        response = requests.get(imagen_url)
        image = Image.open(BytesIO(response.content))
        
        # Extraer texto con OCR
        texto = pytesseract.image_to_string(image)
        
        # # Simulación de procesamiento del texto
        # resultado = {"texto_extraido": texto, "mensaje": "Procesamiento exitoso"}
        # # Enviar resultados a tu backend (simulado)
        # requests.post("https://tu-backend.com/api/guardar", json=resultado)
        # return jsonify(resultado)

        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                        {"role": "user", "content": f"""
                            Extraé los siguientes datos del mandamiento:
                            - Nombre del afectado
                            - Cédula de identidad
                            - Domicilio
                            - Tipo de acción (Ej: embargo, notificación, etc.)
                            - Juzgado interviniente
                            - caratula
                            - monto
                            - gastos de justicia

                            Texto del mandamiento:
                            {texto}
                            
                            Formateá la respuesta en JSON con las claves 'nombre', 'cedula_identidad','domicilio', 'accion', 'caratula', 'monto','gastos_justicia','juzgado_interviniente'.
                        """}

            ],
            web_search=False
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
