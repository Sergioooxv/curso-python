# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 02: INPUT Y OUTPUT
# ==============================================================================
# //======================================================================
#   EJERCICIO 4: LA CUENTA DEL RESTAURANTE
#   ----------------------------------------------------------------------
#   Enunciado: Crea un programa para un grupo de amigos. Debe pedir:
#     1. El total de la cuenta del restaurante (puede tener decimales).
#     2. Cuántos amigos son para pagar (número entero).
#   Calcula cuánto debe pagar cada uno e imprime el resultado.
# //======================================================================


# 1. ENTRADA DE DATOS
# Usamos float() para la cuenta porque el dinero lleva céntimos (decimales).
# Usamos int() para los amigos porque no podemos dividir la cuenta entre 3.5 personas.
cuenta = float(input("¿Cúal es el total de la cuenta? "))
amigos = int(input("¿Cuantos amigos sois? "))

# 2. CALCULO DE LA DIVISIÓN
pago_individual = cuenta / amigos

# 3. SALIDA DE DATOS FORMATEADA
# ¡Ojo a la magia del :.2f al final de la variable!
print(f"Si sois {amigos} amigos y la cuenta es de {cuenta} euros debeis pagar cada uno {pago_individual:.2f}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Controlando los decimales flotantes)
# ==============================================================================
# Si dividies una cuenta de 50 euros entre 3 amigos, el resultado matemático es
# 16.666666666666668. Mostrar un número tan largo en un ticket de restaurante
# queda muy poco profesional.
# 
# Para solucionarlo, en Python usamos un modificador de formato dentro de las 
# llaves: 
# Traducción de '{pago_individual:.2f}':
#  - El signo de dos puntos (:) significa: "Oye Python, prepárate que te voy a dar un
#    formato"
#  - El punto (.) significa: "Nos enfocamso en los decimales"
#  - El número (2) significa: "Quiero exactamente DOS decimales"
#  - La letra (f) significa: "Trátalo como un Float (número decimal)"
# 
# Lo mejor de este método es que además hace el redondeo automático. Si el número fuera
# 16.666, lo redondea directamente a 16.76 Euros. ¡Una maravilla visual!
# ==============================================================================