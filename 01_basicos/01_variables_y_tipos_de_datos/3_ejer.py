# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 01: VARIABLES Y TIPOS DE DATOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 3: INVESTIGANDO TIPOS
#   ----------------------------------------------------------------------
#   Enunciado: Crea cuatro variables con los valores: 100, 12.5, "Python" y True.
#   Utiliza 'print(type(...))' para mostrar en consola de qué tipo es cada una.
# //======================================================================

# 1. CREACIÓN DE VARIABLES (Estilo snake_case)
numero_entero = 100
numero_decimal = 12.5
texto = "Python"
booleano = True

# 2. INVESTIGANDO LOS TIPOS CON TYPE()
# Pasamos la variable dentro de type(), y todo eso dentro de print() para verlo.
print("Esto es un entero:",type(numero_entero))
print("Esto es un decimal:",type(numero_decimal))
print("Esto es un String/Texto:",type(texto))
print("Esto es un Booleano",type(booleano))

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Entendiendo la consola)
# ==============================================================================
# Cuando ejecutes este programa, veras que Python te devuelve algo raro como:
# '<class 'int'>' o '<class 'str'>'. ¿Qué significa esa palabra 'class'?
# 
# En Python, Todo es un "objeto" creado a partir de una "clase" (un molde).
# Así que Python te está diciendo: "Esta variable pertenece a la clase de los 
# enteros.
# 
# 💡 REPASO DE TIPOS:
#  - 'int' -> Integer (Números enteros, sin decimales).
#  - 'float' -> Floating Point (Números de punto flotante/decimales).
#  - 'str' -> String (Cadenas de texto, siempre van entre comillas).
#  - 'bool' -> Boolean (Solo acepta True o False. Ojo: ¡La primera va en Mayus!)
# 
# ¿TE has dado cuenta de que no hemos tenido que escribir en ningún lado que 100
# era un número o que "Python" era texto? A esto se le llama TIPADO DINAMICO.
# Python analiza el valor que metes en la variable en tiempo de ejecución y decide
# el tipo por ti. ¡Magia!
# ==============================================================================
