# ==============================================================================
# //======================================================================
#   EJERCICIO 4: VALIDADOR DE ARCHIVOS SEGUROS
#   ----------------------------------------------------------------------
#   Enunciado: Un usuario intenta subir un documento a tu plataforma.
#   Pide por teclado el nombre del archivo (ej: "factura.pdf", "foto.png").
#   Usa el método de verificación adecuado para comprobar si el archivo 
#   termina en ".pdf" y muestra un resultado booleano (True/False).
# //======================================================================

# 1. ENTRADA DE DATOS
nombre_archivo = input("¿Cual es el nombre de tu archivo con extensión?: ")

# 2. VALIDACIÓN DE EXTENSIÓN
# .endswith() comprueba el final de la cadena y devuelve un booleano puro (True/false)
archivo_correcto = nombre_archivo.endswith(".pdf")

# 3. SALIDA DE DATOS
print(f"El nombre de tu archivo es: {nombre_archivo} | la comprobación tiene que ser (.pdf): {archivo_correcto}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Validación de seguridad en sistemas reales)
# ==============================================================================
# El método '.endswith(".pdf")' es un detector especializado. Mira los últimos
# caracteres del string y comprueba si coinciden exactamente on lo que has puesto
# entre paréntesis.
# 
# 🛡️ SU APLICACIÓN EN EL MUNDO REAL:
# Este método se usa constantemente en páginas web y servidores para proteger sistemas:
#   - Para validar subida de imágenes: '.endswith(".png")' o '.endswith(".jpg")'.
#   - En sistemas de música: '.endswith(".mp3")'.
# 
# 💡 SU HERMANO GEMELO:
# De la misma forma que puedes varificar el final de un texto, Python te ofrece el
# método '.startswith("texto")' para verificar cómo EMPIEZA. por ejemplo, podrías usar
# 'url.startswith("https://")' para comprobar si una página web es segura. ¡Dos herramientas
# brutales para tu caja de herramientas!
# ==============================================================================