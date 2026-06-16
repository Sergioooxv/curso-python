# ==============================================================================
# //======================================================================
#   EJERCICIO 2: DESACTIVANDO CÓDIGO (DEBUGGING)
#   ----------------------------------------------------------------------
#   Enunciado: Este programa da un error al ejecutarse porque la variable 
#   'numero_secreto' intenta sumar un texto. 
#   En lugar de borrar la línea rota, "coméntala" (#) para desactivarla 
#   y escribe una nueva línea abajo que sume el número correctamente como entero.
# //======================================================================

# 👇 ¡REPARA EL CÓDIGO USANDO COMENTARIOS AQUÍ ABAJO! 👇

base = 10
numero_secreto = base + "5"  # ❌ Esta línea rompe el programa

print(f"El número secreto es: {numero_secreto}")