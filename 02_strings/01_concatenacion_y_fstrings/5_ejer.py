# ==============================================================================
# //======================================================================
#   EJERCICIO 5: OPERACIONES DENTRO DE LLAVES
#   ----------------------------------------------------------------------
#   Enunciado: Las f-strings no solo muestran variables, ¡pueden ejecutar código!
#   Declara una variable llamada 'precio_unidad' con el valor 20. 
#   Pide al usuario cuántas unidades quiere comprar (entero).
#   Muestra el coste total realizando la multiplicación DIRECTAMENTE dentro 
#   de las llaves '{}' del print, sin crear variables intermedias.
# //======================================================================

# 1. CONFIGURACIÓN Y ENTRADA DE DATOS
precio_unidad = 20
unidades_comprar = int(input("¿Cuantas unidades quieres comprar?: "))

# 2. SALIDA CON EVALUACIÓN DIRECTA DENTRO DE LAS LLAVES
print(f"El precio total es de {precio_unidad * unidades_comprar} Euros")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Las llaves como miniprocesadores)
# ==============================================================================
# Hasta ahora, siempre habías visto que dentro de las llaves '{}' de una f-string
# poníamos el nombre de una variable. Pero la realidad es que en Python evalúa cualquier
# expresión válida que metas ahí dentro.
# 
# En la línea 17 no hemos creado ninguna variable intermedia como "precio_total'.
# Directamente le hemos dicho a Python: "Calcula esta multiplicación y estampa el 
# resultado aquí mismo".
# 
# 💡 VENTAJAS DE ESTA PRÁCTICA:
#   1. Ahorras memoria al no tener que crear variables que solo vas a usar una vez
#   2. Tu código queda más directo y compacto
# 
# ⚠️ UN CONSEJO DE BUEN PROGRAMADOR:
# Usa eso para operaciones sencillas (como una multiplicación, una suma o transformar un texto).
# si la operación matemática se vuelve muy larga o compleja, es mejor calcularla fuera en una
# variable separada para que tu código no se vuelva ilegible. ¡El equilibrio es la clave!
# ==============================================================================