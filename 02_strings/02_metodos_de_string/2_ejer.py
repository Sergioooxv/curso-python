# ==============================================================================
# //======================================================================
#   EJERCICIO 2: CENSOR DE PALABROTAS
#   ----------------------------------------------------------------------
#   Enunciado: En el chat de un videojuego queremos censurar la palabra "tonto".
#   Dada la siguiente frase, usa un método de string para cambiar esa palabra 
#   por asteriscos "****" e imprime la frase censurada resultante.
# //======================================================================

# 1. TEXTO DE ENTRADA
frase = "Oye tú, eres un tonto, no sabes jugar a este juego."
print(f"La frase original es:\n {frase}")

# 2. PROCESAMIENTO (Sustitución de la palabra prohibida)
# El método .replace() recibe: ("Lo que quiero buscar", "lo que quiero poner en su lugar")
frase = frase.replace("tonto","*****")
# 3. SALIDA DE DATOS
print(f"La frase corregida es:\n {frase}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El cirujano de los textos)
# ==============================================================================
# El método '.replace()' es una de las herramientas más potentes para transformar 
# información. Va recorriendo todo el texto de izquierda a derecha y, cada vez que 
# encuentra la palabra exacta que le has pedido (primer argumento), la recorta y pega
# en su lugar el nuevo texto (segundo argumento).
# 
# 🕵️‍♂️ DATOS IMPORTANTES QUE DEBES SABER:
#   1. Reemplaza TODAS las coincidencias: si la frase dijera "tonto" tres veces, el método
#      cambiaría las tres automáticamente de un solo golpe.
#   2. Es sensible a mayúsculas: si en el chat hubieran escrito "Tonto" con la 'T'
#      mayúscula, este código no lo habría detectado. 'En los próximos ejercicios
#      veremos cómo combinar métodos para solucionar este problema!
# ==============================================================================
