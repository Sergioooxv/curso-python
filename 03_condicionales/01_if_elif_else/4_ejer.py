# ==============================================================================
# //======================================================================
#   EJERCICIO 4: ASISTENTE DE CONVERSIÓN DE DIVISAS
#   ----------------------------------------------------------------------
#   Enunciado: Desarrolla un conversor de moneda inteligente. El usuario debe 
#   introducir una 'cantidad' de dinero en Euros (€) y luego escribir a qué 
#   moneda quiere convertir: "USD" (Dólares), "GBP" (Libras) o "JPY" (Yenes).
#
#   Tasas de cambio ficticias:
#   - De EUR a USD: multiplica por 1.10
#   - De EUR a GBP: multiplica por 0.85
#   - De EUR a JPY: multiplica por 160.0
#
#   Requisitos del script:
#   - Controla si el usuario escribe el código de la moneda en minúsculas 
#     pasándolo a mayúsculas automáticamente con un método de string.
#   - Si introduce una moneda que no sea ninguna de las tres, el sistema debe 
#     mostrar un mensaje de error claro en el 'else' advirtiendo del fallo.
# //======================================================================