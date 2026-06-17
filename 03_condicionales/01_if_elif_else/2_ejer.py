# ==============================================================================
# //======================================================================
#   EJERCICIO 2: CALCULADORA DE TARIFAS DE PARKING
#   ----------------------------------------------------------------------
#   Enunciado: Crea un script que calcule el importe total a pagar en un parking 
#   en función de las horas que ha estado un coche estacionado.
#   Pide las 'horas' por consola (entero) y aplica esta tarifa escalonada:
#
#   - Primera hora (horas == 1): Es gratis (0€).
#   - De 2 a 5 horas: Se cobra a 2€ cada hora. (Ej: 3 horas = 3 * 2 = 6€).
#   - De 6 a 10 horas: Se cobra a 1.5€ cada hora.
#   - Más de 10 horas: Tarifa plana de día completo fija de 20€.
#
#   Calcula el total e imprímelo formateado con dos decimales.
# //======================================================================

# 1. CAPTURA DE DATOS E INICIALIZACIÓN
horas = int(input("¿Cuantas horas lleva tu coche aparcado en el parking: "))
pago = 0.0

# 2. EVALUACIÓN ESCALONADA EN CASCADA
if horas <= 0:
    print(f"Error tus horas no pueden ser 0")
elif horas == 1:
    pago = 0.0
    print(f"Tienes suerte el pago es de: {pago} Euros")
elif horas <= 5:
    pago = horas * 2
    print(f"El coche lleva aparcado: {horas}h | El pago es: {pago} Euros")
elif horas <= 10:
    pago = horas *1.5
    print(f"El coche lleva aparcado: {horas}h | El pago es: {pago} Euros")    
else:
    pago = 20
    print(f"El coche lleva aparcado: {horas}h | El pago es: {pago} Euros")
    
# ===============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (La eficiencia de la evaluación en cascada)
# ===============================================================================
# Cuando programamos tarifas indexadas o escalonadas, es común caer en la tentación
# de escribir condiciones redundantes o excesivamente largas como esta:
#  'elif horas >= 2 and horas <= 5:'
# 
# Aunque matemáticamente es correcto, para el procesador es ineficiente para porque le
# obligas a realizar dos comprobaciones lógicas en lugar de una sola.
# 
# 🌊 EL EFECTO CASCADA ORDENADO:
# Aprovechando que python lee el código estrictamente de arriba a abajo, si ordenamos
# los filtros de menor a mayor de forma estricta, el propio flujo limpia el camino:
#   - Si el usaurio introduce un '4', el primer 'if' (4 <= 0) da False.
#   - Pasa al 'elif horas == 1' (4 == 1), que da false.
#   - Pasa al 'elif horas <=5'. Como 4 es menor o igual que 5, da True. Python ejecuta
#   ese bloque, calcula el pago, imprime el mensaje y ¡Rompe! el condicional saltando
#   directamente al final del script.
# 
# ¿Por qué no hace falta comprobar si las horas son mayores que 1 en ese tramo? Porque si
# hubieran sido 1 o menos, el programa se habría detenido en los pasos anteriores.
# 
# 🧮 TARIFA POR UNIDAD vs TARIFA PLANA:
# Observa la diferencia matemática en el código. En los tramos intermedios usamos una operación
# multiplicativa ('horas * tarifa') porque el precio depende directamente del tiempo. Sin embargo,
# en el 'else' final (para más de 10 horas), aplicamos una TARIFA PLANA. Da igual si el coche se queda
# 11 horas, 15 horas o 24 horas; el valor de la variable se congela en '20.0'.
# 
# Haber usado el modificador ':.2f' en los prints remata el ejericio garantizando que, aunque multipliquemos
# los floats como '1.5', la terminal siempre mostrará una estética limpia y profesional de dos decimales (ej: '7.50').
# ==============================================================================

