# ==============================================================================
# //======================================================================
#   EJERCICIO 4: LA TARJETA DE PRESENTACIÓN
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario tres datos: su ocupación (texto), sus años de 
#   experiencia (entero) y si está disponible para trabajar (True/False).
#   Construye una f-string que actúe como tarjeta de presentación imprimiendo 
#    todo en una sola frase coherente.
# //======================================================================

# 1. ENTRADA DE DATOS (Guardamos cada tipo de dato de forma correcta)
ocupacion = input("¿Cual es tu ocupacion?: ")
anos = int(input("¿Cuantos años tienes?: "))
# Nota: Lo dejamos como texto directo ya que el objetivo es solo imprimirlo en la tarjeta
disponible = input("¿Estas disponible para trabajar? (True/False): ")

# 2. CONSTRUCCIÓN DE LA TARJETA Y SALIDA
# Las f-strings nos permiten fusionar textos, enteros y lo que sea en una frase perfecta.
print(f"Tu ocupación es {ocupacion}, además tienes {anos} y estas disponible para trabajar?: {disponible}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La f-string como pegamento universal)
# ==============================================================================
# Imagina tener que construir este mensaje usando la concatenación clásica con el signo '+':
# 'print("Profesión: "+ ocupacion + " | Experiencia: " + str(experiencia) + ....)'
# Habría sido una pesadilla llena de conversiones a str() y espacios en blanco perdidos
# 
# Las f-strings actúan como un pegamento universal en Python. No importa que 'ocupación'
# sea texto, 'experiencia' sea un número entero, o 'disponible' sea la respuesta del usuario.
# Al estar encerrados deentro de las llaves '{}', Python se encarga de formatear cada pieza
# de forma automática para que encaje perfectamente dentro de la cadena de texto final.
# ¡Es limpio, rápido de escribir y súper profesional!
# ==============================================================================