# ==============================================================================
# //======================================================================
#   EJERCICIO 3: EL FRAGMENTO OCULTO
#   ----------------------------------------------------------------------
#   Enunciado: Tenemos la siguiente cadena de texto confidencial: "TOKEN_secret123_END".
#   Necesitamos aislar el secreto central. Usa slicing con los índices correctos 
#   para extraer solo el texto "secret123" (sin los guiones bajos) e imprímelo.
# //======================================================================

# 1. VARIABLE CON EL DATO CONFIDENCIAL
token =  "TOKEN_secret123_END"

# 2. EXTRACCIÓN DEL FRAGMENTO CENTRAL (Slicing con dos límites)
# Empezamos en la posición 6 (incluida) y frenamos antes de la 15 (la 15 se excluye)
secret = token[6:15]

# 3. SALIDA DE DATOS
print(f"El secreto aislado es: {secret}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Cortando el centro de un string)
# ==============================================================================
# Cuando necesitamos extraer un trozo que no está ni al principio ni al final de 
# un texto, estamos obligados a rellenar tanto el 'inicio' como el 'fin' dentro 
# de la fórmula '[inicio:fin]'.
#
# Vamos a contar minuciosamente las casillas de este token:
#   T[0] O[1] K[2] E[3] N[4] _[5] s[6] e[7] c[8] r[9] e[10] t[11] 1[12] 2[13] 3[14] _[15] E[16] N[17] D[18]
#
# 🎯 ANÁLISIS DE LOS LÍMITES:
#   - Inicio (6): La letra 's' ocupa la posición 6. Como el inicio SÍ se incluye, 
#     nuestro trozo empezará exactamente ahí.
#   - Fin (15): El número '3' está en la posición 14. Si hubiéramos puesto '[6:14]', 
#     Python se habría detenido ANTES del 14 y nos habría devuelto "secret12". Al poner 
#     un 15 (que corresponde al guion bajo), Python frena justo en la casilla anterior (la 14).
#     ¡Así nos aseguramos de capturar el '3' sin traernos el guion bajo!
# ==============================================================================