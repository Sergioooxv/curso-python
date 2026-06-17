# ==============================================================================
# //======================================================================
#   EJERCICIO 2: EL MÉTODO CLÁSICO (.FORMAT)
#   ----------------------------------------------------------------------
#   Enunciado: Aunque las f-strings son mejores, el método '.format()' se 
#   sigue usando muchísimo. Dadas las variables: 'ciudad = "Madrid"' y 'temp = 24'.
#   Construye la frase: "La temperatura en Madrid es de 24 grados." usando 
#   EXCLUSIVAMENTE el método '.format()' con sus llaves '{}' vacías.
# //======================================================================

# 1. DECLARACIÓN DE VARIABLES
ciudad = "Madrid"
temp = 24

# 2. FORMATEO CLÁSICO CON EL MÉTODO .format()
# Las llaves vacías '{}' actúan como buzones esperando recibir datos en orden.
mensaje = "La temperatura en {} es de {} grados.".format(ciudad, temp)

# 3. SALIDA DE DATOs
print(mensaje)

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El estándar de la era intermedia)
# ==============================================================================
# El método '.format()' fue la herramienta estrella de Python 3 durante muchos años
# y supuso una mejora gigante respecto al viejo operador '%'.
# 
# 📬 ¿CÓMO FUNCIONA EL REPARTO EN LAS LLAVES?
# Cuando pones llaves vacías '{}' dentro de un string, Python las trata como "anclas"
# o buzones vacíos. Al ejecutar '.format(ciudad, temp)', Python hace un reparto de
# izquierda a derecha por estricto orden de llegada:
#  - La primera variable ('ciudad') vuela hacia las primeras llaves '{}'.
#  - La segunda variable ('temp') vuela hacia las segundas llaves '{}'.
# 
# 💡 TRUCO EXTRA (Para mentes curiosas):
# Aunque en este ejercicio las llaves están vacías. '.format()' permite poner números
# dentro para cambiar el orden de las variables. Por ejemplo:
#  '"{1} es una ciudad con {0} grados".format(temp, ciudad)'
# A poner '{1}', le dices a Python que pille el elemento en la posición 1 (ciudad)
# y la ponga al principio. ¡Es un sistema muy flexible que sentó las bases de las f-strings!
# ==============================================================================