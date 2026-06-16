# ==============================================================================
# //======================================================================
#   EJERCICIO 3: EXAMEN DE CONDUCIR (OPERADOR AND)
#   ----------------------------------------------------------------------
#   Enunciado: Para obtener el carnet de conducir hay que aprobar dos fases.
#   Pide al usuario que responda 'True' o 'False' a estas dos preguntas:
#     1. ¿Aprobaste el examen teórico?
#     2. ¿Aprobaste el examen práctico?
#   El alumno solo obtiene el carnet si aprueba AMBOS. Usa el operador 'and' 
#   para calcular el resultado e imprímelo.
# //======================================================================

# 1. ENTRADA DE DATOS CON CONVERSIÓN BOOLEANA
# Convertimos el texto del usuario en un booleano real comparándolo directamente
# Si el usuario escribe "True", la expresión dira True. Si escribe otra cosa, dara False.#
teorico = input("¿Aprobaste el examen teórico? (ej: True/False): ") == "True"
practico = input("¿Aprobaste el examen práctico? (ej: True/False): ") == "True"

# 2. EVALUACIÓN LÓGICA (el Filtro exigente)
# El operador 'and' obliga a que ambas variables contengan el valor booleano True.
aprobado = teorico and practico

# 3. SALIDA DE DATOS
print(f"¿Puedes conducir? ¿Esta todo aprobado?: {aprobado}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La trampa del texto "False")
# ==============================================================================
# Este ejercicio esconde una de las trampas más peligrosas de Python.
# Si hubieras hecho simplemente: 'teorico = input(...)', la variable habría guardado
# un texto "False" (con comillas). para Python, cualquier texto que contenga letras
# se considera "lleno" y actúa como un True en las operaciones lógicas. ¡Tu programa
# habría aprobado a alumnos que escribieron False!
# 
# Al añadir el ' == "True"' al final del input, realizamos un truco de magia:
#   - Si el usuario escribe: True -> ¿Es "True" idéntico a "True"? Si -> Se guarda el booleano True
#   - Si el usuario escribe: False -> ¿Es "False" idéntico a "True"? No -> Se guarda el booleano False
# 
# 🧠 SOBRE EL OPERADOR AND:
# El operador 'and' es extremadamente estrícto. Imaginalo como un candado con dos llaves:
#   - True and True -> True (Tienes las dos llaves, el candado se abre).
#   - True and False -> False (Te falta una llave, el candado no se abre).
#   - False and False -> False (No tienes ninguna llave).
# ==============================================================================