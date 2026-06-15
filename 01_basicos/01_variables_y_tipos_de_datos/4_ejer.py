# ==============================================================================
# 🗃️ BLOQUE 01: BÁSICOS | TEMA 01: VARIABLES Y TIPOS DE DATOS
# ==============================================================================
# //======================================================================
#   EJERCICIO 4: CONVERSIÓN DE ESTATURAS (TYPE CASTING)
#   ----------------------------------------------------------------------
#   Enunciado: Declara una variable 'estatura_float' con el valor 1.75. Crea 
#   una nueva variable 'estatura_int' que la convierta a entero usando int().
#   Imprime 'estatura_int' y observa qué pasa con los decimales.
# //======================================================================

# 1. DECLARACIÓN DE FLOAT (DECIMAL)
estatura_float = 1.75

# 2. CONVERSACIÓN DE TIPO (Type Casting)
# Usamos la función int() para forzar a que el dato se transforme en un entero.
estatura_int = int(estatura_float)

# 3. Mostrar Resultado
# En la consola vas a ver un: 1
print("Estatura convertida a entero:",estatura_int)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El misterio de los decimales perdidos)
# ==============================================================================
# Si pensabas que Python iba redondear 1.75 a 2... ¡Te ha engañado! ❌
# 
# Cuando usas la función 'int()' sobre un núemro decimal, Python NO REDONDEA.
# Lo que hace es un proceso llamado TRUNCAR. imagina que Python saca unas tijeras
# y corta el número justo por el punto decimal, tirando a la basura todo lo que
# haya a la derecha, sin importar si es .1 o .99. Por eso 1.75 se convierte a 1.
# 
# 💡 BONUS PRO: ¿Y si el alumno de verdad quiere redondear?
# Si en tu programa necesitas un redondeo matemático real (donde de .5 para arriba
# sube al siguietne número), no uses int(). En Python usamos la función 'round()':
# 
# estatura_redondeada = round(estatura_float) #Esto daria: 2
# ==============================================================================