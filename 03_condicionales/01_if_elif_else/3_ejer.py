# ==============================================================================
# //======================================================================
#   EJERCICIO 3: EL FILTRO DE CALIDAD DE CONTRASEÑAS
#   ----------------------------------------------------------------------
#   Enunciado: Vamos a programar el sistema de validación de contraseñas de un 
#   formulario de registro. Pide al usuario que introduzca una contraseña.
#
#   Debes evaluar su seguridad con las siguientes condiciones exclusivas:
#   1. Si tiene menos de 6 caracteres, imprime: "Seguridad: CRÍTICA. Demasiado corta".
#   2. Si tiene entre 6 y 10 caracteres, comprueba si termina en un número (usa 
#      el método '.isdigit()' con slicing en el último carácter). Si termina en 
#      número es "Seguridad: MEDIA", si no, es "Seguridad: BAJA".
#   3. Si tiene más de 10 caracteres, es "Seguridad: ALTA".
# //======================================================================

# 1. CAPTURA DE DATOS
contrasena = input("Escribe tu contraseña: ")

# 2. EVALUACIÓN DE SEGURIDAD EN CASCADA ANIDADA
if len(contrasena) < 6:
    # ESCENARIO 1: Menos de 6 caracteres
    print("Seguridad: CRÍTICA. Demasiado corta")
elif len(contrasena)  <= 10:
    # ESCENARIO 2: Entre 6 y 10 caracteres (ambos incluidos)
    # Extraemos el último carácter usando Slicing con índice negativo
    slice = contrasena[-1]
    
    # Anidamos un condicional para verificar la naturaleza del carácter
    if slice.isdigit():
        print("Seguridad: MEDIA")
    else:
        print("Seguridad: BAJA")
else:
    # ESCENARIO 3: Más de 10 caracteres (Cualquier otro caso restante)
    print("Seguridad: ALTA")
    
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Conectando bloques de conocimiento)
# ==============================================================================
# Este ejercicio es fantástico porque demuestra cómo la programación no consiste en
# aislar temas, sino en conectar herramientas. Para resolver un problema real de ciberseguridad,
# hemos fusionado condicionales con slicing y Métodos de String.
# 
# 🧩 EL VALOR DE LA VARIABLE ANIDADA:
# Analicemos qué ocurre en el tramo medio ('elif len(contrasena) <= 10'):
# si el usuario escribe "Python7", la longitud es 7. Pasa el primer 'if' y se mete
# en este 'elif'. Una vez dentro, ejecutamos:
#   'ultimo_caracter = contrasena[-1]'
# El indice '-1' es el ancla que apunta siempre al final de string (en este caso, el '7').
# Inmediatamente después, el método '.isdigit()' analiza ese carácter y devuelve 'True'
# porque es un digito numérico. Al dar True, se activa el 'print("Seguridad: MEDIA")'.
# 
# 🕵️‍♂️ OPTIMIZACIÓN DE RECURSOS (No pises tus propios límites):
# En tu primer borrador escribiste 'len(contrasena) <= 6' y luego 'len(contrasena) <= 10'.
# Si una contraseña mide 6 caracteres exactos, el enunciado dice que debe evaluarse si termina
# en número. Al usar '< 6' (estrictamente menor), nos aseguramos de que el 6 caiga correctamente en el segundo tramo.
# 
# Además, terminar el bloque con el 'else:' en lugar de un 'elif len(contrasena) >= 11' es una buena práctica
# de optimización. Como los tramos anteriores ya descartaron todo lo qeu mide de 0 a 10 caracteres, matemáticamente es imposible que el
# 'else' llegue algo que no sea mayor que 10. ¡Ahorramos código y cálculos innecesarios!
# ==============================================================================