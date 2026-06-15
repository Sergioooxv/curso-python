# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 02: INPUT Y OUTPUT
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: EL SALUDO PERSONALIZADO
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario su nombre y su apellido usando dos funciones
#   input() diferentes. Luego, muestra un único saludo en la consola 
#   usando f-strings que diga: "¡Hola [nombre] [apellido]! Qué bueno tenerte aquí."
# //======================================================================

# 1. ENTRADA DE DATOS (INPUT)
# Pistas de diseño: Dejar un espacio al final dentro del input evita que la
# respeusta del usuario se peque a la pregunta en la terminal#
nombre = input("¿Cúal es tu nombre? ")
apellido = input("¿Cúal es tu apellido? ")

# 2. SALIDA DE DATOS (OUTPUT)
# Usamos una f-string (anteponiendo la 'f' antes de las comillas).
# Esto nos permite inyectar las variables directamente entre llaves {}#
print(f"Hola {nombre} {apellido}! Qué bueno tenerte aquí.")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (¿Qué acaba de pasar aquí?)
# ==============================================================================
# La función 'input()' hace dos cosas:
#  1. Muestra el texto que tiene entre paréntesis en la pantalla.
#  2. Pausa el programa por completo y espera a que el usuario escriba algo
#     y pulse la tecla 'Enter'.
# 
# En cuanto pulsas Enter, lo que hayas escrito viaja hacia atrás y se guarda
# dentro de la variale (en este caso, 'nombre' y 'apellido'
# 
# Luego, gracias a las f-strings, podemos fusionar ese texto guardado con 
# nuestro saludo de una forma súper cómoda, sin andar pegado texto con el singo
# '+'
# ==============================================================================