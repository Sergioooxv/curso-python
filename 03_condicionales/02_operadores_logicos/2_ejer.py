# ==============================================================================
# //======================================================================
#   EJERCICIO 2: BECA UNIVERSITARIA (COMBINANDO AND Y OR)
#   ----------------------------------------------------------------------
#   Enunciado: Una universidad otorga becas si el alumno cumple el Criterio A
#   O si cumple el Criterio B. Pide por consola: 'nota_media' (float) y 
#   'distancia_km' (int) desde su casa a la facultad.
#
#   - Criterio A: Tener una 'nota_media' mayor o igual a 9.0 (independientemente de la distancia).
#   - Criterio B: Tener una 'nota_media' mayor o igual a 7.0 Y vivir a más de 50 km ('distancia_km > 50').
#
#   ¡Ojo! Para agrupar condiciones y que el 'or' no rompa la prioridad matemática, 
#   debes utilizar paréntesis '()' para aislar el bloque del Criterio B.
# //======================================================================

# 1. CAPTURA DE DATOS
nota_media = float(input("¿Cual es tu nota media?: "))
distancia_km = int(input("Indica los kilometros donde se encuentra tu casa: "))

# 2. EVALUACIÓN DE LÓGICA COMBINADA EN UNA SOLA LÍNEA
# Usamos paréntesis para encapsular por completo el bloque del Criterio B
if nota_media >= 9.0 or (nota_media >= 7.0 and distancia_km > 50):
    print("BECA CONCEDIDA: Cumples con los requisitos")
else:
    print("BECA DENEGADA: no cumples con los requisitos")
    
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Jerarquía y Precedencia Lógica)
# ==============================================================================
# En el tema anterior vimos cómo resolver problemas usando 'if' y 'elif' en cascada.
# Pero un buen programador debe saber cuándo compactar la lógica en una sola sentencia
# para hacer el código más limpio y directo. Aquí es donde se cruzan los cables del 'and' y el 'or'
# 
# ⚖️ LA JERARQUÍA REGINA: 'and' VA ANTES QUE 'or'
# En programación existe la "Precedencia de Operadores". Igual que en matemáticas los detalles
# multiplicativos se resuelven antes que las sumas, en Python el operador 'and' tiene más
# peso y se ejecuta ANTES que el operador 'or'.
# 
# Si hubieras escrito la línea sin paréntesis:
# 'if nota_media >= 9.0 or nota_media >= 7.0 and distancia_km > 50:'
# Python, por su cuenta, habría agrupado el 'and' del final. En este ejercicio concreto 
# habría funcionado por coincidencia matemática, pero mezclar ambos operadores a la ligera
# es una fábrica de "bugs" invisibles en proyectos grandes.
# 
# 🛡️ EL PODER DE LOS PARÉNTESIS '()'
# Al poner '(nota_media >= 7.0 and distancia_km > 50)', obligamos a Python a romper su 
# orden natural. Ahora el motor evalúa el código como dos grandes paquetes independientes:
#   - Paquete Izquierdo (Criterio A): ¿Tiene un excelente >= 9.0?
#   - Paquete Derecho (Criterio B): ¿Tiene al menos un 7.0 Y ADEMÁS vive lejos?
#
# Como están unidos por un 'or' central, basta con que uno de los dos paquetes se 
# evalúe como 'True' para que el alumno reciba su beca. Acostumbrarse a encapsular 
# con paréntesis hace que tus algoritmos sean predecibles, seguros y fáciles de leer.
# ==============================================================================