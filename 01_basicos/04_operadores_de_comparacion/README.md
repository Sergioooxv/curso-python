# ⚖️ Lección 4: Operadores Relacionales y Lógicos
En esta sección aprenderás a hacer preguntas a Python. Al utilizar estos operadores, Python no te devolvera un número ni un texto; te responderá estrictamente con un valor booleano: **`True`** (Verdadero) o **`False`** (Falso). ¡Es la base para que tu código tome decisiones!

---

## 🔍 1. Operadores Relacionales (Comparación)
Sirven para comparar dos valores. Ojo al truco: en programación, "comparar si son iguales" no se hace con un solo signo `=`, sino con dos `==`.

| Operador | Significado | Ejemplo | Resultado |
| :---: | :--- | :--- | :---: |
| `==` | **Igual a** | `5 == 5` | `True` |
| `!=` | **Diferente de (No es igual)** | `5 != 3` | `True` |
| `>` | **Mayor que** | `10 > 20` | `False` |
| `<` | **Menor que** | `8 < 15` | `True` |
| `>=` | **Mayor o igual que** | `5 >= 5` | `True` |
| `<=` | **Menor o igual que** | `4 <= 3` | `False` |

> ⚠️ **Peligro de examen:** Un solo signo `=` sirve para **guardar** datos en una variable (asignación). Dos signos `==` siven para **comparar** si dos cosas son iguales. ¡No los confundas!

---

## 🧠 2. Operadores Lógicos (And, Or, Not)
¿Qué pasa si tienes que comprobar dos condiciones a la vez? Por ejemplo: *para entrar a la discoteca necesitas ser mayor de 18 años **y** tener entrada*. Para eso usamos los operadores lógicos:

### 🤝 A) El Operador `and` (Exigente)
Devuelve `True` **solo si TODAS** las condiciones que estás comparando son verdaderas. Si una sola falla, todo se vuelve `False`.
* `True and True` -> `True`
* `True and False` -> `False`

### 🚪 B) El operador `or` (Permisivo)
Devuelve `True` si **al menos una** de las condiciones es verdadera. Solo da `False` si todas son falsas.
* `True or False` -> `True`
* `False or False` -> `False`

### 🔄 C) El operador `not` (El rebelde)
Simplemente **invierte** el resultado. Si algo es verdadero lo vuelve falso, y viceversa.
* `not True` -> `False`
* `not False` -> `True`

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Control de Acceso
Pide al usuario que introduzca su edad (entero). Crea una variable booleana llamada 'puede_entrar' que compare si la edad es mayor o igual a 18. Muestra el resultado por consola.
### 🔹 Ejercicio 2:
Declara una variable fija en tu código llamada 'clave_correcta' con el texto "admin123". Luego, pide al usuario por teclado que intente adivinar la contraseña. Compara si son exactamente iguales usando el operador relacional correcto y muestra el resultado.
### 🔹 Ejercicio 3:
Para obtener el carnet de conducir hay que aprobar dos fases. Pide al usuario que responda 'True' o 'False' a estas dos preguntas:
1. ¿Aprobaste el examen teórico?
2. ¿Aprobaste el examen práctico?
El alumno solo obtiene el carnet si aprueba **AMBOS**. Usa el operador 'and' para calcular el resultado e imprimelo.
### 🔹 Ejercicio 4:
Una tienda ofrece descuentos si el cliente cumple al menos uno de los requisitos: ser estudiante O ser jubilado. Pregunta al usuario si es estudiante (si/no) y si es jubilado (si/no). Usa el operador 'or' para determinar si se le aplica el descuento.
### 🔹 Ejercicio 5:
Declara una variable llamda 'tengo_hambre' y asignale el valor True. Imprime el valor de la variable, pero aplicandole el operador 'not' por delante. Observa el cambio en la consola y explica qué ha pasado