# 🧵 Lección 1: Concatenación y f-Strings en Python
En esta lección aprenderás a manipular textos combinados entre sí. En Python, los Strings no son solo texto, estático; podemos sumarlos, multiplicarlos y rellenarlos denámicamente con variables de una forma súper elegante.

---

## 🧩 1. Uniendo Textos (Concatenación y Multiplicación)
Python nos permite usar operadores aritméticos directamente con los textos. Sí, ¡has leído bien! Podemos usar el signo `+` y el signo `*`.

### ➕ A) Concatenación (Sumar Textos)
Consiste en pegar un texto al final de otro usando el operador `+`.
```python
nombre = "Tu nombre"
saludo = "Hola "+ nombre #Resultado: "Hola tu nombre"
```
> ⚠️ **Peligro de error (TypeError):** No puedes concatenar un texto (`str`) con un número (`int` o `float`) usando el signo `+`. Si intentas hacer `"Edad: " + 25", Python estallará.¡Para eso inventaron las f-string!

### ✖️ B) Multiplicación de Strings (Repetición)
Si multiplicas un texto por un número entero usando `*`, Python lo repetirá esa cantidad de veces.
```python
risa = "ja"*3 # Resultado: "jajaja"
```

## 🚀 2. f-strings (Formateo Literal de Cadenas)
Introducidas en Python 3.6, las f-strings son la forma moderna, rápida y limpia de de incrustar variables dentro de un texto. Solo tienes que poner una letra `f` minúscula justo antes de abrir las comillas, y podrás meter cualquier variable o código dentro de unas llaves `{}`.
```python
edad = 28
# ¡Olvidate de convertir números a texto manualmente!
mensaje = f"Tengo {edad} años." # Resultado: "Tengo 28 años".
```
## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: El Generador de nombres completos
Pide al usuario su nombre por teclado y luego su apellido. Crea una tercera variable llamada 'nombre_completo' que use la concatenación clásica para unirlos, asegurándote de dejar un espacio en blanco entre ambos. Muestra el resultado por consola.
### 🔹 Ejercicio 2: La Alerta del Sistema
Queremos pintar un banner de advertencia en la consola que llame mucho la atención del usuario. Usa la multiplicación de Strings para imprimir una línea con 30 asteriscos, luego el mensaje "¡ERROR CRITICO!" y cierra con otra linea de 30 asteriscos. Todo usando el menor código posible.
### 🔹 Ejercicio 3: F-String Express
Un compañero de trabajo antiguo ha dejado este código escrito usando concatenaciones con '+' y convirtiendo números a texto con str(): 
'mensaje = "El producto " + producto + " cuesta " + str(precio) + " euros."' Refactoriza (mejora) esa línea usando una f-string moderna para que sea mucho más legible y limpia.
### 🔹 Ejercicio 4: La Tarjeta de Presentación
Pide al usuario tres datos: su ocupación (texto), sus años de experiencia (entero) y si está disponible para trabajar (True/False). Construye una f-string que actúe como tarjeta de presentación imprimiendo todo en una sola frase coherente.
### 🔹 Ejercicio 5: Operaciones dentro de llaves
Las f-string no solo muestra variables, ¡pueden ejecutar código! Declara una variable llamada 'precio_unidad' con el valor 20. Pide al usuario cuántas unidades quiere comprar (entero). Muestra el coste total realizando la multiplicación DIRECTAMENTE dentro de las llaves '{}' del print, sin crear variables intermedias.