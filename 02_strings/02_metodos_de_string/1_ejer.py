# ==============================================================================
# 🗃️ BLOQUE 02: STRINGS | TEMA 02: MÉTODOS DE STRING
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: NORMALIZADOR DE NOMBRES
#   ----------------------------------------------------------------------
#   Enunciado: Un usuario se ha registrado en tu web y ha escrito su nombre 
#   lleno de espacios y mal formateado: "   sErGiO raMoS   ".
#   Crea un programa que limpie los espacios de los extremos y lo transforme 
#   para que quede en formato de nombre propio limpio: "Sergio Ramos".
# //======================================================================

# 1. ESTADO INICIAL (Dato sucio de entrada)
nombre = "   sErGiO raMoS   "
print(f"Texto original (sucio): {nombre}")

# 2. CADENA DE MONTAJE (Encadenamiento de métodos)
# .strip() elimina los espacios de los extremos y .title() pone formato de nombre propio.
nombre = nombre.strip().title()

# 3. ESTADO FINAL (Dato normalizado)
print(f"Texto corregido (limpio): {nombre}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La cadena de montaje de Python)
# ==============================================================================
# En este ejercicio has aprendido dos conceptos que valen millones en el mundo real:
# 
# 1. ENCADENAR MÉTODOS:
# En python puedes poner un punto '.' detrás de otro para aplicar varias acciones
# seguidas en una sola línea. Al hacer 'nombre.strip().title()', Python primero
# limpia los espacios y, al texto resultante, le aplica las mayúsculas. ¡Súper eficiente!
# 
# 2. LOS STRINGS SON INMUTABLES:
# Si solo hicieras 'nombre.strip().title()' sin poner el 'nombre =' delante, la variable
# original NO habría cambiado. Los métodos de string nunca modifican el texto original;
# calculan una copia limpia y te la devuelven. Por eso es obligatorio reasignar la
# variable ('nombre = ....') si quieres guardar los cambios para siempre.
# ==============================================================================