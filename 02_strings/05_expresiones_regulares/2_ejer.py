# ==============================================================================
# //======================================================================
#   EJERCICIO 2: CAZADOR DE EMAILS
#   ----------------------------------------------------------------------
#   Enunciado: Vamos a validar la presencia de un correo. Un email básico se 
#   compone de texto alfanumérico ('\w+'), una arroba '@', y más texto.
#   Usa 're.search()' para verificar si la variable 'correo' contiene una 
#   estructura válida e imprime un mensaje de confirmación en consola.
# //======================================================================

# 1. IMPORTAMOS EL MÓDULO NATIVO DE REGEX
import re

# 2. ENTRADA DE DATOS DINÁMICA
correo = input("Escribe tu correo: ")

# 3. DEFINICIÓN DEL PATRÓN (Texto + @ + Texto + . + Texto)
patron = r"\w+@\w+\.\w+"

# 4. VALIDACIÓN DE LA COINCIDENCIA
valido = re.search(patron,correo)

# 5. SALIDA DE DATOS
if valido: # re.search(patron,correo):
    print(f"✅ El correo '{correo}' tiene un formato VÁLIDO.")
else:
    print(f"❌ El correo '{correo}' NO es válido. Asegúrate de incluir la '@' y el '.' correctamente.")
    
# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (El peligro del punto en Regex)
# ==============================================================================
# Este ejercicio es un clásico de la programación. Vamos a desmenuzar el patrón
# paso a paso para entender como actúa el "bisturí" de Regex:
# 
#
#   r"\w+  @  \w+  \.  \w+"
# 
#   🧩 PIEZA A PIEZA:
#   - '\w': Significa cualquier carácter alfanumérico (letras de la A a la Z, números o guion bajo).
#   - '+': Es un cuantificador que significa "uno o más de los anteriores". Así que '\w+' se llevara
#   un bloque entero de texto (como "soporte" o "miempresa").
#   - '@': Busca la arroba de manera exacta y literal.
#   - '\.': ¡CUIDADO AQUÍ! En el lenguaje Regex, el punto por si solo '.' es un comodín que 
#   significa "cualquier carácter del mundo". Si queremos buscar un punto real de texto
#   (el del .com, .es, etc.), tenemos que ponerle una barra invertida delante '\.'.
#   A esto se le llama "escapar el carácter".
# 
#  💡 NOTA AVANZADA: Este patrón es genial para aprender, pero en producción real se usan patrones
#  mucho más largos para evitar que se cuelen caracteres raros. ¡Pero como base de aprendizaje es imbatible!
# ==============================================================================