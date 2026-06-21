# ==============================================================================
# //======================================================================
#   EJERCICIO 4: VALIDADOR DE ESTADO DE RANGO MILITAR
#   ----------------------------------------------------------------------
#   Enunciado: En un videojuego de estrategia, un jugador recibe el rango de 
#   "Veterano" si sus 'puntos_experiencia' (int) superan los 5000 puntos. 
#   Si tiene 5000 o menos, su rango se mantiene en "Recluta".
#
#   Pide por consola los 'puntos_experiencia' y, utilizando el operador ternario 
#   en una sola línea, asigna el texto correspondiente a la variable 'rango'.
#   Imprime un mensaje elegante mostrando el resultado.
# //======================================================================

# 1. CAPTURA DE DATOS
puntos_experiencia = int(input("¿Cuantos puntos de experiencia tienes?: "))

# 2. OPERADOR TERNARIO DE ASIGNACIÓN DE ESTADO
rango = "Veterano" if puntos_experiencia > 5000 else "Recluta"

# 3. SALIDA FORMATEADA
print(f"Tu rango actual con {puntos_experiencia} es de: {rango}")

# ==============================================================================
# 👨‍🏫 TEORÍA EXTENDIDA PARA EL ALUMNO (Videojuegos y optimización de estados)
# ==============================================================================
# En el desarrollo de videojuegos, las variables de estado cambian miles de veces
# por segundo debido al bucle principal de renderizado (game loop). Usar estructuras
# compactas como el operador ternario ayuda a que el código de actualización de UI
# (interzad de usuario) sea directo, Limpio y fácil de depurar en tiempo real.
# 
# 🎮 APLICACIÓN EN LA INTERFAZ DE USUARIO (UI):
# Cuando un juego muestra datos en pantalla (como el nombre del rango encima de la 
# cabeza dle personaje), el motor gráfico suele reevaluar esta condición constantemente.
# Si usáramos bloques 'if-else' tradicionales de 4 líneas para cada texto dinámico de pantalla,
# el archivo de la interfaz se volveria kilométrico e inmanejable. El operador ternario
# mantiene la lógica de presentación pegada a la misma asignación garantizando un flujo de 
# trabajo mucho más ágil en la arquitectura de software.
# ==============================================================================