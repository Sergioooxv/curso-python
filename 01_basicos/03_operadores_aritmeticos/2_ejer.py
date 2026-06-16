# ==============================================================================
# //======================================================================
#   EJERCICIO 2: EL CONVERSOR DE MONEDA
#   ----------------------------------------------------------------------
#   Enunciado: Crea un conversor de Euros (€) a Dólares ($). 
#   1. Pide al usuario la cantidad de euros que quiere cambiar (puede tener decimales).
#   2. Declara una variable fija con el tipo de cambio (ej: 1 euro = 1.09 dolares).
#   3. Calcula cuántos dólares equivalen e imprime el resultado con 2 decimales.
# //======================================================================

# 1. ENTRADA DE DATOS (usamos float porque el dinero tiene céntimos)
cantidad = float(input("¿Qué cantidad de Euros quieres cambiar?: "))

# 2. CONFIGURACIÓN Y CÁLCULO
tipo_cambio = 1.09
dolares = cantidad * tipo_cambio

# 3. SALIDA DE DATOS FORMATEADA
# Aplicamos el formato de 2 decimales (.2f) para que parezca dinero real.
print(f"Tienes {cantidad} Euros, equivalen a un total de: {dolares:.2f} Dolares en el mercado actual")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El peligro de los números mágicos)
# ==============================================================================
# En este ejercicio hemos creado una variable llamada 'tipo_cambio = 1.09'.
# Podríamos haber hecho directamente: 'dolares = euros * 1.09'. Funciona igual, si.
# Pero meter números sueltos en mitad de las operaciones se considera MALA PRÁCTICA
# en programación (se llama "números mágicos" porque aparecen ahí sin explicación).
# 
# Al meter el 1.09 dentro de una variable con un nombre claro ('tipo_cambio'):
#  1. El código se lee e interpreta muchísimo mejor (es autodocumentado).
#  2. Si mañana el dolar sube o baja, solo tienes que cambiar el valor en la línea 15,
#     en lugar de tener que buscar el número 1.09 oculto en tu código.
# 
# ¡Escribe siempre código pensado en el mantenimiento futuro!
# ==============================================================================