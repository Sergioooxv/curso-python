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

# 1. CAPTURA DE DATOS (Manejamos floats para dinero)
euros = float(input("¿Qué cantidad de dinero en Euros tienes?: "))
moneda = input("¿Qué moneda quieres convertir tus euros? (Ej: USD/GBP/JPY): ")

# 2. PROCESAMIENTO CON LIMPIEZA DINÁMICA DE STRINGS
if moneda.upper() == "USD":
    cambio = euros * 1.10
    print(f"Tus {euros:.2f}€ son {cambio:.2f} USD (Dolares)")
elif moneda.upper() == "GBP":
    cambio = euros * 0.85
    print(f"Tus {euros:.2f}€ son {cambio:.2f} GBP (Libras)")
elif moneda.upper() == "JPY":
    cambio = euros * 160.0
    print(f"Tus {euros:.2f}€ son {cambio:.2f} JPY (Yenes)")
else:
    # Red de seguridad contra datos erróneos
    print(f"La moneda introducida no esta soportada: {moneda}")
    
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Sanitización y control de excepciones lógicas)
# ==============================================================================
# En el desarrollo de software moderno, hay una máxima que todo programador debe grabar 
# a fuego en su mente: "Nunca te fíes de los datos que introduce el usuario". Un 
# usuario puede escribir "usd", "Usd", "USD" o incluso equivocarse de palabra.
# 
# 🧼 SANITIZACIÓN AL VUELO CON '.upper()':
# En lugar de obligar al alumno a escribir una condición gigantesca llena de operadores
# lógicos como 'if moneda == "USD" or moneda == "usd" or moneda == "Usd":', Python nos 
# permite "sanitizar" el dato de forma sutil.
# Al evaluar 'moneda.upper()', transformamos temporalmente la cadena a mayúsculas en el
# mismo instante de la comparación. Si el usuario escribió "gbp", Python lo lee internamente
# como "GBP" y la condición se cumple limpiamente. ¡Código más corto es igual a código con menos fallas!
# 
# 🛡️ EL 'ELSE' COMO GESTOR DE ERRORES:
# En aplicaciones profesionales, el bloque 'else' final no es un simple descarte; funciona como una
# "red de captura" (fallback) para evitar corrupciones de flujo. Si el usuario introduce "Pesos", y
# no tuviéramos un 'else', el programa terminaría en silencio sin hacer nada, dejando al usuario confundido.
# El 'else' intercepta cualquier dato no completado en los 'if/elif' y ofrece una respuesta controlada y elegante.
# ==============================================================================