# ==============================================================================
# 🗃️ BLOQUE 03: CONDICIONALES | TEMA 03: OPERADOR TERNARIO
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: COSTES DE ENVÍO EN UN E-COMMERCE
#   ----------------------------------------------------------------------
#   Enunciado: Un comercio online ofrece envío gratuito si la compra supera 
#   los 50€. Si no la supera, el envío cuesta 4.90€.
#
#   Pide al usuario el 'total_carrito' (float). A continuación, calcula el 
#   'coste_envio' utilizando una ÚNICA LÍNEA con el operador ternario.
#   Muestra por pantalla el coste del envío y el total absoluto.
# //======================================================================

# 1. CAPTURA DE DATOS
total_carrito = float(input("¿Cuánto es el total de tu carrito?: "))

# 2. OPERADOR TERNARIO ESTRICTO (Asignación pura de valor numérico)
# Estructura: valor_si_true if condicion else valor_si_false
coste_envio = 0.0 if total_carrito > 50.0 else 4.90

# 3. CÁLCULO DEL TOTAL ABSOLUTO
total_factura = total_carrito + coste_envio

# 4. SALIDA DE DATOS FORMATEADA
print(f"\n📦 Coste de envío: {coste_envio:.2f}€ " + ("(¡Gratis por superar 50€!)" if coste_envio == 0 else ""))
print(f"💳 Total absoluto a pagar: {total_factura:.2f}€")

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (La pureza del dato en el Operador Ternario)
# ==============================================================================
# El operador ternario es una herramienta fantástica de "Syntactic Sugar" (azúcar sintáctico)
# diseñada para hacer el código más compacto. Sin embargo, para usarlo como un profesional, debemos
# seguir la regla de la "Pureza del Dato".
# 
# 🧠 VALORES PUROS vs CADENAS MEZCLADAS:
# Si intentamos almacenar mensajes de texto junto con operaciones matemáticas en la misma línea dle ternario.
# Esto rompe la arquitectura del script. Si guardas texto en 'coste_envio', luego no puedes usar esa variable
# para hacer operaciones matemáticas (como sumar el coste del envío al carrito).
# 
# La norma de oro es: El ternario calcula y guarda el DATO BRUTO (en este caso, el float '0.0' o '4.90'). La 
# maquetación, los textos y lso adornos con f-strings se gestionan delegándolos en los 'print()' de salida.
# 
# 💡 TRUCO AVANZADO DE REGALO:
# Fíjate en el primer 'print()'. Hemos emtido un operador ternario directamente INSIDE del f-string:
#   '("¡Gratis...!)" if coste_envio == 0 else "")'.
# Pythn permite incrustar ternarios dentro de las llaves de impresión para mostrar u ocultar texto de forma
# dinámica. ¡Esto reduce líneas de código y mantiene la terminal con una estética impecable!
# ==============================================================================