# ==============================================================================
# 🗃️ BLOQUE 03: CONDICIONALES | TEMA 01: IF, ELIF, ELSE
# ==============================================================================
# //======================================================================
#   EJERCICIO 1: EL CONTROLADOR DE ACCESO AL CASINO (LÓGICA ANIDADA)
#   ----------------------------------------------------------------------
#   Enunciado: Diseña un sistema de acceso para un casino que pida al usuario 
#   dos datos por consola: su 'edad' (entero) y si posee el 'pase_vip' (booleano).
#
#   Reglas de negocio estrictas:
#   1. Si es menor de 18 años, el acceso está terminantemente denegado.
#   2. Si tiene entre 18 y 21 años (ambos incluidos), solo puede pasar si posee 
#      el pase VIP (True). Si no lo tiene, se le deniega el acceso con un aviso.
#   3. Si tiene más de 21 años, el acceso es libre e inmediato (tenga o no VIP).
#
#   Muestra un mensaje personalizado e hiperclaro para cada uno de los escenarios.
# //======================================================================

# 1. CAPTURA Y SANEAR DATOS
edad = int(input("¿Cual es tu edad?: "))
pase_vip = input("¿Tienes pase Vip?: ")

# Saneamos la entrada para tener un booleano puro (True/False)
tiene_vip = pase_vip.lower()== "si"
    
# 2. EVALUACIÓN POR CAPAS EXCLUSIVAS
if edad < 18:
    # 2.1: Menores de edad descártados de golpe
    print("Tienes el acceso totalmente prohibido")
elif edad <= 21:
    # 2.2: Tramo intermedio (De 18 a 21 años)
    # Solo entran aquí si NO son menores de 18 y si NO superan los 21.
    if tiene_vip:
        print("Tienes la edad y el VIP puedes entrar")
    else:
        print("Tienes la edad pero no tienes el VIP")
else:
    # 2.3: Mayores de 21 años libres de restricciones
    print("Acceso Autorizado: Eres mayor de 21 años. Tu entrada es Libre e inmediata.")
    
# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (El peligro de los embudos infinitos)
# ==============================================================================
# Diseñar condicionales eficientes requiere entender que Python evalúa las opciones
# en cascada (de arriba hacia abajo) y se detiene en la PRIMERA parada que sea Verdadera.
# 
# 🛑 EL ERROR DEL "EMBUDO ANCHO" (Por qué cambiamos '18 <= edad' por 'edad <=21'): 
# Si escribimos 'elif 18 <= edad', estamos abriendo una puerta gigante. Si un cliente
# introduce que tiene 35 años, Python comprueba el primer 'if' (35 < 18 -> False) y 
# salta al 'elif'. Al leer '18 <= 35' (-> True), Python se mete de cabeza en esa habitación
# y se pone a comprobar si tiene VIP.
# 
# ¿Cuál es el problema? Que ese cliente de 35 años JAMÁS llegará al 'else' del final,
# porque Python ya ha encontrado una parada válida y da por terminado todo el bloque de 
# decisiones. El 'else' final se convierte en "código muerto".
# 
# 🎯 LA SOLUCIÓN CORRECTA:
# Al acortar el segundo escalón como 'elif edad <= 21', creamos tramos herméticos:
#   - Tramo 1: Menores de 18.
#   - Tramo 2: Entre 18 y 21 (Los que pasaron el primer filtro pero no superan los 21)
#   - Tramo 3 ('else'): Todos los demás (es decir, los mayores de 21).
# 
# De esta manera, el código es 100% robusto, no tiene fugas de lógica y el negocio funciona
# exactamente como el cliente o la empresa ha solicitado. ¡Asegurar los limites de los rangos
# es la diferencia entre un código junior y uno profesional!#