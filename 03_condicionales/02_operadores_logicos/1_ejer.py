# ==============================================================================
# 🗃️ BLOQUE 03: CONDICIONALES | TEMA 02: OPERADORES LÓGICOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: APROBACIÓN DE HIPOTECA BANCARIA
#   ----------------------------------------------------------------------
#   Enunciado: Un banco necesita automatizar el pre-análisis de hipotecas. 
#   Pide al usuario tres datos: 'ingresos_mensuales' (float), 'tiene_deudas' 
#   (booleano/texto convertido) y 'antiguedad_laboral_meses' (int).
#
#   Reglas para conceder la hipoteca (Debe cumplir TODAS):
#   1. Los ingresos mensuales deben ser estrictamente superiores a 2500€.
#   2. NO debe tener deudas pendientes (usa el operador 'not').
#   3. La antigüedad laboral en su empresa debe ser mayor o igual a 12 meses.
#
#   Escribe una única condición combinada usando 'and' y 'not'.
# //======================================================================

# 1. CAPTURA Y SANITIZACIÓN DE DATOS
ingresos_mensuales = float(input("¿Cuáles son tus ingresos mensuales?: "))

# Convertimos la respuesta de texto directamente a un booleano puro evaluando su string
respuesta_deudas = input("¿Tienes deudas pendientes? (Si/No): ")
tiene_deudas = respuesta_deudas.lower() == "si"

antiguedad_laboral = int(input("¿Cuántos meses tienes de antiguedad laboral?: "))

# 2. EVALUACIÓN CON UNA ÚNICA CONDICIÓN COMBINADA
# Usamos 'and' para obligar al cumplimiento de todo y 'not' para invertir el booleano #
if ingresos_mensuales > 2500 and not tiene_deudas and antiguedad_laboral >=12:
    print(f"Estudio viable: Cumples con todos los requisitos financieros. Hipotecia concedida")
else:
    print(f"Estudio denegado: No cumples con los criterios mínimos de estabilidad")
    

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Evaluación perezosa y Flags Booleanos)
# ==============================================================================
# Combinar condiciones en una única línea es una práctica excelente para simplificar 
# la estructura del código, pero exige entender cómo interactúan los tipos de datos.
# 
# 🏷️ TEXTO VS BOOLEANOS (El error común del input):
# Recuerda que 'input()' lee texto. Si intentas hacer 'input(...) == True', Python
# comparará el string '"Si"' con el booleano 'True', dando como resultado 'False'.
# La manera correcta es procesar el texto con '.lower()' primero y comprobar si es igual a '"si"'.
# esa comparación sí genera un 'True' o 'False' booleano real que guardamos en la variable 
# 'tiene_deudas'.
# 
# 🔄 EL TRABAJO DEL OPERADOR 'not':
# La variable 'tiene_deudas' guarda un 'True' si el usuario tiene deudas. Sin embargo el banco exige 
# que NO las tenga. Al escribir:
#   'not tiene_deudas'
# Si la variable es 'False' (no deudas), el 'not' la transforma en 'True', permitiendo que esa parte
# del condicional apruebe el examen. Se lee exactamente igual que el lenguaje humano: "Si los ingresos
# son mayores a 2500 Y NO tienes deudas...
# 
# 🦥 PERFORMANCE: EVALUACIÓN PEREZOSA (Short-Circuit Evaluation)
# Una gran vientaja de encadenar con 'and' es la eficiencia. Python evalúa de izquierda a derecha.
# Si un usuario introduce que gana 1000 Euros, la primera condición da 'False'. Al ser un 'and', Python
# es "perezoso" y detiene la lectura inmediatamente; no llegará a mirar si tiene deudas ni su antiguedad 
# porque sabe que el resultado final a a ser 'False' pase lo que pase. ¡Ahorro puro de procesamiento!#