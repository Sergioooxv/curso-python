# ==============================================================================
# //======================================================================
#   EJERCICIO 5: CAZANDO MENTIRAS (OPERADOR NOT)
#   ----------------------------------------------------------------------
#   Enunciado: Declara una variable llamada 'tengo_hambre' y asígnale el valor True.
#   Imprime el valor de esa variable, pero aplicándole el operador 'not' por delante.
#   Observa el cambio en la consola y explica qué ha pasado.
# //======================================================================

# 1. DECLARACIÓN DE LA VARIABLE BOOLEANA
tengo_hambre = True

# 2. SALIDA DE DATOS DEMOSTRANDO EL INVERSOR LÓGICO
print(f"Valor original de la variable: {tengo_hambre}")
print(f"Valor aplicando el operador NOT: {not tengo_hambre}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El operador rebelde 'not')
# ==============================================================================
# El operdor 'not' es el más sencillo de los operadores lógicos porque no compara
# dos cosas entre sí; simplemente se aplica sobre una sola variable o expresión y
# le da la vuelta por completo al valor. Es el "inversor" de Python.
# 
# Su tabla de verdad es un espejo:
#   - not True -> Se convierte en False
#   - not False -> Se convierte en True
# 
# 💡 ¿Para qué se usa esto en el desarrollo real?
# Se utiliza muchisimo para crear "interruptores" (o flags) en el código.
# Imagina que estás programando un videojuego o una aplicación:
#   - Si tienes una variable 'juego_pausado = False', escribir 'not juego_pausado'
#     te permite activar de olpe el estado de pausa.
#   - Si tienes 'usuario_conectado = True', puedes usar 'if not usuario_conectado'
#     para saber de forma directa cuándo mostrar el formulario de registro.
# 
# Es una herramienta clave para negar condiciones de una forma muy natural y legible.
# ==============================================================================