# ==============================================================================
# //======================================================================
#   EJERCICIO 2: RECORTANDO EL PREFIJO
#   ----------------------------------------------------------------------
#   Enunciado: En tu tienda online, los productos tecnológicos empiezan siempre 
#   por el prefijo "TEC-". Dado el siguiente código de barras en texto: "TEC-84729"
#   Usa slicing para extraer ÚNICAMENTE las tres letras del prefijo (sin el guion) 
#   y muéstralo por pantalla.
# //======================================================================

# 1. VARIABLE DE ENTRADA
codigo = "TEC-84729"

# 2. REBANADO EN DOS PARTES (Slicing Quirurgico)
# Extraemos el prefijo: desde el principio hasta el índice anterior al 3 (0,1,2)
codigo_letras = codigo[:3]
# Extraemos la parte numérica: desde el índice 4 hasta el final de la cadena
codigo_numeros = codigo[4:]

# 3. SALIDA DE DATOS
print(f"Letras extraídas: {codigo_letras}")
print(f"Números extraídos: {codigo_numeros}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Cómo partir un texto en trozos limpios)
# ==============================================================================
# El slicing en Python se basa en la fórmula '[inicio:fin]'. Para entender cómo funciona
# tenemos que dibujar el mapa de posiciones (índices) de nuestro texto:
#
#    T   E   C   -   8   4   7   2   9
#   [0] [1] [2] [3] [4] [5] [6] [7] [8]
#
# 🪓 CORTE 1: AISLANDO LAS LETRAS ('codigo[:3]')
#  Cuando dejas el hueco de 'inicio' vacío, Python asume automáticamente que quieres
#  empezar desde la posición [0]. Al poner un 3 en el 'fin', le estás diciendo:
#  "Avanza y corta justo ANTES de llegar al 3". Por lo tanto, se queda con las casillas
#  0,1 y 2, que corresponden a "TEC". ¡El guion se queda fuera!
# 
# 🪓 CORTE 2: AISLANDO LOS NÚMEROS ('codigo[4:]')
#  En este caso, hacemos lo contrario. Le decimos a Python que empiece a cortar de forma
#  fija en la posición [4] (donde empieza el número 8). Al dejar el hueco del 'fin'
#  completamente vacío, Python entiende que no tieen que frenar y que debe llevarse todo el 
#  texto restante hasta el final de la cadena.
# 
# 💡 CONCLUSIÓN:
#  Omitir el inicio '[:X]' sirve para agarrar los primeros carateres, y omitir el fin '[X:]'
#  sirve para agarrar los últimos. 'Una técnica que evita tener que calcular cuánto mide el texto!
# ==============================================================================