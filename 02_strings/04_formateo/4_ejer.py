# ==============================================================================
# //======================================================================
#   EJERCICIO 4: CÓDIGOS DE FACTURA (RELLENO DE CEROS)
#   ----------------------------------------------------------------------
#   Enunciado: En tu sistema de facturación, los números de cliente deben tener 
#   siempre 4 dígitos. Si un cliente tiene el ID 7, la factura debe poner "0007".
#   Dada la variable 'id_cliente = 54', usa el formateo de f-strings para 
#   imprimir el ID formateado con ceros a la izquierda hasta cumplir los 4 dígitos.
# //======================================================================

# 1. VARIABLE DE ENTRADA (ID numérico en bruto)
id_cliente = 54

# 2. SALIDA DE DATOS CON RELLENO DE CEROS
# El modificador :04d obliga a tener un ancho de 4 dígitos rellenando con ceros
print(f"El ID del cliente es: {id_cliente:04d}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Generación de códigos fijos)
# ==============================================================================
# En el mundo de la gestión empresarial, las facturas, los códigos de barras y los 
# identificadores suelen tener una longitud fija para que las bases de datos no se 
# desordenen. 
#
# Al poner ':04d' dentro de las llaves, le estamos dando un patrón estricto a Python:
#   - El ':' activa la configuración del formateo.
#   - El '0' inicial le dice: "Si quedan huecos vacíos, rellénalos con ceros".
#   - El '4' especifica el ancho total obligatorio que debe tener el texto en pantalla.
#   - La 'd' le avisa de que el dato original es un 'Digit' (un número entero).
#
# 🤯 ¿CÓMO REACCIONA EL PROGRAMA SEGÚN EL NÚMERO?
#   - Si el ID fuera 7 ➡️ Python dibuja 3 ceros: '0007'.
#   - Si el ID fuera 54 (nuestro caso) ➡️ Python dibuja 2 ceros: '0054'.
#   - Si el ID fuera 9999 ➡️ No dibuja ningún cero porque ya ocupa las 4 casillas.
#   - Si el ID fuera 12345 ➡️ ¡OJO! Python no recortará el número; lo mostrará entero 
#     para no destruir la información real del ID.
# ==============================================================================