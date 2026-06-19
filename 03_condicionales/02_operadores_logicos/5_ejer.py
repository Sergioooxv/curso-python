# ==============================================================================
# //======================================================================
#   EJERCICIO 5: FIREWALL DE SEGURIDAD (EL GRAN DESAFÍO COMBINADO)
#   ----------------------------------------------------------------------
#   Enunciado: Vamos a simular el cortafuegos de un servidor militar. 
#   El acceso solo se concede si se cumple una de las siguientes dos grandes vías:
#
#   - Vía 1 (Superusuario): El 'usuario' es exactamente "root" y la 'clave' es "1234".
#   - Vía 2 (Usuario estándar verificado): El 'usuario' es un empleado dado de alta 
#     (cualquiera diferente a "root"), la 'clave' es correcta, la 'ip_permitida' 
#     es True Y además estamos dentro del 'horario_laboral' (True).
#
#   Pide los datos necesarios y monta una estructura condicional robusta para 
#   autorizar o denegar el acceso.
# //======================================================================


usuario = input("LOGIN - INTRODUCE TU USUARIO: ")
clave = input("LOGIN - INTRODUCE TU CLAVE: ")

clave_estandar_valida = "pass123"

ip_permitida = input("¿La IP de origien está en la lista blanca? (Si/No): ").lower() == "si"
horario_laboral = input("¿El intento ocurre en Hoario laboral? (Si/No): ").lower() == "si"

via_superusuario = (usuario == "root" and clave == "1234")

via_estandar = (usuario != "root" and clave == clave_estandar_valida and ip_permitida and horario_laboral)

if via_superusuario or via_estandar:
    print("[ACCESS GRANTED] – Identidad verificada. Bienvenido al servidor central.")
else:
    print("[ACCESS DENIED] – Intrusión detectada o parámetros de red fuera de rango. IP reportada.")