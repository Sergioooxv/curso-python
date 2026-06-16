# ==============================================================================
# //======================================================================
#   EJERCICIO 2: EL VALIDADOR DE CONTRASEÑAS
#   ----------------------------------------------------------------------
#   Enunciado: Declara una variable fija en tu código llamada 'clave_correcta'
#   con el texto "admin123". Luego, pide al usuario por teclado que intente 
#   adivinar la contraseña. Compara si son exactamente iguales usando el 
#   operador relacional correcto y muestra el resultado.
# //======================================================================

# 1. CONFIGURACIÓN INICIAL Y ENTRADA
clave_correcta = "admin123"
intento = input("Adivina la contraseña: ")

# 2. COMPARACIÓN DE TEXTO DIRECTA
# Usamos el operador '==' para comparar si los dos textos son idénticos.
acceso_concedido = clave_correcta == intento

# 3. SALIDA DE DATOS
print(f"Tu clave es: {acceso_concedido}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Python es "Case Sensitive")
# ==============================================================================
# Comparar texto en programación funciona igual de rápido que comparar números.
# El operador '==' mira carácter por carácter para verificar si las cadenas 
# coinciden.
# 
# ⚠️ DETALLE MUY IMPORTANTE:
# Python es un lenguaje 'Case Sensitive' (sensible a mayúsculas y minúsculas).
# Si el usuario introduce 'Admin123' o 'ADMIN123', el resultado será 'False'.
# Para que devuelva 'True', tiene que ser exactamente igual, letra por letra:
# 'admin112'.
# 
# Más adelante en el curso aprenderás trucos como '.lower()' para convertir todo
# a minusculas automáticamente y evitar que el programa falle por un despiste del 
# usuario.
# ==============================================================================