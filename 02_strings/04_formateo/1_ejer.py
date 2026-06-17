# ==============================================================================
# 🗃️ BLOQUE 02: STRINGS | TEMA 04: FORMATEO
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: EL ARQUEÓLOGO DEL CÓDIGO (OPERADOR %)
#   ----------------------------------------------------------------------
#   Enunciado: Te han contratado para actualizar un script del año 2010. 
#   Te encuentras con esta línea que usa el viejo operador '%':
#      'mensaje = "Usuario: %s | Intentos: %d" % (nombre, intentos)'
#   Declara las variables nombre = "Admin" e intentos = 3, y reescribe 
#   ese mensaje usando una f-string moderna.
# //======================================================================

# 1. DECLARACIÓN DE VARIABLES
nombre = "Tu Nombre"
intentos = 3

# 2. SISTEMA ANTIGUO (Operador % - Estilo prehístórico)
mensaje = "usuario: %s | Intentos: %d" % (nombre, intentos)
print(f"Frase original: {mensaje}")

# 3. REFACTORIZACIÓN MODERNA (f-strings - Estilo actual)
mensaje = f"Usuario {nombre} | Intentos: {intentos}"
print(f"Frase con f-strings: {mensaje}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Viaje en el tiempo informático)
# ==============================================================================
# Aunque hoy en día las f-strings nos parecen lo más normal del mundo, no siempre
# estuvieron ahí (se añadieron a partir de Python 3.6). En el código antiguo,
# verás constantemente el operador '%'.
# 
# ¿CÓMO FUNCIONABA ESE MAPA HISTÓRICO?
# El sistema funcionaba dejando "comodines" o marcadores dentro del texto según
# el tipo de dato que se iba a meter:
#  - '%s' significaba "aquí va un String (texto)".
#  - '%d' significaba "aquí va un Digit (número entero)".
# Al final del texto, se ponía otro '%' y una tupla con las variables en el mismo
# orden en el que debían encajar.
# 
# 🕵️‍♂️ ¿POR QUÉ ERA PEOR QUE LAS F-STRINGS?
# 1. Dificil de leer: Tienes que ir saltando con la mirada del centro del texto al 
# final para saber qué variable va en cada sitio.
# 2. Propenso a errores: Si te equivocabas de orden o ponías un '%d' en una variable
# que guardaba texto, el programa se romía de inmediato.
# 
# Al actualizarlo a 'f"Usuario: {nombre}"', el código se lee de un solo vistazo,
# es infinitamente más limpio y mucho más seguro. ¡Acabas de hacer tu primera 
# refactorización!
# ==============================================================================