# ==============================================================================
# //======================================================================
#   EJERCICIO 2: LA ALERTA DEL SISTEMA
#   ----------------------------------------------------------------------
#   Enunciado: Queremos pintar un banner de advertencia en la consola que 
#   llame mucho la atención del usuario. Usa la multiplicación de strings (*) 
#   para imprimir una línea con 30 asteriscos, luego el mensaje "¡ERROR CRÍTICO!" 
#   y cierra con otra línea de 30 asteriscos. Todo usando el menor código posible.
# //======================================================================

# 1. SALIDA DE DATOS MAQUETADA (Form limpia y legible para el alumno)
# print("*"*30 + "\nERROR CRITICO\n" +"*"*30) #Versión simplificada en una sola linea con f-string
print("*"*30)
print("¡ERROR CRÍTICA!")
print("*"*30)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Multiplicar letras... ¿cómo es posible?)
# ==============================================================================
# En la vida real, si multiplicas "Hola" x 3 en una calculadora, te daría un error.
# Pero en programación, Python es capaz de interpretar que multiplicar un texto por
# un número entero significa: "repite este texto tantas veces como te pido"
# 
# Al escribir '"*"*30', le estamos ahorrando el procesador y a nosotros dedos tener
# que teclear treinta asteriscos a mano. Es una herramienta genial para crear líneas
# divisorias, barras de carga o marcos visuales en aplicaciones de consola.
# 
# 🚀 TRUCO DE EXPERTO (Reduciendo a una sola línea):
# Si quieres llevar este ejercicio al siguiente nivel de optimización, puedes meter 
# todo el banner dentro de un compacto 'print' usando saltos de linea (\n) y 
# concatenación los bloques así:
# 
# print("*"*30 + "\nERROR CRITICO\n" +"*"*30) 
# 
# De exactamente el mismo resultado en la terminal, pero usando una única línea de código.
# ==============================================================================