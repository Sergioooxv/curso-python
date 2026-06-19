# ==============================================================================
# //======================================================================
#   EJERCICIO 3: CENTRAL DE ALARMAS DOMÉSTICA
#   ----------------------------------------------------------------------
#   Enunciado: Programamos el software de una alarma. Pide dos datos por consola:
#   'sensor_movimiento' (si/no) y 'sistema_activado' (si/no).
#
#   La alarma debe dispararse (imprimir "🚨 ¡ALERTA! Intruso detectado...") si:
#   - El 'sensor_movimiento' se activa (da True) Y el 'sistema_activado' NO está 
#     en modo mantenimiento (es decir, el sistema está encendido, True).
#
#   Si el sensor detecta movimiento pero la alarma estaba apagada, debe imprimir 
#   "Aviso silencioso: Movimiento detectado con alarma desactivada". En cualquier 
#   otro caso, imprimir "Sistema seguro". Usa operadores lógicos para resolverlo.
# //======================================================================

# 1. CAPTURA DE DATOS Y CONVERSIÓN A BOOLEANOS PUROS
# Aplicamos .lower() para evitar fallso si el usuario escribe en mayúsculas
movimiento_detectado = input("¿El sensor detecta movimiento? (Si/No): ").lower() == "si"
sistema_encendido = input("¿El sistema de alarma está conectado? (Si/No): ").lower() == "si"

# 2. EVALUACIÓN DE SEGURIDAD CON OPERADORES LÓGICOS ('and' y 'not')
if movimiento_detectado and sistema_encendido:
    # Caso 1: Movimiento + Alarma encendida = Disparo total
    print("🚨 ¡ALERTA! Intruso detectado.")
elif movimiento_detectado and not sistema_encendido:
    # Caso 2: Movimiento + Alarma apagada = Alerta silenciosa de control
    print("⚠️ Aviso silencioso")
else:
    # Caso 3: No hay movimiento, o el sistema está seguro
    print("🟢 Sistema seguro.")

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (La limpieza al evaluar Booleanos Reales)
# ==============================================================================
# En el desarrollo de software profesional, la claridad del código y el manejo exacto
# de los tipos de datos diferencian a un programador novel de uno experto.
# 
# 🚫 EL ERROR DE COMPARAR BOOLEANOS CON TEXTO:
# Si transformas una variable en booleano al hacer 'input() == "si"', esa variable
# pasa a contener un valor 'True' o 'False'.
# Si más adelantes escribes 'if variable == "si":', estás comparando el valor 'True'
# con la palabra '"si"'. Para Python, mezclar peras con manzanas da siempre 'False'.
# El condicional no se ejecutará nunca, creando un agujero de seguridad crítico.
# 
# 🧼 CÓMO EVALUAR BOOLEANOS COMO UN PROFESIONAL:
# Si una variable ya es un booleano, NO hace falta poner '== True' ni '== False'.
# Python entiende los booleanos de forma nativa dentro de los condicionales:
#   - Escribir 'if movimiento_detectado:' es suficiente. Si value True, entra; si no, salta.
# 
# 🔄 EL PODER DE INVERSIÓN DEL OPERADOR 'not':
# Mira el bloque 'elif': 'elif movimiento_detectado and not sistema_encendido:'.
# El operador 'not' invierte el sentido de la variable booleana que tiene a su derecha.
# Si 'sistema_encendido' es 'False' (porque el usuario contestó "No"), 'not sistema_encendido'
# se transforma mágicamente en 'True'.
# Al volverse True, el operador 'and' se valida por completo y permite disparar el aviso
# silencioso. Esto hacee que el código se lea de manera fluida y natural: "Si hay movimiento y
# NO está el sistema encendido...".
# ==============================================================================
    