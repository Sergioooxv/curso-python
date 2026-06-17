# ==============================================================================
# 🗃️ BLOQUE 02: STRINGS | TEMA 05: EXPRESIONES REGULARES
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: EL DETECTOR DE TELÉFONOS
#   ----------------------------------------------------------------------
#   Enunciado: Queremos verificar si un usuario ha introducido un número de 
#   teléfono válido en nuestro formulario. En España los móviles tienen 9 dígitos.
#   Importa el módulo 're', define el patrón correcto para buscar 9 números 
#   seguidos ('\d') y comprueba si la variable 'telefono' lo cumple usando 're.search()'.
# //======================================================================

# 1. IMPORTAMOS EL MÓDULO NATIVO DE REGEX
import re

# 2. ENTRADA DE DATOS DINÁMICA
telefono = input("Introduce tu número de telefono: ")
# 3. DEFINICIÓN DEL PATRÓN (9 dígitos seguidos)
patron = r"\d{9}"

# 4. BÚSQUEDA DEL PATRÓN EN EL TEXTO
# re.search busca el patrón en cualquier parte de la cadena introducida
exite = re.search(patron,telefono)

# 5. CONTROL DE FLUJO / RESPUESTA
if exite:
    print(f"El número de telefono {telefono} es valido. ✅")
else:
    print(f"El número de telefono {telefono} no es valido. ❌")
    
# ==============================================================================
# 👨‍🏫 EXPLICACIÓN PARA EL ALUMNO (Tu primer patrón inteligente)
# ==============================================================================
# Las expresiones Regulares (Regex) son plantillas que sirven para buscar patrones
# de texto en lugar de palabras exactas. En Python, activamos este superpoder
# importando el módulo 're'.
# 
# 🕵️‍♂️ DESCOMPONIENDO EL PATRON: 'r"\d{9}"'
# - La 'r' al principio le dice a Python que es un "Raw String" (texto en bruto).
# Esto evita que interprete la barra invertida '\' como un salto de línea u otro comando.
# - '\d' es el comodín que significa "Digito númerico" (Cualquier número del 0 al 9).
# - '{9}' es un cuantificador. Le dice a Python: "El elemento anterior (\d) se tiene que
# repartir exactamente NUEVE veces seguidas".
# 
# 🔍 ¿QUÉ HACE 're.search()'?
# Escanea todo el texto que meta el usuario. Si encuentra un bloque de 9 números juntos
# (por ejemplo, dentro de "Mi tlf es 612345678"), devolverá un objeto con la coincidencia
# (que evalúa como True). Si el usuario pone letras o solo 5 números, devolverá 'None' (que
# evarlúa como False).
# 
# 💡 NOTA PARA LA CLASE: Como usamos 're.search()', si un alumno escribe "Hola 600111222 adios",
# el programa dirá que es VÁLIDO porque el patrón EXISTE en mitad del texto. Más adelante 
# aprenderemos a blindar los extremos si hiciera falta.
# ==============================================================================