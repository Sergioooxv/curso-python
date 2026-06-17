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

import re

telefono = input("Escribe un número de telefono: ")