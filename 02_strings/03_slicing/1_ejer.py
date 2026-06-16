# ==============================================================================
# 🗃️ BLOQUE 02: STRINGS | TEMA 03: SLICING
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: EXTRACCIÓN DE CARACTERES SUELTOS
#   ----------------------------------------------------------------------
#   Enunciado: Dada la variable palabra = "PROGRAMACION":
#     1. Extrae e imprime la primera letra usando un índice positivo.
#     2. Extrae e imprime la última letra usando un índice negativo.
# //======================================================================

# 1. VARIABLE BASE
palabra = "PROGRAMACION"

# 2. EXTRACCIÓN MEDIANTE ÍNDICES
primera_letra = palabra[0] # El índice 0 siempre es el primer elemento
segunda_letra = palabra[-1] # El índice -1 siempre da la vuelta y pilla el último

print(f"La primera letra de {palabra} es: {primera_letra}")
print(f"La segunda eltra de {palabra} es: {segunda_letra}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El doble mapa de coordenadas)
# ==============================================================================
# Para entender cómo Python lee las letras de un String, imagina que cada carácter
# está guardado dentro de una casilla numerada. Python te regala dos formas de medir:
# 
# ⬅️ DE IZQUIERDA A DERECHA (Índices positivos):
# Empezamos a contar SIEMPRE desde el 0.
#   [0] = 'P', [1] = 'R', [2] = 'O', [3] = 'G'... y así hasta el final.
# Por eso 'palabra[0]' nos devuelve la 'P'.
# 
# ➡️ DE DERECHA A IZQUIERDA (Índices negativos):
# Cuando queremos empezar por el final, usamos números negativos. Pero ¡OJO!, aquí
# no existe el '-0' (matemáticamente no tiene sentido), así que empezamos desde el -1.
#   [-1]='N', [-2]='O', [-3]='I', [-4]='C'....
# Por eso 'palabra[-1]' nos da la 'N' de forma directa.
# 
# 💡 TRUCO PRO: Los índices negativos son salvavidas reales. Imagina que estás
# leyendo un texto gigante que ha escrito un usuario y no tienes ni idea de cuántas
# letras mide. Gracias a [-1], siempre podrás aislar el último carácter al instante
# sin necesidad de calcular la logitud del texto.
# ==============================================================================