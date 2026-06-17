# ==============================================================================
# //======================================================================
#   EJERCICIO 4: CENSURA DE DATOS CONFIDENCIALES (SUB)
#   ----------------------------------------------------------------------
#   Enunciado: En los logs de tu servidor se ha filtrado este texto sensible: 
#   "El cliente pago con la tarjeta 1234-5678-9012-3456 en la web".
#   Investiga o utiliza la función 're.sub()' para buscar el patrón de los 
#   16 dígitos de la tarjeta (separados por guiones si quieres, o directamente) 
#   y reemplázalos por la palabra "[CENSURADO]" antes de mostrar el texto por pantalla.
# //======================================================================

# 1. IMPORTAMOS EL MÓDULO NATIVO DE REGEX
import re

# 2. VARIABLE CON INFORMACIÓN SENSIBLE
log_servidor = "El cliente pago con la tarjeta 1234-5678-9012-3456 en la web"

# 3. PATRÓN DE LA TARJETA Y REEMPLAZO CON RE.SUB()
# Definimos el patrón de 4 bloques de 4 dígitos separados por guion
patron_tarjeta = r"\d{4}-\d{4}-\d{4}-\d{4}"

# re.sub(patron, reemplazo, texto_original)
log_limpio = re.sub(patron_tarjeta, "[CENSURADO]", log_servidor)

# 4. SALIDA DE DATOS
print(f"Texto original: {log_servidor}")
print(f"Texto protegido: {log_limpio}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Ciberseguridad y limpieza de datos con re.sub)
# ==============================================================================
# En el desarrollo de software profesional, la seguridad es lo primero. Jamás se 
# deben guardar datos como tarjetas de crédito, contraseñas o DNIs en abierto en 
# los archivos de registro (logs). La función 're.sub()' (de substitución) es la 
# herramienta reina para solucionar esto.
#
# 🔧 ¿CÓMO FUNCIONA LOS PARÁMETROS DE 're.sub()'?
# Necesita tres argumentos obligatorios en sus paréntesis:
#   1. El patrón que tiene que buscar: 'patron_tarjeta' (4 números - 4 números...).
#   2. El texto que va a poner en su lugar: '"[CENSURADO]"'.
#   3. La variable o texto original donde tiene que operar: 'log_servidor'.
#
# 🕵️‍♂️ LA VANTALA DEL PATRÓN COMPUESTO:
# Al diseñar '\d{4}-\d{4}-\d{4}-\d{4}', le estamos diciendo a Python que sea muy 
# específico. Si en el texto pusiera "El cliente compró 4 libros", el número 4 
# NO se censuraría, porque no cumple la estructura de la tarjeta entera. Python 
# solo morderá cuando localice el patrón completo, manteniendo el resto del texto 
# intacto. ¡Una maravilla para proteger datos masivos!
# ==============================================================================