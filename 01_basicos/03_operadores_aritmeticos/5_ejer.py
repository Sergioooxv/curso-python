# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL DESAFÍO DE LA PRIORIDAD MATEMÁTICA
#   ----------------------------------------------------------------------
#   Enunciado: Queremos calcular la nota media de un alumno que ha sacado
#   un 4.0 en el primer examen y un 8.0 en el segundo examen.
#   Si escribes: 'media = 4.0 + 8.0 / 2', Python dará un resultado incorrecto (8.0).
#   Arregla esa línea usando paréntesis para obligar a Python a calcular la 
#   nota media real (6.0) e imprime el resultado.
# //======================================================================

# 1. NOTAS DEL ALUMNO
nota1 = 4.0
nota2 = 8.0

# 2. CÁLCULO DE LA MEDIA CON PRIORIDAD CORRECTA
# Envolvemos la suma entre paréntesis para que se ejecute ANTES que la división.
media = (nota1+nota2)/2

# 3. SALIDA DE DATOS
print(f"Nota media: {media}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La jerarquía de operaciones o PEMDAS)
# ==============================================================================
# ¿Por qué fallaba el código sin los paréntesis?
# Si tu escribes: 'media = 4.0 + 8.0 / 2', Python sigue las reglas matemáticas
# estrictas. La división tiene más prioridad que la suma, así que Python hace esto:
#   1. Divide 8.0 / 2, lo cual da 4.0.
#   2. Le suma la nota1: 4.0 + 4.0 = 8.0
# ¡Y el alumno se encuentra con un 8 de media cuando ha suspendido un examen! ❌
# 
# Para hackear este orden, usamos los Paréntesis '()'. En Python, los paréntesis
# tienen el nivel de prioridad máximo. Al poner '(nota1+nota2)', obligamos a Python
# a realizar primero la suma (4.0 + 8.0 = 12.0) y luego ya divide el resultado
# entre 2, dando la media correcta de 6.0 ✔️
# 
# 💡 REGLA DE MEMORIA (PEMDAS):
# Cuando veas una línea con muchas opeeraciones juntas, recuerda que Python resuelve
# en este orden:
#  1. P -> Parentesis
#  2. E -> Exponentes (Potencias)
#  3. M / D -> Multiplicación y División
#  4. A / S -> Adición (Suma) y Sustracción (Resta)
# ==============================================================================