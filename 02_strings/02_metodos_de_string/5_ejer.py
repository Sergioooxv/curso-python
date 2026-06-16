# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL DETECTIVE DE BUSCADOR
#   ----------------------------------------------------------------------
#   Enunciado: Tenemos la base de datos de un periódico con la siguiente noticia:
#      "El precio del bitcoin bate un nuevo récord histórico este mes."
#   Usa un método para averiguar en qué posición exacta (índice) empieza la 
#   palabra "bitcoin". Imprime ese índice numérico por pantalla.
# //======================================================================

# 1. VARIABLE INICIAL (Base de datos del periódico)
noticia = "El precio del bitcoin bate un nuevo récord histórico este mes."

# 2. BÚSQUEDA DE ÍNDICE
# .find() rastrea la cadena y nos devuelve la posición exacta de la primera letra
index_bitcoin = noticia.find("bitcoin")

# 3. SALIDA DE DATOS
print(f"La palabra 'bitcoin' empieza en el indice número: {index_bitcoin}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Cómo cuenta Python las posiciones)
# ==============================================================================
# El método '.find()' actúa como el buscador de tu navegador (Ctrl + F). Empieza
# a leer el texto desde el principo y, en cuanto encuentra la coincidencia exacta,
# se para y te dice el número de la casilla donde empieza (la 'b' de bitcoin).
# 
# 🧠 REGLAS DE ORO DE LOS ÍNDICES EN PYTHON:
#   1. Se empieza a contar desde el 0: La primera letra 'E' de la frase está en 
#      el índice 0. 
#   2. Los espacios cuentan: Cada espacio en blanco ocupa una posición real en la
#      memoria
# 
# 🕵️‍♂️ ¿QUÉ PASA SI LA PALABRA NO EXISTE?
# Si intentas buscar una palabra que no está en el texto, por ejemplo: 'noticia.find("ethereum")'
# el método '.find()' no romperá el programa; te devolverá un '-1'.
# Ese '-1' es el código universal en programación para decir: "Busqué por todas partes,
# pero o encontré nada". ¡Es una herramienta ideal para poner filtros antes de operar!
# ==============================================================================