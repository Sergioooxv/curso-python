#===================================================================
# DOCUMENTACIÓN — Calculadora de IMC
# Autor: Sergio Salas
# Versión: 1.0
#===================================================================

# DESCRIPCIÓN
# Programa que calcula el Índice de Masa Corporal (IMC) de una persona
# a partir de su peso y altura, y determina su categoría de salud.

# FÓRMULA
# IMC = peso (kg) / altura² (m)

# ELEMENTOS UTILIZADOS
#
# input()
#   Pide datos al usuario por teclado.
#   Siempre devuelve texto (string).
#
# float()
#   Convierte texto a número decimal.
#   Necesario porque input() devuelve string
#   y no se pueden hacer cálculos con texto.
#
# math.pow(x, n)
#   Eleva x a la potencia n.
#   Usamos math.pow(altura, 2) para calcular altura².
#   Requiere importar el módulo math al inicio.
#
# if / elif / else
#   Estructura de condiciones.
#   El programa evalúa cada condición en orden
#   y ejecuta solo el bloque que se cumple.
#
# <= y 
#   Operadores de comparación encadenados.
#   18.5 <= imc < 25 significa
#   "imc es mayor o igual a 18.5 Y menor que 25".
#
# str()
#   Convierte un número a texto.
#   Necesario para concatenar números con strings.
#
# round(numero, decimales)
#   Redondea un número a los decimales indicados.
#   round(imc, 2) muestra el IMC con 2 decimales.

# CATEGORÍAS DE IMC
# Menos de 18.5        → Bajo peso
# Entre 18.5 y 24.9    → Peso normal
# Entre 25.0 y 29.9    → Sobrepeso
# Entre 30.0 y 34.9    → Obesidad grado I
# Entre 35.0 y 39.9    → Obesidad grado II
# 40 o más             → Obesidad grado III

#===================================================================
#Importamos modulo math para utilizar math.pow()
import math

#Pedimos los datos al usuario con input y guardamos los datos en las vaiables
nombre = input("¿Como te llamas?: ")
peso = float(input("¿Cual es tu peso?: "))
altura = float(input("¿cual es tu altura en metros? (ej: 1.80): "))
#Texto plano con Print
print("//===================================================================")
print("// ANALISIS DE LOS DATOS")
print("//===================================================================")
print("\nOkey ya tenemos todo lo que necesitamos... Analizando tus datos:")

#Hacemos calculo de potencia con math.pow()
imc = peso/math.pow(altura,2)

#Acemos las comprobaciones para ver en que rango esta el usuario
if imc < 18.5:
    categoria ="Bajo peso"
elif 18.5 <= imc < 25:
    categoria ="Peso normal"
elif 25 <= imc < 30:
    categoria ="Sobrepeso"
elif 30 <= imc < 34.9:
    categoria ="Obesidad grado I"
elif 35 <= imc < 39.9:
    categoria ="Obesidad grado II"
elif 40 <= imc:
    categoria ="Obesidad grado III "
else:
    print("No has introducido datos")
    
print("Ya tenemos todo "+nombre+"!!")
print("tu IMC es el siguiente: "+str(round(imc,2)))
print("Tu categoria es: "+categoria)

