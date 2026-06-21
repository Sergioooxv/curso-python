# ==============================================================================
# //======================================================================
#   EJERCICIO 3: INTERFAZ DINÁMICA (MODO OSCURO AUTOMÁTICO)
#   ----------------------------------------------------------------------
#   Enunciado: El sistema operativo de un móvil cambia su interfaz según la hora.
#   Pide al usuario la 'hora_actual' (int, formato de 0 a 23).
#
#   Aplica esta regla en una sola línea con operador ternario:
#   Si la hora es mayor o igual a las 20 (8 PM) O menor o igual a las 6 (6 AM), 
#   la variable 'modo_pantalla' debe ser "DARK". En cualquier otro horario, debe 
#   ser "LIGHT". Cruza operadores lógicos dentro del ternario.
# //======================================================================

# 1. CAPTURA DE DATOS
hora_actual = int(input("Escribe tu hora actual (Formato: 0 a 23): "))

# 2. OPERADOR TERNARIO CON OPERADOR LÓGICO COMPUESTO ('or')
modo_pantalla = "DARK" if hora_actual >= 20 or hora_actual <= 6 else "LIGHT"

# 3. SALIDA POR PANTALLA
print(f"Configuración del sistema renderizada a modo: {modo_pantalla}")