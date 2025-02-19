
import g4f

# Texto de ejemplo
test_texto = """
EI Oficial de Justicia a quien fuere entregado eI presente mandamiento de intimación de pago y embargo ejecutivo, en virtud a lo dispuesto por providencia de esta misma fecha, se constituirá ante ei Sr. MARCOS ANTONIO VERA ROLON C.I. NO 3.985.964, con domicilio en la casa de la calle Damas Argentinas y Dublin N0386 de la Ciudad de Asunción A.I. NO: 949, y le intimará a que dé y pague en el acto de requerimiento la suma de GUARANIES DOS MILLONES QUINIENTOS CUARENTA MIL NOVECIENTOS OCHENTA Y OCHO (gs.2.540.988.-), más la suma de GUARANIES DOCIENTOS CINCUENTA Y CUATRO MIL NOVENTA Y OCHO (gs. 254.098) en concepto de Impuesto al Valor Agregado (1.V.A), que le reclama la Abg. MARIA TERESA AÑAZCO, según documentos presentados en los autos caratulados R.H.P. DE LA ABOG. MARIA TERESA AÑAZCO EN EL EXPEDIENTE: COOP STMA. TRINIDAD LTDA. C/ MARCOS ANTONIO VERA ROLON S/ ACCIÓN EJECUTIVA.- No haciéndolo voluntariamente procederá a trabar embargo ejecutivo sobre bienes suficientes del deudor hasta cubrir el monto reclamado y mas la suma de GUARANIES DOCIENTOS CINCUENTA Y CUATRO MIL NOVENTA Y OCHO (gs. 254.098) correspondientes a los gastos causídicos Para el fiel cumplimiento de su cometido indicado precedentemente, podrá debiendo en todo momento proceder conforme a derecho y a 10 dispuesto en el Art. 451 del C.P.C.- Dado, firmado y sellado, en la Sala de Audiencias y Público Despacho de S.S. el Juez de Primera Instancia en 10 Civil y Comercial del Segundo Turno, Abg. ARNALDO MARTINEZ ROZZANO, en la ciudad de Asunción, ASUNCIÓN, ASUNCION, 13 de Diciembre de 2024 Ante mí: Firmado di talm tepor.N ELIA MARIA RAMON MIRTINEZ POiZANO (JUEZA) ORTIZ RIO/A) 
"""


client = g4f.ChatCompletion.create(
    model="gpt-4o-mini",
    provider=g4f.Provider.Free2GPT,  # Forzar un proveedor específico
    messages=[
                {"role": "user", "content": f"""
                    Extraé los siguientes datos del mandamiento:
                    - Nombre del afectado
                    - Cédula de identidad
                    - Domicilio
                    - Tipo de acción (Ej: Ejecutivo, Preventivo)
                    - Juzgado interviniente
                    - caratula
                    - monto
                    - gastos de justicia
                    
                    Formateá la respuesta en JSON con las claves 
                    'nombre', 'cedula_identidad','domicilio', 'accion', 'caratula', 'monto','gastos_justicia','juzgado_interviniente'.

                    Texto del mandamiento:
                    {test_texto}
                    
                    
                """}

    ]
)

print(client)