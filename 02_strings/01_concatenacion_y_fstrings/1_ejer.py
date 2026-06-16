# ==============================================================================
# 🗃️ BLOQUE 02: STRINGS | TEMA 01: CONCATENACIÓN Y F-STRINGS
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: GENERADOR DE NOMBRES COMPLETOS
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario su nombre por teclado y luego su apellido.
#   Crea una tercera variable llamada 'nombre_completo' que use la 
#   concatenación clásica (+) para unirlos, asegurándote de dejar un espacio 
#   en blanco entre ambos. Muestra el resultado por consola.
# //======================================================================

# 1. ENTRADA DE DATOS
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

# 2. CONCATENACIÓN CLÁSICA (Sumando el espacio en blanco intermedio)
nombre_completo = nombre +" "+ apellido

# 3. SALIDA DE DATOS
print(f"Tu nombre completo es: {nombre_completo}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La suma de textos y sus reglas)
# ==============================================================================
# En python, el signo más '+' es polifocético. Si le das dos números, los suma.
# Pero si le das dso textos (strings), realiza una operación llamada CONCATENACIón,
# que consiste simplemente en "pegar" el segundo texto justo al final del primero.
# 
# ⚠️ LA REGLA ESTRICTA DEL OPERADOR '+':
# Para poder concatenear con '+', ambos lados de la operación TIENEN que ser texto.
# Si intentas hacer esto:
#   edad = 25
#   mensaje = "Mi edad es: " + edad # ❌ ¡ESTO DA ERROR! (TypeError)
# 
# Python se quejará porque no sabe cómo "sumar" letras con números. Si necesitas 
# meter números o booleanos dentro de un texto usando la concatenación clásica,
# tendrías que transformarlos a texto a la fuerza usando la funcion str():
#   mensaje = "Mi edad es: + str(edad) # ✔️ Esto sí funciona
# 
# Por suerte, para ahorrarnos este dolor de cabeza y no tener que estar usando str()
# a cada rato, en los siguientes ejercicios explotaremos a fondo las f-strings.
# ==============================================================================