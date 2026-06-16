# ==============================================================================
# //======================================================================
#   EJERCICIO 3: CALCULADORA DE IVA
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario el precio base de un producto (decimal).
#   Calcula el valor del IVA (21% en España) y muestra en consola:
#     1. Cuánto dinero es el IVA del producto.
#     2. El precio final total (Precio base + IVA).
# //======================================================================

# 1. ENTRADA DE DATOS (Admite decimales por si el precio incluye céntimos)
precio_base = float(input("Cual es el precio base de tu producto?: "))

# 2. CÁLCULO DE PORCENTAJES
# Para sacar el 21% de una cantidad, multiplicamos por 0.21
precio_iva = precio_base * 0.21
# ATAJO PRO: Multiplicar por 1.21 calcula el precio base + el 21% de golpe.
precio_total = precio_base * 1.21

# 3. SALIDA DE DATOS (Usando f-strings consaltos de línea y formateo de 2 decimales)
print(f"El precio del IVA es el siguiente: {precio_iva:.2f} Euros\nEl precio total del producto con IVA es: {precio_total:.2f} Euros")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Cómo calcular porcentajes como un Pro)
# ==============================================================================
# Cuando calculas el IVA o cualquier porcentaje de programación, no usamos la
# regla de tres clásica del colegio porque requiere demasiados pasos. Usamos
# Decimales.
#  - El 21% equivale a multiplicar por 0.21
#  - El 10% equivale a multiplicar por 0.10
#  - El 4% equivale a multiplicar por 0.04
# 
# Para obtener el precio total final, el camino largo habría sido:
#  precio_total = precio_base + precio_iva
# 
# Sin embargo, en la línea 18 hemos usado un truco matemático espectacular:
# multiplicar por 1.21. El '1' representa el 100% del precio original
# (El precio base) y el '.21' le suma el 21% del tirón. Ahorramos una 
# operación de suma al procesador y nuestro código queda mucho más 
# elegante. ¡Quédate con este truco de multiplicación!
# ==============================================================================