# 🔪 Lección 3: Slicing (Rebanado) de Strings en Python
En python, los strings son secuencias indexadas de caracteres. Esto significa que cada letra ocupa una posición fija con un número (índice). El **Slicing** es la técnica que nos permite extraer caracteres sueltos o "rebanar" un trozo entero de un texto usando los corchetes `[]`.

## 🗺️ 1. El Mapa de Índices (Positivos y Negativos)
Imagina la palabra `"PYTHON"`. Python le asigna dos mapas de coordenadas automáticos:
* **Índices Positivos (De izquierda a derecha):** Empieza en `0`.
* **Índices Negativos (De derecha a izquierda):** Empieza en `-1` (ideal para pillar las últimas letras sin saber cuánto mide el texto).

---

## ✂️ 2. La Fórmula Mágina del Slicing
Para cortar un string, abrimos corchetes tras la variable y usamos hasta tres parámetros separados por dos puntos `:`.

$$\text{variable}[\text{inicio} : \text{fin} : \text{paso}]$$

* **`inicio`**: El índice donde empieza el corte (se incluye). Si se deja vacío, Python asume que empieza desde el principio (`0`).
* **`fin`**: El índice donde termina el corte (**¡OJO! Este no se incluye**, se queda una casilla antes). Si se deja vacío, llega hasta el final.
* **`paso`**: Cada cuántas letras va dando saltos (por defecto es `1`).

### 💡 Ejemplos Rápidos con `texto = "PYTHON"`
* `texto[0]` -> `"P"` (Letra suelta).
* `texto[0:2]` -> `"PY"` (Corta desde el índice 0 hasta el anterior al 2). 
* `texto[:4]` -> `"PYTH"` (Desde el principio hasta el anterior al 4). 
* `texto[2:]` -> `"THON"` (Desde el índice 2 hasta el final) 
* `texto[::-1]` -> `"NOHTYP"` (El truco maestro: paso negativo lee el texto al revés).

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1:
Dada la variable palabra = "PROGRAMACIÓN":
1. Extrae e imprime la primera letra usando un índice positivo.
2. Extra e imprime la primera letra usando un índice negativo.
### 🔹 Ejercicio 2:
En tu tienda online, los productos tecnológicos empiezan siempre por el prefiojo "TEC-". Dado el siguiente código de barras en texto: "TEC-84729" Usa slicing para extraer ÚNICAMENTE las tres letras del prefijo (sin el guion) y muéstralo por pantalla.
### 🔹 Ejercicio 3:
Tenemos la siguiente cadena de texto confidencial: "TOKEN_secret123_END". Necesitamos aislar el secreto central. Usa slicing con los índices correctos para extraer solo el texto "secret123" (sin los guiones bajos) e imprimelo.
### 🔹 Ejercicio 4:
Dada la cadena de texto "A1B2C3D4E5", queremos deshacernos de los números y quedarnos solo con las letras ("ABCDE"). Aplica la fórmula del slicing usando el tercer parámetro (paso) para ir saltando los números e imprime el resultado limpito.
### 🔹 Ejercicio 5:
El Slicing en Python guarda un truco legendario para dar la vuelta a una palabra sin usar bucles. Dada la palabra "radar", usa el slicing inverso para guardarla del revés en una nueva variable. Imprime el resultado y comprueba si se lee igual (palíndromo).