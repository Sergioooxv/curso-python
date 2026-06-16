# ==============================================================================
# //======================================================================
#   EJERCICIO 4: REPARTO DE CARAMELOS (OPERADORES SECRETOS)
#   ----------------------------------------------------------------------
#   Enunciado: Imagina que tienes 15 caramelos y quieres repartirlos entre
#   4 niños en partes exactamente iguales (sin romper caramelos). 
#   Crea un programa que calcule y muestre usando los operadores '//' y '%':
#     1. Cuántos caramelos enteros recibe cada niño.
#     2. Cuántos caramelos sobran en la bolsa y te quedas tú.
# //======================================================================

# 1. VARIABLES INICIALES
# (Evitamos la 'ñ' en el nombre de la variable por buenas prácticas de programación)
caramelos = 15
ninios = 4

# 2. OPERACIONES CON OPERADORES "SECRETOS"
# La división entera (//) nos da el resultado sin sacar decimales (el cociente).
caramelos_repartidos = caramelos // ninios
#El módulo (%) nos da lo que sobra de la división entera (el Resto o Residuo).
caramelos_quedas = caramelos % ninios

# 3. SALIDA DE DATOS
print(f"Cada niño recibe: {caramelos_repartidos}\nEn bolsa sobra: {caramelos_quedas}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Volviendo a la división de primaria)
# ==============================================================================
# Para entender estos dos operadores, solo hay que recordar cómo dividimos en 
# la pizarra del colegio antes de que nos enseñaran los decimales:
# 
#        15  |_4__  <- Niños
#       -12    3    <- Cociente (Resultado entero que da el operador '//')
#       ----
#        [3]        <- Resto o Residuo (Lo que sobra y nos da el operador '%')
#
# 🔹 Operador '//' (División entera): Te dice cuántas partes completas le tocan 
#     a cada uno de los niños
# 🔹 Operador '%' (Módulo): Te dice cuánto se ha quedado sin poder repartir.
# 
# 💡 ¿Por qué el Módulo (%) es el operador más valioso en programación?
# Aunque ahora te parezca un juego de niños, el signo '%' se usa constantemente
# para: 
#  1. Saber si un número es PAR o IMPAR: Si haces 'numero%2' y el resto da 0, es par
#  si da 1, es impar.
#  2. Controlar ciclos: Hacer que un evento ocurra cada 'X' veces dentro de un bucle.
#  3. Convertir unidades: Pasar minutos totales a horas y minutos sobrantes.
# ==============================================================================