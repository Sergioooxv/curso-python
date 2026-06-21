# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL CALCULADOR DE RECARGOS POR PASARELA de PAGO
#   ----------------------------------------------------------------------
#   Enunciado: Una tienda online cobra una comisión fija por gestión de 2.50€ 
#   si el cliente decide pagar con "PAYPAL". Si paga con "TARJETA", la comisión 
#   es de 0.0€.
#
#   Pide al usuario el 'importe_articulo' (float) y el 'metodo_pago' (texto). 
#   Usa el operador ternario en una sola línea para calcular la variable 'comision', 
#   asegurándote de sanitizar el método de pago con '.upper()'.
#   Muestra en la terminal el desglose con el total final formateado.
# //======================================================================

# 1. CAPTURA Y SANITIZACIÓN EN LA ENTRADA
importe_articulo = float(input("¿Cuál es el importe del articulo?: "))
metodo_pago = input("Cuál es el metodo de pago (Paypal o Tarjeta): ").upper()

# 2. OPERADOR TERNARIO (Sanitización al vuelo y asignación float pura)
# Evaluamos pasando el método a mayúsculas directamente en la condición
comision = "Comision de 2.50" if metodo_pago == "paypal" else "comision de 0.0."

# 3. CÁLCULO DEL TOTAL
total_pedido = importe_articulo + comision

# 4. SALIDA DE DATOS FORMATEADA
print(f"\n🛒 Desglose del pedido:")
print(f"   - Artículo:  {importe_articulo:.2f}€")
print(f"   - Comisión:  {comision:.2f}€")
print(f"   ------------------------")
print(f"💳 Total final: {total_pedido:.2f}€")

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Sanitización integrada en el Ternario)
# ==============================================================================
# Una de las ventajas más brutales de Python es que nos permite meter métodos de objetos (como '.upper()')
# directamente dentro de la condición del operador ternario Esto significa que podemos transformar el texto
# introducido por el usuario a vuelo, evaluar la condición y asignar el precio correcto en una sola línea limpia 
# de código.
# 
# 🕵️‍♂️ EL FLUJO DE COMPARACIÓN EXACTA.
# Si el usuario introduce "paypal" (en minusculas) y aplicamos 'metodod_pago.upper()' Python evalúa intermaente
# '"PAYPAL" == "PAYPAL"', lo cual da True y asigna el float 2.50. Si introduce "tarjeta", se evalúa '"TARJETA" == "PAYPAL"'
# da False y aplica 0.0.
# 
# Al mantener la variable 'comision' como un tipo de dato numérico puro (float), garantiamos que el programa
# prueba realiar operaciones matemáticas posteriores, como calcular el 'total_pedido'. Mezclar strings explicativos dentreo
# de variables de cálculo intermedio es un error de arquitectura clásico que debemos enseñar a evitar desde el primer día.
# ==============================================================================