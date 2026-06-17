# ==============================================================================
# //======================================================================
#   EJERCICIO 3: CONTROL DE DECIMALES
#   --------------------------------================================------
#   Enunciado: Estás calculando el precio de una porción de tarta y la división 
#   te devuelve un número con demasiados decimales: 'precio = 4.3333333333'.
#   Muestra por pantalla el precio final usando una f-string, pero aplicando 
#   el formateo necesario para que SOLO se muestren 2 decimales y el símbolo '€'.
# //======================================================================

# 1. VARIABLE CON EXCESO DE DECIMALES (Dato en bruto)
precio = 4.3333333333

# 2. SALIDA DE DATOS CON FORMATEO DE PRECISIÓN
# Usamos el modificador :.2f dentro de las llaves para recortar los decimales
print(f"El precio sin formatear: {precio}€ | El precio formateado {precio:.2f}€")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El código secreto de los decimales)
# ==============================================================================
# Cuando metes una variable numérica dentro de las llaves de una f-string, Python
# te permite añadir configuraciones extra si pones dos puntos ':'  justo detrás del
# nombre de la variable.
# 
# Vamos a destripar que significa exactamente '{precio:.2f}:'
#   - El ':' le dice a Python: "¡Atento!, que ahora viene una orden de formato".
#   - El '.' le dice a Python: "Esta orden va a afectar a los decimales (los que van tras el punto)".
#   - El '2' Le dice a Python: "Quiero que me dejes exactamente DOS digitos decimales".
#   - La 'f' Le dice a Python: "Trata este número como un Float (número con decimales)".
# 
# 🧠 DATO IMPORTANTISIMO SOBRE EL REDONDEO:
# Python no se limita a "cortar" el número de golpe; aplica la regla del redondeo matemático
# estándar. Si nuestro precio fuera '4.338', al poner ':.2f' Python mostraría por pantalla
# '4.34' porque el 8 redondea hacia arriba. ¡Hace el trabajo sucio por ti automáticamente!
# ==============================================================================