# ==============================================================================
# //======================================================================
#   EJERCICIO 4: SALTOS DE RANA (EL TERCER PARÁMETRO)
#   ----------------------------------------------------------------------
#   Enunciado: Dada la cadena de texto "A1B2C3D4E5", queremos deshacernos de 
#   los números y quedarnos solo con las letras ("ABCDE").
#   Aplica la fórmula del slicing usando el tercer parámetro (paso) para 
#   ir saltando los números e imprime el resultado limpito.
# //======================================================================

# 1. VARIABLE CON EL TEXTO MEZCLADO
texto = "A1B2C3D4E5"

# 2. FILTRADO CON PASO DE CORTE (Slicing con saltos)
# Dejar vacíos los dos primeros huecos le dice a Python: "recorre todo el texto"
# El ':2' del final activa el salto doble (va saltando de 2 en 2 caracteres)
letras = texto[::2]
#letras = texto[0:10:2] #Esto hace exactamente lo mismo

# 3. SALIDA DE DATOS
print(f"Texto original mezclado: {texto}")
print(f"Solo letras (filtrado):  {letras}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El secreto del tercer parámetro)
# ==============================================================================
# Hasta ahora siempre habías usado la fórmula del slicing con un único dos puntos: 
# '[inicio:fin]'. Pero la realidad es que la sintaxis completa de Python permite 
# meter hasta tres parámetros: '[inicio:fin:paso]'.
#
# El 'paso' es el ritmo al que avanza el corte. Por defecto es 1 (lee todas las letras).
#
# 🕵️‍♂️ MIRA CÓMO TRABAJA EL PASO 2 EN NUESTRO TEXTO:
#   Posición [0] -> 'A'  (Se la queda)
#   Posición [1] -> '1'  (La salta)
#   Posición [2] -> 'B'  (Se la queda)
#   Posición [3] -> '2'  (La salta)
#   Posición [4] -> 'C'  (Se la queda)... y así hasta el final.
#
# Al escribir 'texto[::2]', omitimos el inicio y el fin para que Python escanee la 
# cinta entera, pero obligamos a la "rana" a saltar de dos en dos. ¡Es un filtro 
# ultra potente que te ahorra crear bucles complejos para limpiar patrones repetitivos!
# ==============================================================================