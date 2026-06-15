# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 02: INPUT Y OUTPUT
# ==============================================================================
# //======================================================================
#   EJERCICIO 2: LA MÁQUINA DEL TIEMPO
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario su edad por teclado. Calcula cuántos años
#   tendrá dentro de exactamente 10 años y muéstralo en la consola.
#   ⚠️ OJO: Recuerda transformar el dato del input para poder hacer matemáticas.
# //======================================================================

# 1. ENTRADA DE DATOS DE CONVERSION (Anidación de funciones)
# Pasamos el input() dentro del int(). Python ejecuta primero el input(),
# recibe el texto del usuario (ej: "25") y luego int() lo convierte en número (25).
edad = int(input("¿Que edad tienes? "))
anos = 10 # NO HACE FALTA GUARDAR LOS AÑOS EN VARIABLE

# 2. CALCULO MATEMÁTICO
# Como 'edad' ya es un número entero, podemos sumarle otra variable númerica sin problemas.
edad_anos = edad + anos
# edad_anos = edad + 10

# 3. SALIDA DE DATOS
print(f"Dentro de 10 años tendras: {edad_anos} años")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (La regla de oro del input)
# ==============================================================================
# Grábate esto a fuego: Todo lo que entra por la función 'input()' es TEXTO (str)
# Aunque el usuario escriba un número como el 25, para Python eso son dos caracteres
# de texto: "2" y "5".
# 
# Si intentas hacer esto sin el int():
#  edad = input("¿Quké edad tienes? ") # Imagina que pones 25
#  print(edad +10)
# 
# Python te escupirá un error de tipo (TypeError) diciendo que no puede concatenar
# un texto ("25") con un número (10). ¡NO sabe si quieres sumar o pegar las letras!
# 
# Al escribir 'int(input(...))' resuelves el problema transofmrando las letras en 
# un número real atnes de gaurdarlo en la variable. ¡Esencial para cualquier calculo!
# ==============================================================================