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