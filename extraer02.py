import g4f

def extraer_datos_ia(texto):
    """
    Envía un texto a GPT-4 usando GPT4Free y extrae información clave.
    """
    try:
        respuesta = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",  # También podés probar con "gpt-3.5-turbo" gpt-4
            messages=[
                {"role": "system", "content": "Sos un asistente experto en derecho que extrae información clave de mandamientos judiciales."},
                {"role": "user", "content": f"""
                    Extraé los siguientes datos del mandamiento:
                    - Nombre del afectado
                    - Cédula de identidad
                    - Tipo de acción (Ej: embargo, notificación, etc.)
                    - Número de expediente
                    - Juzgado interviniente

                    Texto del mandamiento:
                    {texto}
                    
                    Formateá la respuesta en JSON con las claves 'nombre', 'ci', 'accion', 'expediente' y 'juzgado'.
                """}
            ],
            provider=g4f.Provider.FreeGpt  # Usa servidores gratuitos
        )


        # Verificar si la respuesta está correctamente estructurada
        if respuesta:
            #print("Respuesta de la API:", respuesta)  # Imprimir la respuesta para ver lo que devuelve
            return respuesta
        else:
            return "Error recib: No se recibió respuesta de la API."

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Texto de ejemplo
    test_texto = """
    EL OFICIAL DE JUSTICIA, a quien fuere entregado el presente mandamiento de INTIMACIÓN DE PAGO Y EMBARGO EJECUTIVO, acompañado de un Escribano Público o en su defecto de dos (2) testigos hábiles, se constituirá ante la parte demandada, los Sres. HUGO JAVIER FRUTOS VILLALBA, con C.I. Nº 3.774.033; y GABRIEL EUSEBIO QUINTANA CAPDEVILA, con C.I. Nº 3.836.802, ambos con domicilio en la calle Nanawa esq. Kuarahy (a media cuadra del colegio San Antonio), Barrio Laurelty, de la ciudad de Luque, y les intimará a que den y paguen en el acto de requerimiento la suma de GUARANÍES TREINTA Y CINCO MILLONES OCHOCIENTOS OCHENTA Y NUEVE MIL SEISCIENTOS SETENTA NUEVE (Gs.35.889.679,-), que se les reclama en el juicio caratulado: "UNIÓN NEGOCIOS Y COBRANZAS SOCIEDAD ANÓNIMA C/ HUGO JAVIER FRUTOS VILLALBA Y OTRO S/ ACCIÓN PREPARATORIA DE JUICIO EJECUTIVO"; Nº 371; AÑO: 2023; SECRETARÍA Nº 39.- NO VERIFICÁNDOSE el pago, procederá a trabar EMBARGO EJECUTIVO, decretado por A.I. Nº 487 de fecha 21 de agosto de 2024, sobre bienes suficientes de la parte demandada hasta cubrir la suma reclamada, más la de GUARANÍES TRES MILLONES QUINIENTOS OCHENTA Y OCHO MIL NOVECIENTOS SESENTA Y SIETE (Gs.3.588.967,-), que el Juzgado fija provisoriamente para gastos de justicia.- PARA el mejor cumplimiento de su cometido, podrá solicitar y obtener el auxilio de la fuerza pública y allanar domicilio si necesario fuere, debiendo actuar en todo conforme a derecho. Dejará además en poder del demandado el duplicado firmado, con la indicación del día y hora de su diligenciamiento, de conformidad con el Art. 451 del C.P.C. e importa la obligación de constituir, en el mismo plazo y domicilio dentro del radio de esta ciudad, bajo apercibimiento de lo dispuesto en el Art. 48 del C.P.C.- DADO, FIRMADO Y SELLADO en la Sala de Audiencias y Público despacho de S.S., el Señor JUEZ DE PRIMERA INSTANCIA EN LO CIVIL Y COMERCIAL DEL VIGÉSIMO TURNO, en la ciudad de Asunción, 23 de agosto de 2024.- Ante mí:
    """
    # Llamar a la función para extraer datos
    datos_extraidos = extraer_datos_ia(test_texto)

    # Mostrar la respuesta
    print("\nDatos extraídos:\n", datos_extraidos)
