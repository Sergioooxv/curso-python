# 🔍 Lección 5: Expresiones Regulares (Regex) en Python
Una **Expresión Regular** (o *Regex*) es una secuencia de caracteres que forma un **patrón de búsqueda**. Imagina que es un "buscar y reemplazar" de Word, pero con esteroides. En lugar de buscar una palabra exacta, puedes buscar patrones como: "un número de 9 dígitos que empiece por 6", "un correo electrónico" o "una matrícula".

En Python, para usar Regex necesitamos importar el módulo nativo **`re`**.

---

## 🗺️ 1. Los Superpoderes de la Tabla Regex (Metacarácteres)
Para construir nuestros patrones, usamos comodines especiales:

| Símbolo | Qué significa | Ejemplo |
| :--- | :--- | :--- |
| `\d` | Cualquier **dígito** (número del 0 al 9) | `\d\d\d` (Busca 3 números seguidos) |
| `\w` | Cualquier carácter **alfanumérico** (letras o números) | `\w\w` (Busca 2 letras/números) |
| `+` | Que el elemento anterior se repite **1 o más veces** | `\d+` (Busca un bloque de números enteros) |
| `{n}` | Que se repite exactamente **n veces** | `\d{4}` (Busca exactamente 4 números, ej: un año) |

---

## 🛠️ 2. Las 3 Funciones Clave del Módulo `re`
1. **`re.search(patron, texto):`** Busca si el patrón existe en *cualquier parte* del texto. Devuelve un objeto si lo encuentra o `None` si no.
2. **`re.match(patron, texto):`** Busca el patrón *únicamente al principio* de la cadena de texto.
3. **`re.findall(patron, texto):`** Busca *todas* las coincidencias en el texto y te las devuelve ordenadas en una **lista de Python**.

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: El Detector de Teléfonos
Queremos verificar si un usuario ha introducido un número de teléfono válida en nuestro formulario. En España los móviles tienen 9 digitos. Importa el módulo 're', define el patrón correcto para buscar 9 números seguidos ('\d') y comprueba si la variable 'telefono' lo cumple usando 're.search()'.
### 🔹 Ejercicio 2: Cazados de Emails
vamos a validar la presencia de un correo. Un email básico se compone de texto alfanumérico ('\w+'), una arroba '@', y más texto. Usa 're.search()' para verificar si la variable 'correo' contiene una estructura válida e imprime un mensaje de confirmación en consola.
### 🔹 Ejercicio 3: Extracción de Precios
Un sistema automático ha extraído este texto de una web: "El menú cuesta 15 euros, la bebida son 3 euros y el postre 5 euros". Utiliza la función 're.findall()' junto con el patrón adecuado para extraer ÚNICAMENTE los números sueltos y guardarlos en una lista. Imprime la lista.
### 🔹 Ejercicio 4: Censura de Datos Confidenciales
En los logs de tu servidor se ha filtrado este texto sensible: "El cliente pago con la tarjeta 1234-5678-9012-3456 en la web". Investiga o utiliza la función 'res.sub()' para buscar el patrón de los 16 dígitos de la tarjeta (separados por guiones si quieres, o directamente) y reemplázalos por la palabra "[Censurado]" antes de mostrar el texto por pantalla.
### 🔹 Ejercicio 5: El Validador de Matrículas
Las matrículas actuales en España constan de 4 números seguidos de 3 letras mayúsculas (ejemplo: 1234FGH"). Crea un patrón estrícto usando '{4}' y '{3}' y comprueba si la variable 'matricula_coche' cumple con el estandar oficial de tráfico.