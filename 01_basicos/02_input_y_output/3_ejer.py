# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 02: INPUT Y OUTPUT
# ==============================================================================
# //======================================================================
#   EJERCICIO 3: FORMATEANDO REBOREDO (REPORTE DE TIENDA)
#   ----------------------------------------------------------------------
#   Enunciado: Crea un programa que imprima un ticket de compra usando un 
#   solo print(). Debes utilizar '\n' para los saltos de línea y '\t' para
#   alinear los precios como si fuera una tabla.
# //======================================================================

# 1. SALIDA DE DATOS FORMATEADA (Un solo print para todo el ticket)
# Usamos \n para saltar de línea y \t para crear columnas perfectas.
print(f"--- TICKET DE COMPRA --- \nProducto\tPrecio\nCafe Molido\t{2.50}\nTostada\t\t{3.20}\nTotal compra:\t{5.70}")
#print(f"--- TICKET DE COMPRA --- \nProducto\tPrecio\n" + "-"*24 + f"\nCafe Molido\t{2.50}€\nTostada\t\t{3.20}€\n" + "-"*24 + f"\nTotal compra:\t{5.70}€")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Las Secuencias de Escape)
# ==============================================================================
# En programación, cuando metemos una barra invertida '\' dentro de un texto, 
# le estamos diciendo a Python: "Oye, el siguiente carácter es especial, no
# lo imprimas tal cual". A esto se le llama 'Secuencias de Escape'. Las dos 
# formas más famosas son:
# 
# 🔹 '\n' (New Line / Salto de línea):
#    Equivale a pulsar la tecla 'Enter' en tu teclado. Todo lo que escribas
#    justo después de un \n aparecerá en la línea de abajo. Es ideal para no
#    tener que escribir veinte funciones print() seguidas.
# 
# 🔹 '\t' (Tab / Tabulador):
#    Mueve el texto hacia la derecha hasta la siguiente "columna invisible"
#    (Suele equivaler a 4 u 8 espacios). Fijate cómo en 'Tostada' Hemos puesto
#    '\t\t' para compensar que la palabra es más corta que 'Cafe Molido' y
#    Conseguir que los precios queden perfectamente alineados en vertical.
# 
# 💡 Truco PRO: ¿Viste el print comentado? contiene ('"-"*24') En Python
#     podemos multiplicar un texto por un número para que se repita 
#     esa cantidad de veces. ¡Súper útil para hacer líneas divisorias!
# ==============================================================================