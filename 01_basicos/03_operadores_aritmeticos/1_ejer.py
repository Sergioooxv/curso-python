# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 03: OPERADORES ARITMÉTICOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: LA CALCULADORA BÁSICA
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario que introduzca dos números enteros por teclado.
#   Calcula y muestra en la consola el resultado de:
#     1. La Suma.
#     2. La Resta.
#     3. La Multiplicación.
#     4. La División Real.
# //======================================================================

# 1. ENTRADA DE DATOS (Forzamos a enteros 'int' como pide el enunciado)
num1 = int(input("Dime tu primer número: "))
num2 = int(input("Dime tu segundo número: "))

# 2. OPERACIONES MATEMÁTICAS
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# 3. SALIDA DE DATOS (Usando f-strings como estructura limpia con saltos de línea)
print(f"Resultado las operaciones:\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El comportamiento de la división)
# ==============================================================================
# Si ejecutas este programa y pones los números '10' y '2', veras que los 
# resultados de la suma, resta y multiplicación salen como números enteros secos:
#   Suma: 12
#   Resta: 8
#   Multiplicacion: 20
# 
# Sin embargo, la división te devolverá: 'División: 5.0' (con punto decimal).
# 
# 💡 REGLA DE ORO EN PYTHON:
# El operador de división real '/' SIEMPRE, sin excepción, devuelve un dato de
# tipo float (decimal), aunque el resultado sea exacto y hayamos usado números
# enteros. Python hace esto para evitar pérdidas de información (por ejemplo,
# si divides 5/2, necesitas ese .5). Sin en algún momento necesitas borrar los
# decimales de una división, ¡Tendrás que usar el operador de división entera
# '//' que veremos más adelante.
# ==============================================================================