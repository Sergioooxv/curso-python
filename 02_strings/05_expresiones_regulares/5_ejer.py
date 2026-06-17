# ==============================================================================
# //======================================================================
#   EJERCICIO 5: EL VALIDADOR DE MATRÍCULAS
#   ----------------------------------------------------------------------
#   Enunciado: Las matrículas actuales en España constan de 4 números seguidos 
#   de 3 letras mayúsculas (ejemplo: "1234FGH"). 
#   Crea un patrón estricto usando '{4}' y '{3}' y comprueba si la variable 
#   'matricula_coche' cumple con el estándar oficial de tráfico.
# //======================================================================

# 1. IMPORTAMOS EL MÓDULO NATIVO DE REGEX
import re

# 2. VARIABLE CON LA MATRÍCULA A CONTROLAR
matricula_coche = "2847KLP"

# 3. PATRÓN ESTRICTO DE TRÁFICO (4 números + 3 letras mayúsculas)
patron_matricula = r"\d{4}[A-Z]{3}"

# 4. VALIDACIÓN DE ENTRADA CON RE.MATCH()
# re.match exige que el patrón coincida exactamente desde el inicio del texto
if re.match(patron_matricula, matricula_coche):
    print("Matrícula VÁLIDA detectada. Acceso al parking autorizado.")
else:
    print("Matrícula NO válida. Acceso denegado.")
    
# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Rangos de letras y validación de inicio)
# ==============================================================================
# Para cerrar el bloque de Regex, hemos subido el nivel creando un patrón compuesto 
# que combina números y un rango específico de letras.
#
# 🕵️‍♂️ DESGLOSE DEL PATRÓN COMPUESTO:
#   - '\d{4}': Busca exactamente un bloque de CUATRO números seguidos.
#   - '[A-Z]': Los corchetes definen un "rango de caracteres". En este caso, le 
#     estamos diciendo a Python: "Aquí solo permito letras individuales que vayan 
#     desde la 'A' hasta la 'Z' (es decir, letras de nuestro alfabeto en MAYÚSCULAS)".
#   - '{3}': Es el cuantificador que obliga a que el rango anterior ('[A-Z]') se 
#     repita exactamente TRES veces seguidas.
#
# 🚨 LA GRAN DIFERENCIA: ¿POR QUÉ RE.MATCH() Y NO RE.SEARCH()?
#   - 're.search()' busca el patrón en cualquier rincón. Si la matrícula fuera 
#     "Hola, mi coche es 2847KLP", search diría que es VÁLIDA porque el patrón existe dentro.
#   - 're.match()' es mucho más estricto. Exige que el texto empiece obligatoriamente 
#     con el patrón. Si el texto tiene cualquier palabra o espacio delante de los números, 
#     dará 'False'. 
#
# Para sistemas automáticos como barreras de parking, lectores de peajes o radares, 
# 're.match()' es la herramienta idónea para asegurar que el dato leído es limpio y puro.
# ==============================================================================