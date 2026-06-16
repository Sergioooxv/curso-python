# ==============================================================================
# //======================================================================
#   EJERCICIO 3: EL ANALIZADOR DE TEXTO
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario que escriba una frase larga por teclado.
#   El programa debe calcular y mostrar de forma automática:
#     1. Cuántas veces aparece la letra 'a' (independientemente de si es 'A' o 'a').
#     2. Cuántos caracteres en total tiene la frase (pista: usa una función que ya conoces).
# //======================================================================

# 1. ENTRADA DE DATOS
frase = input("Escribe una frase larga:\n")

# 2. PROCESAMIENTO Y ANÁLISIS
#Convertimos a minúsculas temporalmente para asegurar que contamos tanto 'a' como 'A'
num_a = frase.lower().count("a")
# Calculamos la logitud total de la cadena
num_frase = len(frase)

# 3. SALIDA DE DATOS
print(f"Tu frase es:\n{frase}\nLa cantidad de letras a es: {num_a}\nY la frase tiene {num_frase} caracteres")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El truco de la unificación de datos)
# ==============================================================================
# Si hubieras hecho directamente 'frase.count("a")', python habría ignorado todas las letras "A"
# mayusculas, porque para el ordenador son dos caracteres totalmente distintos con códigos internos diferentes.
# 
# Al encadenar '.lower().count("a")', primero transformamos toda la frase a minúsculas 
# en la memoria de Python y luego cuentas las letras sobre esa base unificada. ¡Un truco
# vital para buscadores y filtros!
# 
# ⚠️ RECUERDA SOBRE LA FUNCIÓN len():
# La función 'len()' no cuenta solo letras. Cuenta "caracteres". Esto significa que los
# espacios en blanco, las comas, los puntos y los números también suman el total.
# ==============================================================================