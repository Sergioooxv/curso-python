# 🛠️ Lección 2: Métodos de String en Python
En Python, los textos son objetos inteligentes. Eso significa que vienen equipados de fábrica con funciones integradas especiales llamadas **métodos**. Un método es una acción que puedes ejecutar *sobre* el propio texto usando la sintaxis del punto (`.nombre_metodo()`).

---

## 🔝 1. Métodos de Caja (Mayúsculas y Minúsculas)
Ideales para normalizar textos antes de guardarlos en una base de datos o compararlos.
* `texto.upper()` -> Convierte TODO el texto a **MAYÚSCULAS**
* `texto.lower()` -> Convierte TODO el texto a **minúsculas**
* `texto.capitalize()` -> Pone la **Primera letra en mayúscula** y el resto en minúscula
* `texto.title()` -> Pone en **Mayúsculas La Primera Letra De Cada Palabra** (formato titulo).

---

## 🧹 2. Métodos de Limpieza y Modificación
Es muy común que los usuarios dejen espacios sin querer o cometan errores al teclear. Aquí tienes tus herramientas de cirujano:
* `texto.strip()` -> Elimina todos los **espacios en blanco sobrantes**  al principio y al final del texto.
* `texto.replace("antiguo","nuevo")` -> Busca un fragmento de texto y lo **remplaza** por otro por completo.

---

## 📊 3. Métodos de Búsqueda y Verificación
Siven para interrogar al texto y obtener información sobre su contenido.
* `texto.count("letra")` -> **Cuenta cuántas veces** aparece una letra o palabra dentro del string.
* `texto.find("texto")` -> Busca la posición (indice) de un texto. Si no lo encuentra, devuelve `-1`
* `texto.startswith("Hola")` -> Devuelve `True` o `False` si el texto **empieza** por esa cadena.
* `texto.endswith(".pdf")` -> Devuelve `True` o `False` si el texto **termina** por esa cadena (ideal para validar archivos).

> ⚠️ **¡Regla de Oro Inmutable!** Los strings en Python son **inmutables**. Esto significa que ningún método modifica el texto original. Métodos como `.upper()` o `.replace()` calculan el resultado y te devuelve una **copia nueva**. Si quieres conservar los cambios, debes reasignar la variable: `texto = texto.upper()`.

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Normalización de Nombres
Un usuario se ha registrado en tu web y ha escrito su nombre lleno de espacios y mal formateado: "    sErGiO raMoS     ". Crea un programa que limpie los espacios de los extremos y lo transforme para que quede en formato de nombre propio limpio: "Sergio Ramos".
### 🔹 Ejercicio 2: Censor de Palabrotas
En el chat de un videojuego queremos censurar la palabra "tonto". Dada la siguiente frase, usa un método de string para cambiar esa palabra por asteríscos "*****" e imprime la frase censurada resultante.
### 🔹 Ejercicio 3: El Analizador de Texto
Pide al usuario que escriba una frase larga por teclado. El programa debe calcular y mostrar de forma automática:
    1. Cuántas veces aparece la letra 'a' (independientemente de si es 'A' o 'a').
    2. Cuántos caracteres en total tiene la frase (pista: usa una función que ya conoces).
### 🔹 Ejercicio 4: Validador de Archivos Seguros
Un usuario intenta subir un documento a tu plataforma. Pide por teclado el nombre del archivo (ej: "factura.pdf", "foto.png"). Usa el método de verificación adecuado para comprobar si el archivo termina en ".pdf" y muestra un resultado booleano (True/False).
### 🔹 Ejercicio 5: El Detective de Buscador
Tenemos la base de datos de un periodico con la siguiente noticia: "El precio del bitcoin bate un nuevo récord histórico este mes." Usa un método para averiguar en qué posición exacta (índice) empieza la palabra "bitcoin". Imprime ese indice numérico por pantalla.
