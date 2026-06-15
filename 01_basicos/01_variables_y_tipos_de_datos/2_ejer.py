# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 01: VARIABLES Y TIPOS DE DATOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 2: EL CAMBIAZO DE VARIABLES
#   ----------------------------------------------------------------------
#   Enunciado: Declara una variable llamada 'juguete_favorito' con el texto 
#   "Pelota". En la siguiente línea, cambia su valor a "Consola de videojuegos".
#   Imprime la variable antes y después del cambio para ver cómo se actualiza.
# //======================================================================

# 1. ASIGNACIÓN INICIAL
# Creamos la variable y le asignamos su primer valor en memoria.
juguete_favorito = "Pelota"

# Imprimimos el valor actual. En la consola verias: Pelota
print(juguete_favorito)

# 2. REASIGNACIÓN DE VARIABLE (El cambiazo)
# En Python, las variables puede cambiar de valor a lo largo del programa.
# Al usar el signo "=" otra vez con el mismo nombre, NO creamos una variable nueva;
# Simplemente le decimos a la variable "juguete_favorito" que apunte el nuevo dato.#
juguete_favorito = "Cosola de videojuegos"

# Imprimimos el nuevo valor. En la consola verás: Consola de videojuegos
print(juguete_favorito)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (¿Qué pasa detrás de escena?)
# ==============================================================================
# Cuando hiciste el "cambiazo", el texto "Pelota" no se transformó en la consola.
# lo que pasó en la Memoria RAM de tu ordenador fue esto:
# 
# 1. Primero, se creó el texto "Pelota" en un rincón de la memoria y le pegamos
# la etiqueta "juego_favorito".
# 
# 2. Al reasignar, se creó el texto "Consola de videojuegos" en otro rincón
# diferente, y despegamos la etiqueta "juego_favorito" de "Pelota" para pegarsela
# al nuevo texto.
# 
# 3. Como "Pelota" se quedó sin ninguna etiqueta, Python la detecta como basura
# y la elimina de la memoria automáticamente para no gastar RAM.
# ¡A esto se le llama Dinamismo y Gestión de Memoria en Python!
# ==============================================================================