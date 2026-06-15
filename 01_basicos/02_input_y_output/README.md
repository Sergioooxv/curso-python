# 🗣️ Lección 2: Input y Output (Entradas y Salidas)

¡Ya sabes guardar datos en variables! ahora aprenderás a hacer que tus programas sean interactivos: cómo perdirle información a un usuario a través del teclado (**Input**) y cómo mostrarle los resultados en la pantalla (**Output**).
---
## 📤 1. Output: Mostrar datos con `print()`
La función `print()` pinta en la consola lo que le metas dentro. como vimos en la lección anterior, podemos pasarle varios datos separados por comas o usar la forma profesional: las **f-strings**.

```python
nombre = "Tu nombre"
# Forma moderna y limpia (f-string)
print(f"Hola, {nombre}, ¡bienvenido al curso!)
```

💡 Trucos avanzados de `print()` que debes conocer:
* **Salto de línea(\n):** Rompe el texto y lo pasa a la línea de abajo.
* **Tabulador(\t):** Mete un espacio grande de sangría.
* **El parrafo `end`:** Por defecto, cada `print()` hace un salto de línea al final. Si quieres que el sigueitne `print()` se quede en la mimsa linea usa `end=""`.

```python
print("Hola", end="")
print("Mundo") # Salida: Hola mundo (en la misma línea)
```

## 📥 2. Input: Recibir datos con `input()`

Ls función `input()` detiene el programa y se queda esperando a que el usuario escriba algo en la consola y pulse **Enter**.

```python
color = input("¿Cual es tu color favorito?")
```

### ⚠️ La Regla de oro de `input()` (¡Peligro!)

**IMPORTANTE** Todo lo que el usuario escribe a través de `input()`, Python lo recibe SIEMPRE como un texto (str). Siempre.
Si le pides su edad y el usuario escribe 25, Python guardará el texto "25". Si intentas hacer mátematicas con eso, el programa romperá.

Para solucionarlo, debes envolver el `input()` dentro de una función de conversión (`int()` o `float()`). A esto se le llama anidación de funciones:

```python
# Así se pide un número entero correctamente
edad = int(input("Introduce tu edad:"))

# Así se pide un número decimal correctamente:
precio = float(input("¿Cuánto cuesta el cafe?:"))
```

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: El Saludo Personalizado
Pide al usuario su nombre y su apellido usando dos funciones `input()` diferentes. Luego, muestra un único saludo en la consola usando `f-strings` que diga: "¡Hola [nombre] [apellido]! Que bueno tenerte aquí"

### 🔹 Ejercicio 2: La Máquina del tiempo
Pide la edad y calcula cuántos años tendrá el usaurio en el futuro (¡Cuidado con los tipos!).

### 🔹 Ejercicio 3: Formateando Facturas
Diseña una salida visual limpia usando saltos de líneas y tabuladores

### 🔹 Ejercicio 4: La cuenta del Restaurante
Pide el total de una cuenta, el numero de amigos y calcula cuánto paga cada uno con decimales.

### 🔹 Ejercicio 5: Imprimiendo en Línea
Juega con el parametro `end` para romper el comportamiento nativo del `print()`.
