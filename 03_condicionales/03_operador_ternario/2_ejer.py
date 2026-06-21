# ==============================================================================
# //======================================================================
#   EJERCICIO 2: FILTRO DE ACCESO RÁPIDO
#   ----------------------------------------------------------------------
#   Enunciado: Pide al usuario su 'edad' (int) por consola. 
#   Usa el operador ternario en una sola línea para guardar en una variable 
#   llamada 'estado' el texto "Acceso Autorizado" si tiene 18 años o más, 
#   o "Acceso Denegado" si es menor.
#
#   Imprime el valor de la variable 'estado'.
# //======================================================================

# 1. CAPTURA DE DATOS
edad = int(input("¿Cual es tu edad?: "))

# 2. OPERADOR TERNARIO DIRECTO (Asignación limpia de String según condición)
estado = "Acceso autorizado" if edad >= 18 else "Acceso Denegado"

# 3. SALIDA POR CONSOLA
print(estado)

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (El principio de asignación limpia)
# ==============================================================================
# Este ejercicio muestra la verdadera esencia y el propósito para el que fue diseñado
# el operador ternario en Python: La asignación directa y limpia de estados.
# 
# 🧼 EVITANDO LAS VARIABLES VACÍAS (Código Junior vs Código Profesional):
# En un enfoque tradicional con 'if/else' de bloques, muchas vecies nos vemos obligados
# a declarar una variable vacía arriba o repetir la palabra clave de asignación:
#
#   if edad >= 18:
#       estado = "Acceso autorizado"
#   else:
#       estado = "Acceso Denegado"
# 
# Aunque funciona, ensucia visualmente el script para tareas tan simples. Con el operador
# ternario, la variable 'estado' nace y se rellena en un único movimiento atómico.
# 
# 🧐 ¿CÓMO LO LEE PYTHON INTUITIVAMENTE?
# La magia de la sintaxis de Python es que se lee casi como inglés fluido: 
# "estado es igual a 'Acceso Autorizado' Si edad es mayor o igual a 18, SI NO, es igual a
# 'Acceso Denegado'". Mantener esta estructura compacta mejora drásticamente la velocidad de lectura
# del código revisamos miles de líneas de software.
# ==============================================================================