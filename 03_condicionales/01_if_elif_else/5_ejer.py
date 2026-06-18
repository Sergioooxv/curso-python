# ==============================================================================
# //======================================================================
#   EJERCICIO 5: CONTROL DE STOCK E INVENTARIO INTELIGENTE
#   ----------------------------------------------------------------------
#   Enunciado: En un almacén logístico queremos automatizar las alertas de compra. 
#   Pide por consola el 'stock_actual' (entero) de un producto.
#
#   Aplica la siguiente lógica corporativa:
#   - Si el stock es menor que 0: Imprime un error grave "Stock negativo detectado. Revisar sistema".
#   - Si el stock está entre 0 y 5 (incluidos): Imprime "Alerta: Stock crítico. Realizar pedido URGENTE".
#   - Si el stock está entre 6 y 20: Imprime "Estado: Stock moderado. Monitorizar ventas".
#   - Si el stock es mayor que 20: Comprueba si supera las 100 unidades. Si es así, 
#     imprime "Estado: Sobre-stock en almacén. Detener producción". Si está entre 
#     21 y 100, imprime "Estado: Stock óptimo".
# //======================================================================

# 1. CAPTURA DE DATOS
stock_actual = int(input("¿Cual es el stock actual del producto?: "))

# 2. EVALUACIÓN LOGÍSTICA ESCALONADA Y ANIDADA
if stock_actual < 0:
    print(f"ERROR GRAVE: Stock negativo detectado. Revisar Sistema.")
elif stock_actual <= 5:
    print(f"Alerta: Stock crítico. Realizar pedido URGENTE")
elif stock_actual <= 20:
    print(f"Estado: Stock moderado. Monitorizar ventas") 
else:
    # Bloque para stock superior a 20 unidades
    # Anidamos un sub-condicional para evaluar el volumen del excedente
    if stock_actual > 100:
        print(f"Sobre-stock en almacén. Detener producción")
    else:
        # Si no supera 100, por descarte está entre 21 y 100
        print(f"Estado: stock óptimo")
        
        
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Estructuras complejas y optimización por descarte)
# ==============================================================================
# Este ejercicio representa fielmente cómo se programa la lógica de negocio en sistemas ERP o
# almacenes automatizados (como los de Amazon o grandes cadenas logísticas).
# 
# ✂️ SIMPLIFICACIÓN Y "CÓDIGO MUERTO":
# Si en tu propuesta inicial escribiste: 'elif stock_actual >= 21 and stock_actual <= 100:'
# Esto es correcto en los resultados; pero redundante para la máquina. ¿Por qué?
# 1. Ya estás dentro del ramal 'else' (que sustituye a tu 'elif stock_actual > 20'), por
#   lo que Python ya sabe con certeza absoluta que el stock es mayor que 20. Comprobar
#   si es '>=21' es repetir una pregunta que ya tiene respuesta.
# 2. Si la primera pregunta interna ('if stock_actual > 100') da false, significa que el 
#   número NO es mayor que 100 (es decir, es 100 o menos).
# 
# Al aplicar un 'else:' interno directo, limpiamos el código de operaciones matemáticas
# repetitivas. El programa se vuelve más rápido, consume menos recursos y es mucho más
# fácil de leer para otros desarrolladores.
# 
# 🛡️ DISEÑO DEFENSIVO:
# Al colocar el filtro de menores de cero al principio del todo ('if stock_actual < 0'), 
# aplicamos una técnica de desarrollo llamada "Retorno Temprano" (Early Return) o filtro 
# defensivo. nos quitamos de encima los errores del sistema inmediatamente, asegurando
# que todo el código que viene detrás trabaje únicamente con datos reales y positivos.
# ==============================================================================