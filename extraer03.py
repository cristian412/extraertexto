import g4f

try:
    respuesta = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente experto en derecho especializado en el análisis de mandamientos judiciales. Tu objetivo es extraer información clave como las partes involucradas, el objeto del litigio, el juzgado y la fecha del mandamiento, y proporcionar un resumen claro y conciso de la información relevante. Formatea la respuesta como una lista de puntos."
            },
            {"role": "user", "content": "dime qué es el código civil"}
        ],
        provider=g4f.Provider.FreeGpt
    )

    if respuesta:
        print("Respuesta de la API:")
        print(respuesta)
    else:
        print("La respuesta fue None.")

except Exception as e:
    print(f"Error al llamar a la API: {str(e)}")
    # Aquí podrías agregar código para registrar el error en un archivo o enviarlo a un servicio de seguimiento de errores.