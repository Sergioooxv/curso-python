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