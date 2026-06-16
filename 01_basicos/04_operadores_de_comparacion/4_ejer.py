# ==============================================================================
# //======================================================================
#   EJERCICIO 4: DÍA DE DESCUENTO (OPERADOR OR)
#   ----------------------------------------------------------------------
#   Enunciado: Una tienda ofrece descuentos si el cliente cumple al menos uno
#   de estos requisitos: ser estudiante O ser jubilado.
#   Pregunta al usuario si es estudiante (si/no) y si es jubilado (si/no).
#   Usa el operador 'or' para determinar si se le aplica el descuento.
# //======================================================================

# 1. ENTRADA DE DATOS Y CONVERSOR BOOLEANO
# Comparamos contra "Si" con mayúscula para transformar la respeusta en True o False.
estudiante = input("¿Eres estudiante? (Si/No): ") == "Si"
jubilado = input("¿Eres jubilado? (Si/No): ") == "Si"

# 2. EVALUACIÓN LÓGICA (El filtro permisivo)
# Al usar 'or', basta con que una de las dos variables sea True para que todo sea True#
estudiante_or_jubilado = estudiante or jubilado

# 3. SALIDA DE DATOS
print(f"Tienes acceso a los descuentos de la tienda: {estudiante_or_jubilado}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El operador bonachón 'or')
# ==============================================================================
# A diferencia del operador 'and' (que era súper estricto y te pedia cumplir todo),
# el operador 'or' es el compañero más permisivo de Python
# 
# Imagina al operador 'or' como un guardia de seguridad buena gente que te deja pasar
# si cumples AL MENOS una de las condiciones:
#   - True or False -> True (¿Eres estudiante aunque no seas Jubilado? ¡Pasa, tienes descuento!)
#   - False or True -> True (¿Eres jubilado aunque ya no esutdies? ¡Pasa también!)
#   - True or True -> True (¿Cumples ambas? ¡Doble combo, por supuesto que entras!)
#   - False or False -> False (Único caso en el que falla: no eres ni lo uno ni lo otro).
# 
# ⚠️ NOTA DE DISEÑO (Mayúsculas y Minúsculas):
# Al haber escrito '== "Si"', si el usuario teclea "si" con la 's' minúscula, Python
# diría que es Falso porque busca la coincidenia exacta. No te preocupes, en las 
# próximas lecciones aprenderemos a controlar esto para que tu programa acepte "si",
# "SI" o "Si" sin romperse. ¡Paso a Paso!
# ==============================================================================