# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 01: VARIABLES Y TIPOS DE DATOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: MI TARJETA DE PRESENTACIÓN
#   ----------------------------------------------------------------------
#   Enunciado: Crea tres variables: una para tu nombre, otra para tu edad
#   (debe ser un entero) y otra para tu pais. Luego, usa tres funciones
#   print() diferentes para mostrar cada valor en la consola.
# //======================================================================

# 1. Declaración de variables
# Creamos las variables asignándoles un valor. Python detecta el tipo automaticamente.
nombre = "Tu nombre" # Tipo: str(String / Texto)
edad = 18 # Tipo: int(Integer/Entero)
pais = "España" # Tipo: str(String / Texto)

# 2. Mostrar Resultados en Consola (Explicación de métodos)
#
# -- Método 1: Usando comas (Recomendación para principiantes) ----
# Al usar la coma (,), Python hace dos cosas automáticamente:
#  1. Convierte cualquier dato (como el entero de la edad) a texto para mostrarlo
#  2. Añade un espacio en blanco automático entre los elementos.#
print("Mi nombre es:",nombre)
print("Mi edad es:",edad) 
print("Mi pais es:",pais)

print("\n"+"-"*40 + "\n") # Esto es solo una línea divisoria en la consola

#
# --- ⚠️ EL ERROR COMÚN CON EL OPERADOR SÍMBOLICO MÁS (+) ---
# Si intentas hacer esto:
# print("Mi edad es: "+edad)
# 
# Python lanzará un error de tipo: 'TypeError: can only concatenate str (not "int") to str'.
# ¿Por qué? Porque el signo "+" sirve para SUMAR números o para PEGAR (concatenar) textos.
# Python se vuelve loco porque no sabe si quieres sumar texto con un número o qué hacer.
# 
# Si por cojones quieres usar el "+" tendrías que transformar el número a texto manualmente así:
# print("Mi edad es: "+str(edad)) # <- Esto si funcionaria, pero es más pesado de escribir.

# --- Metodo 2: Las F-Strings (El estándar profesional en Python) ---
# Colocando una "f" antes de las comillas, puedes meter las variales directamente
# dentro del texto usando llaves {}. Es el método más limpio, rápido y moderno.#
print(f"Hola mi nombre es {nombre}, tengo {edad} años y vivo en {pais}.")