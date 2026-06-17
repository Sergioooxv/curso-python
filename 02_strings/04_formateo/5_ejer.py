# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL TICKET DE COMPRA (ALINEACIÓN)
#   ----------------------------------------------------------------------
#   Enunciado: Queremos pintar un miniticket en la consola donde el nombre del 
#   producto ocupe exactamente 15 caracteres (alineado a la izquierda) y el 
#   precio ocupe 6 caracteres (alineado a la derecha).
#   Prueba a usar los modificadores de alineación '<' y '>' dentro de una 
#   f-string para maquetar estas dos líneas y que queden perfectamente en columna:
#      Producto: "Pan", Precio: 1.25
#      Producto: "Manzanas", Precio: 3.40
# //======================================================================

# 1. DECLARACIÓN DE VARIABLES (Datos de la compra)
producto1, precio1 = "Pan", 1.25
producto2, precio2 = "Manzanas", 3.40

# 2. IMPRESIÓN DEL TICKET MAQUETADO
print("=======TICKET DE COMPRA=======")
# {variable:<15}  -> Reserva un bloque de 15 caracteres alineado a la izquierda
# {variable:>6.2f} -> Reserva un bloque de 6 caracteres alineado a la derecha con 2 decimales
print(f"{producto1:<15} | {precio1:<6.2f}")
print(f"{producto2:<15} | {precio2:<6.2f}")
print(f"==============================")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Maquetación de tablas en consola)
# ==============================================================================
# Cuando imprimes texto normal, las palabras cortas y largas descuadrán las columnas
# para solucionar esto, las f-strings de Python incluyen "diseñadores de bloques".
# 
# 📐 TRABAJANDO CON BLOQUES DE ANCHO FIJO:
# - '{prod1:<15}': Le dice a Python que cree una "caja" invisible que mida exactamente
# 15 caracteres de ancho y pegue el texto a la izquierda ('<'). si el producto
# es "pan", Python rellena los 12 espacios restantes con huecos vaciós.
# - '{precio1:>6.2f}': Hace un combo triple. El ':' activa el formato, el '>'
# alinea el precio a la DERECHA, el '6' obliga a que la caja mida 6 caracteres de ancho
# y el '.2f' congela los dos decimales obligatorios.
# 
# Gracias a que ambos productos se metenen cajas del mismo tamaño (15 para texto y 6 para precio),
# la barra de separación '|' y los simbolos de '€' quedan perfectamente en columna, imitando el ticket
# en una caja registradora real.
# ==============================================================================