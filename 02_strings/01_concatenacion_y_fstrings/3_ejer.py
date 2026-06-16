# ==============================================================================
# //======================================================================
#   EJERCICIO 3: F-STRING EXPRESS
#   ----------------------------------------------------------------------
#   Enunciado: Un compañero de trabajo antiguo ha dejado este código escrito 
#   usando concatenaciones con '+' y convirtiendo números a texto con str():
#      'mensaje = "El producto " + producto + " cuesta " + str(precio) + " euros."'
#   Refactoriza (mejora) esa línea usando una f-string moderna para que sea 
#   mucho más legible y limpia.
# //======================================================================

# 1. VARIABLES INICIALES
producto = "Teclado Mécanico"
cuesta = 25

# 2. REFACTORIZACIÓN CON F-STRING (código moderno y limpio)
# Ponemos la 'f' delante de las comillas y nos olvidamos de los '+' y los str()
mensaje = f"El producto: {producto} tiene un coste de {cuesta} Euros"

# 3. SALIDA DE DATOS
print(mensaje)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Por qué las f-strings ganaron la guerra)
# ==============================================================================
# El código antiguo que dejó tu compañero funciona, si, pero tiene tres problemas:
#   1. Es propenso a errores: si te olvidas de poner 'str(precio)', el programa explota.
#   2. Es dificil de leer: está lleno de comillas que se abren y se cierran y signos '+'.
#   3. Es más lento: a nivel interno, Python sufre más uniendo piezas sueltas.
# 
# Las f-strings (Formatted String Literals) llegaron para solucionar esto. Al poner
# la 'f' mágica antes de las comillas, le dices a Python: "Oye, procesa este texto de golpe,
# y cuando veas unas llaves '{}', mete ahí dentro lo que valga esa variable".
# 
# Da igual si la variable es un texto, un número entero, un decimal o un booleano;
# Python se encarga de transformarlo todo a texto de forma transparente y segura.
# ¡Es la forma estándar en la que escribirás texto dinámico en tu día a día!
# ==============================================================================