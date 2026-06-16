# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL ESPEJO (SLICING INVERSO)
#   ----------------------------------------------------------------------
#   Enunciado: El slicing en Python guarda un truco legendario para dar la 
#   vuelta a una palabra sin usar bucles. Dada la palabra "radar", usa el 
#   slicing inverso para guardarla del revés en una nueva variable.
#   Imprime el resultado y comprueba si se lee igual (palíndromo).
# //======================================================================

# 1. VARIABLE ORIGINAL
palabra = "radar"
print(f"Palabra original: {palabra}")

# 2. SLICING INVERSO (El truco del espejo)
# Dejamos inicio y fin vacíos para tomar todo el texto, y ponemos paso -1 (marcha atrás)
palabra_invertida = palabra[::-1]
print(f"Palabra invertida: {palabra_invertida}")

# 3. COMPROBACIÓN DE PALÍNDROMO
# Comparamos si el derecho y el revés son exactamente iguales
es_palindromo = palabra_invertida == palabra
print(f"La palabra es palindromo: {es_palindromo}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Viajando al pasado con el paso -1)
# ==============================================================================
# En el ejercicio anterior aprendiste que el tercer parámetro '[::paso]' le dice a 
# Python cuántas casillas saltar hacia adelante. ¿Pero qué pasa si ese número es negativo?
#
# Al poner '[::-1]', le estás dando una orden muy loca a Python: "Quiero que recorras 
# todo el texto de principio a fin, pero con un paso de -1 (es decir, caminando hacia atrás)".
#
# 🔄 LA MAGIA DETRÁS DE LAS BAMBALINAS:
#   - Python empieza de manera automática en la última letra de la cadena.
#   - Va restando 1 a la posición en cada paso.
#   - Se detiene cuando llega a la primera letra del texto.
#
# Gracias a esto, consigues invertir cualquier cadena de texto en una sola línea de 
# código sin necesidad de usar bucles complejos. Es un truco famosísimo en Python y 
# la forma más rápida de resolver el clásico problema de detectar palíndromos (palabras 
# que se leen igual de izquierda a derecha que de derecha a izquierda como 'radar', 
# 'ana' o 'reconocer').
# ==============================================================================