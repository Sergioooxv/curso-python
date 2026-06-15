# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 02: INPUT Y OUTPUT
# ==============================================================================
# //======================================================================
#   EJERCICIO 5: IMPRIMIENDO EN LÍNEA
#   ----------------------------------------------------------------------
#   Enunciado: Por defecto, cada print() escribe en una línea diferente. 
#   Crea tres funciones print() seguidas que muestren las palabras "Cargando", 
#   "datos" y "completado...", pero usando el parámetro 'end' para forzar 
#   a que todo se muestre en una sola línea separado por espacios.
# //======================================================================

# 1. SALIDA DE DATOS EN LA MISMA LÍNEA
# Usamos end="" para romper el comportamiento nativo de saltar de línea.
print("Cargando ", end="")
print("datos ", end="")

# Al último print le quitamos el end para que, al finalizar el programa,
# la terminal del sistema opeartio salte de línea limpiamente.
print("Completado...")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (¿Qué es el parámetro invisible 'end'?)
# ==============================================================================
# Cuanto tú escribes un print() normal, como este:
# print("Hola")
#
# Python en verdad esta ejecutando esto en secreto:
# print("Hola", end="\n")
# 
# Por defecto, todos los print() traen oculto un parametro llamado 'end' que vale \n
# (El salto de línea que vimos en el ejercicio 3). Por eso cada print() escribe abajo.
# 
# Al escribir tu manualmente 'end=""' (comillas vacias) o 'end=" "', estás hackeando
# el comportamiento nativo. Le estás diciendo a Python: "Oye, cuando termines de pintar
# este texto, NO saltes de la línea: en su lugar, no pongas nada (o un espacio) y quedate
# ahí esperando al siguiente print()".
# 
# 💡 ¿Para qué se usa en el mundo real?
# Se usa muchisimo para barras de carga en la consola (como los porcentajes [10%....20%..])
# para imprimir elementos de listas uno al lado del otro, o para crear interfaces visuales
# dinamicas en la terminal.
# ==============================================================================