# 👨‍🏫 Lección 1: Variables y Tipos de Datos en Python

¡Bienvenido/a al inicio de tu viaje con Python!
En esta primera sección vas a entender cómo tu ordenador almacena información en su memoria
y cómo interactuar con los diferentes tipos de datos que existen.

---

## 📌 1. ¿Qué es una Variable?

Imagina una variable como una **caja con una etiqueta pegada por fuera**. Puedes meter un valor dentro de la caja
(un número, un texto, etc.) y, cada vez que uses el nombre de la etiqueta en tu código, Python irá a la caja a buscar ese valor.

En Python, crear una variable es tan fácil como escribir su nombre y asignarle un valor usando el signo igual (`=`):

```python
edad = 26
nombre = "Profesor"
```

### ⚠️ Reglas obligatorias para nombrar variables:
1. **Minúsculas y Guiones Bajos:** Usamos el estilo `snake_case`. Si el nombre tiene varias palabras, se separan con guíon bajo (ej: `mi_edad_actual = 26`).
2. **No empezar con números:** `1variable` romperá el programa. Usa `variable1`.
3. **Sin caracteres especiales:** No uses espacios, eñes ni acentos en los nombres de las variables (`año` o `dirección` pueden dar problemas; usa `anio` o `direccion`).

## 🔢 2. Los 4 Tipos de Datos Fundamentales
A diferencia de otros lenguajes, Python es de tipado dinámico. Esto significa que no necesitas decirle "oye, te voy a guardar un texto; él solito ve las comillas y dice: "¡Ahh, esto es un texto!".

Aquí tienes los cuatro tipos de datos esenciales que usarás el 90% del tiempo:

| Tipo de Dato | Nombre en Python | Ejemplo | Descripción |
| :--- | :--- | :--- | :--- |
| **Entero** | `int` | `10`, `-5`, `0` | Números completos sin decimales. |
| **Decimal** | `float` | `3.14`, `-0.5` | Números con punto decimal. (En programación se usa punto `.`, no coma `,`).|
| **Texto** | `str` (String) | `"Hola"`, `'Mundo'` | Cadenas de texto envueltas en comillas dobles o simples. |
| **Booleano** | `bool` | `True`, `False` | Estados lógicos: Verdadero o Falso. ¡Ojo! La primera letra va en mayúscula. |

### 🔍 ¿Cómo saber el tipo de una variable?
Puedes usar la función integrada `type()` combinada con `print()` para que Python te diga qué tiene dentro esa variable:

```python
puntuacion = 9.5
print(type(puntuacion)) #Salida: <class 'float'>
```

## 🔄 3. Conversación de Tipos (Type Casting)
A veces necesitas transformar un dato en otro. Por ejemplo, si tienes el texto `"25"` y quieres sumarle `1`, necesitas transformarlo en un número entero. Para eso usamos funicones con el mismo nombre del tipo de dato:

```python
texto_numero = "25"
numero_real = int(texto_numero) # Ahora es un numero (int) igual a 25

estatura = 1.83
estatura_entera = int(estatura) # Convierte a int truncando los decimales. Resultado: 1
```

## 🎯 Ejercicios Prácticos
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Mi tarjeta de Presentación
Crea tres variables: una para tu `nombre`, otra para tu `edad` (debe ser un entero) y otra para tu `pais`. Luego, usa tres funciones `print()` diferentes para mostrar cada valor en la consola.

### 🔹 Ejercicio 2: El cambiazo de variables
Declara una variable llamada `juguete_favorito` y asignale el texto `"Pelota"`. En la siguiente línea de codigo, cambia el valor de esa misma variable a `"Consola de videojuegos"`. Imprime la variable antes y después del cambio para ver cómo se actauliza la memoria.

### 🔹 Ejercicio 3: Investigando Tipos
Crea cuatro variables con los siguientes valores exactos: `100`, `12.5`, `"Python"` y `True`. Utiliza `print(type(...))` para mostrar en la consola de qué tipo exacto es cada una de las variables que has creado.

### 🔹 Ejercicio 4: Conversión de Estaturas
Declara una variable llamada `estatura_float`  con el valor `1.75` (un decimal). Crea una nueva variable llamada `estatura_int` que converta ese decimal a un núero entero usando la función `int()`. Imprime `estatura_int` y observa qué pasa con los decimales.

### 🔹 Ejercicio 5: El Contador incremental
Crea una variable llamada `contador` con el valor inicial de `0`. Incrementa su valor en `1` (pista: `contador = contador +1`). Luego, vuelve a incrementarlo sumándole `5` más. Finalmente, multiplica su valor total por `2` e imprime el resultado final en la consola (debería darte `12`).

