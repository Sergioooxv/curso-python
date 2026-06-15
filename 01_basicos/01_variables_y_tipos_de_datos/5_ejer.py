# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 01: VARIABLES Y TIPOS DE DATOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL CONTADOR INCREMENTAL
#   ----------------------------------------------------------------------
#   Enunciado: Crea una variable 'contador' en 0. Increméntala en 1. Luego, 
#   súmale 5 más. Finalmente, multiplica su valor total por 2 e imprime 
#   el resultado (debe dar 12).
# //======================================================================

# 1 . INICIALIZACIÓN
contador = 0

# 2. OPERACIONES OPERACIÓN POR OPERACIÓN
contador = contador+1 # 0 + 1 = 1
contador = contador+5 # 1 + 5 = 6
contador = contador*2 # 6 * 2 = 12

# 3. MOSTRAR EL RESULTLADO FINAL
print("El resultado final del contador es:",contador)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El truco de los programadores flojos)
# ==============================================================================
# Lo hicimos arriba es totalmente correcto, pero los programadores siempre
# buscan escribir menos. En Python existe un "atajo" llamado Operadores de 
# Asignación Compuesta para modificar una variable usando su propio valor actual
# 
# Mira como se reescribiría nuestro código de forma profesional:
# contador = 0
# contador += 1 # Esto es EXACTAMENTE LO MISMO que: contador = contador + 1
# contador += 5 # Esto es EXACTAMENTE LO MISMO que: contador = contador + 5
# contador *= 2 # Esto es EXACTAMENTE LO MISMO que: contador = contador * 2
# 
# 💡 ¿Por qué se usa?
# Porque es más compacto y evita tener que escribir el nombre de la variable dos veces
# Sirve para sumar (+=), restar (-=), multiplicar (*=) y dividir (/=), ¡Pruebalo!
# ==============================================================================