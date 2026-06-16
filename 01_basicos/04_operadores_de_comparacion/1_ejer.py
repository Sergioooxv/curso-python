# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 04: OPERADORES RELACIONALES Y LÓGICOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: CONTROL DE ACCESO
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario que introduzca su edad (entero).
#   Crea una variable booleana llamada 'puede_entrar' que compare si la 
#   edad es mayor o igual a 18. Muestra el resultado por consola.
# //======================================================================

# 1. ENTRADA DE DATOS
edad = int(input("¿Cúal es tu edad?: "))

# 2. COMPARACIÓN DIRECTA (¡Sin usar 'if0'!)
# La expresion 'edad >= 18' se evalúa en secreto. Si se cumple, se transforma
# directamente en 'True' y se guarda en la variable. Si no, se guarda 'false
puede_entrar = edad >= 18

# 2.1 COMPARACIÓN USANDO IF 
# Esto es exactamente igual que la forma simplificada, más adelante lo veremos
# más a fondo.
#puede_entrar = False
#if edad >= 18:
#    pueden_entrar = True

# 3. SALIDA DE DATOS
print(f"¿Puedes entrar con tu edad?: {puede_entrar}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La potencia de las expresiones booleanas)
# ==============================================================================
# Cuando estamos empezando, todos tendemos a pensar que para saber si alguien es
# mayor de edad necesitamos un condicional 'if'. ¡Pero Python es mucho más listo!
# 
# Al escribir la linea 18: 'puede_entrar = edad  >= 18'
# Python no lee texto, lee una pregunta matemática. Imagina que el usuario pone un
# '20': 
#  ¿Es 20 mayor o igual que 18? -> La respuesta es Sí (True).
# 
# Entonces Python machaca toda esa operación y la sustituye por el valor booleano
# puro, haciendo que en secreto la línea quede así: 'pueden_entra = True'.
# 
# Hacerlo de esta manera tiene dos ventajas brutales:
#  1. Ahorra líneas de código y variables inicializadas a ciegas
#  2. Aprendemos a usar los operadores de comparación como generadores automáticos 
# de respuestas.
# ==============================================================================
