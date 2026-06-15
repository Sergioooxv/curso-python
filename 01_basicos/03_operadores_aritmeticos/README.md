# 🧮 Lección 3: Operadores Aritmeticos en Python
En esta sección aprenderás a transformar tu código en una calculadora. Python puede realizar operaciones aritmeticas a una velocidad absurda, desde sumas básicas hasta cálculos complejos usando operadores avanzados.

---

## ➕ 1. Los Operadores Básicos y Avanzados
Aquí tienes la tabla definitiva con los 7 operadores aritméticos que necesitas dominar en Python:

| Operador | Operación | Ejemplo | Resultado | Descripción |
| :---: | :--- | :--- | :---: | :--- |
| `+` | **Suma** | `5 + 3` | `8` | Suma dos valores. |
| `-` | **Resta** | `10 - 4` | `6` | Resta el segundo valor del primero. |
| `*` | **Multiplicación** | `4 * 3` | `12` | Multiplica dos valores. |
| `/` | **División Real** | `10 / 4` | `2.5` | Divide dando **siempre** un resultado decimal (`float`). |
| `//` | **División Entera** | `10 // 4` | `2` | Divide pero **elimina los decimales**, devolviendo solo el entero. |
| `%` | **Módulo (Resto)** | `10 % 4` | `2` | Devuelve el **resto** que sobra de una división entera. |
| `**` | **Exponente (Potencia)**| `2 ** 3` | `8` | Eleva el primer número a la potencia del segundo ($2^3$). |

---

## 👑 2. Jerarquía de las Operaciones (Procedencia)

¿Cuánto da `5 + 3 * 2`? Si respondiste `16`, ¡error! ❌ El resultado es `11`.

Python, al igual que las matemáticas del colegio, sigue un orden estricto para resolver operaciones cuando hay varias juntas. El orden de prioridad (de mayor a menor) es:

1. **Paréntesis `()`:** (Tienen el poder máximo, resuelven primero lo que haya dentro).
2. **Potencias `**`**
3. **Multiplicación `*`, División `/`, División entera `//`, Módulo `%` **(Tienen la misma prioridad)**
4. **Suma `+` y Resta `-`** (Tienen la prioridad más baja).

> 💡 **Regla de oro:** Si dos operadores tienen la misma prioridad (como un `*`  y un `/`), Python resuelve de **izquierda a derecha**.

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: La Calculadora Básica
Pide al usuario que introduzca dos números enteros por teclado.
Calcula y muestra en la consola el resultado de:
1. La Suma.
2. La Resta.
3. La Multiplicación.
4. La División.
### 🔹 Ejercicio 2: El Conversor de Euros a Dolares
Crea un conversor de Euros a Dolares.
1. Pide al usuario la cantidad de euros que quiere cambiar (puede tener decimales).
2. Declara una variable fija con el tipo de cambio (ej: 1 euro = 1.09 dolares).
3. Calcula cuántos dólares equivalen e imprime el resultado con 2 decimales.
### 🔹 Ejercicio 3: Calculadora de IVA
Pide al usuario el precio base de un producto (decimal).
Caulcula el valor del IVA (21% en España) y muestra en consola:
1. Cuánto dinero es el IVA del producto.
2. El precio final total (Precio base + IVA).
### 🔹 Ejercicio 4: Reparto de Caramelos
Imagina que tienes 15 caramelos y quieres repartirlos entre 4 niños en partes exactamente iguales (sin romper caramelos).
Crea un programa que calcule y muestre usando los operadores `//` y `%`:
1. Cuántos caramelos enteros recibe cada niño.
2. Cuántos caramelos sobran en la bolsa y te quedas tu.
### 🔹 Ejercicio 5: El Desafio de la Prioridad
Queremos calcular la nota media de un alumno que ha sacado un 4.0 en el primer examen y un 8.0 en el segundo examen.
Si escribes: 'media = 4.0 + 8.0 / 2', Python dará un resultado incorrecto (8.0). Arregla ea línea usando paréntesis 
para oblicar a Python a calcular la nota media real (6.0) e imprime el resultado.