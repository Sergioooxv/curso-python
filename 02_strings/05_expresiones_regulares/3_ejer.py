# ==============================================================================
# //======================================================================
#   EJERCICIO 3: EXTRACCIÓN DE PRECIOS (FINDALL)
#   ----------------------------------------------------------------------
#   Enunciado: Un sistema automático ha extraído este texto de una web: 
#   "El menú cuesta 15 euros, la bebida son 3 euros y el postre 5 euros".
#   Utiliza la función 're.findall()' junto con el patrón adecuado para extraer 
#   ÚNICAMENTE los números sueltos y guardarlos en una lista. Imprime la lista.
# //======================================================================

# 1. IMPORTAMOS EL MÓDULO NATIVO DE REGEX
import re

# 3. EXTRACCIÓN MULTIPÁTRON CON FINDALL
# \d+ busca bloques numéricos (de uno o más dígitos seguidos)
texto_precios = "El menú cuesta 15 euros, la bebida son 3 euros y el postre 5 euros"
numeros = re.findall(r"\d+", texto_precios)

# 4. SALIDA DE DATOS
print(f"Texto original: {texto_precios}")
print(f"Lista de precios encontrados: {numeros}")

# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Extrayendo colecciones de datos)
# ==============================================================================
# Hasta ahora, con 're.search()', solo comprobábamos si un patrón existía una vez. 
# Pero en el mundo real (como al hacer Web Scraping), necesitamos extraer TODOS los 
# datos de un tipo que aparezcan en una página o texto. Para eso sirve 're.findall()'.
#
# 🎯 ANÁLISIS DEL PATRÓN COLECTOR: 'r"\d+"'
#   - '\d': Ya sabemos que busca un dígito (0-9).
#   - '+': Es el cuantificador clave. Significa "uno o más de lo mismo". 
#
# 🕵️‍♂️ ¿POR QUÉ EL PLÚS '+' ES TAN IMPORTANTE?
# Si hubieras escrito 're.findall(r"\d", texto_precios)' (sin el +), Python habría 
# extraído los números de uno en uno, devolviéndote esto: ['1', '5', '3', '5']. 
# ¡Habría destrozado el número 15! 
# Gracias al '+', cuando Python encuentra el '1', mira al lado, ve el '5', y dice: 
# "Vale, esto es un bloque completo". Y te extrae el '15' unificado.
#
# 💡 OJO AL DATO: 're.findall()' siempre devuelve los elementos en formato de Texto 
# (Strings), dentro de una lista: "['15', '3', '5']". Si en el futuro quisiéramos 
# sumar esos precios, tendríamos que convertirlos a enteros usando 'int()'.
# ==============================================================================