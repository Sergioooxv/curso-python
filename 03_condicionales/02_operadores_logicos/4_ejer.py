# ==============================================================================
# //======================================================================
#   EJERCICIO 4: LIQUIDACIÓN DE DESCUENTOS BLACK FRIDAY
#   ----------------------------------------------------------------------
#   Enunciado: Un e-commerce aplica un 30% de descuento si se da alguna de 
#   estas condiciones corporativas:
#   - Que el cliente sea "VIP" Y realice la compra cualquier día de la semana.
#   - Que la compra se realice en el día "VIERNES" (sea VIP o no).
#
#   Pide al usuario la 'moneda_gasto' (float), si es 'es_vip' (si/no) y el 
#   'dia_semana' (texto). Si tiene descuento, calcula el nuevo precio. Si no, 
#   mantiene el original. Aplica 'and', 'or' y métodos de string.
# //======================================================================

moneda_gasto = float(input("Dime el precio del producto sin descuento: "))
es_vip = input("¿Eres VIP del comercio (Si/No): ").lower() == "si"
dia_semana = input("¿Qué dia de la semana realizaste la compra?: ").lower()

if es_vip or dia_semana == "viernes":
    precio_final = moneda_gasto * 0.70
    ahorro = moneda_gasto * 0.30
    print(f"¡TIENES DESCUENTO! Se aplica un 30% de Black Friday.")
    print(f"Precio final: {precio_final:.2f}€ (Has ahorrado {ahorro:.2f}€")
else:
    print(f"NO TIENES DESCUENTO. El precio final se mantiene en {moneda_gasto:.2f}€")
    
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Ecuaciones financieras y unificación lógica)
# ==============================================================================
# En las plataformas de comercio electrónico, reducir las líneas de código unificando
# criterios comerciales ayuda a que el mantenimiento del software sea mucho más sencillo.
# 
# 🎯 ANÁLISIS DE LA CONDICIÓN UNIFICADA:
# El enunciado nos pedía evaluar dos casos:
#   - Caso 1: Cliente VIP y cualquier día.
#   - Caso 2: Cualquier cliente y día viernes.
# 
# Si lo analizamos con perspectiva, la condición 'Cualquier día' y 'Cualquier cliente' 
# anula la necesidad de usar un 'and'. Basta con escribir 'if es_vip or dia_semana == "viernes":'. 
# Si el cliente es VIP, el 'or' se da por satisfecho (True) y le da el descuento da igual 
# el día. Si el día es "viernes", el 'or' también se cumple da igual si es VIP o no. ¡La 
# lógica se simplifica al máximo!
#
# 🧮 EL ERROR MATEMÁTICO DEL DESCUENTO:
# Un fallo muy común al empezar a programar es confundir el valor del descuento con el 
# precio final. Si multiplicas 'precio * 0.30', estás obteniendo la cantidad que vas 
# a quitar (el ahorro). Para mostrar lo que el cliente realmente va a pagar en la caja, 
# debes restar esa cantidad al total, o multiplicar directamente por '0.70' (que representa 
# el 70% restante del valor del producto). Vigilar los cálculos financieros es clave para 
# evitar desastres contables en producción.
# ==============================================================================