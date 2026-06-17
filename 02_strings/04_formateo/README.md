# 📊 Lección 4: Formateo de Strings en Python
A lo largo de la historia de Python, han existido diferentes maneras de meter variables dentro de un texto. Aunque hoy en día usamos f-strings por comodidad, un buen programador debe conocer todos los estilos para entender código antiguo y controlar cómo se muestran los números (decimales, monedas, etc.).

---

## 🏛️ 1. La Evolución del Formateo (Los 3 Estilos)
### 🦖 Estilo Dinosaurio (Operador `%`)
Heredado del lenguaje C. Usa marcadores de posición según el tipo de dato (`%s` para texto, `%d` para enteros).
```python
"Hola %s, tienes %d años" % ("Tu nombre", 23)
```

### Estilo dinosaurio-Moderno (Método .format())
Introducción en Python 3. Usa llaves vacías `{}` como comodines y luego pasa las variables en orden al final.
```python
"Hola {}, tienes {} años".format("Tu nombre",35)
```

### Estilo Futurista (Actual: f-strings)
El estandar acutal desde Python 3.6. Más rápido, limpio y directo.
```python
f"Hola {nombre}, tienes {edad} años"
```

## 🎯 2. Formateo Numérico Avanzado (Trucos de precisión)
Dentro de las llaves `{}` de las f-strings (y del `.format()`), podemos usar los dos puntos `:` para aplicar superpoderes visuales a los números:
* **Redondear decimales (`:.2f`):** Limita los decimales a la cantidad que le pidas (la `f` significa float).
    * `f"{3.14159:.2f}"` -> `3.14`
* **Relleno con ceros (`03d`):** Añade ceros a la izquierda hasta cumplir la longitud deseada.
    * `f"{7:03d}"` -> `007`

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: El Arqueólogo del Código
Te han contratado para actualizar un script del año 2010. Te encuentras con esta línea que usa el viejo operador `%`: 
* `mensaje = "Usuario: %s | Intentos: %d" % (nombre, intentos)`
Declara las variables nombre = "admin e intentos = 3, y reescribe ese mensaje usando una f-string moderna.
### 🔹 Ejercicio 2: El Método Clásico
Aunque las f-strings son mejores, el método `.format()` se sigue usando muchísimo. Dadas las variables: `ciudad = "Madrid"` y `tem = 24`. Construye la frase: `"La temporada en Madrid es de 24 grados."` usando EXCLUSIVAMENTE el método `.format()` con sus llaves `{}` vacías.
### 🔹 Ejercicio 3: Control de Decimales
Estás calculando el precio de una porción de tarta y la división te devuelve un número con demasiados decimales: `precio = 4.333333`. Muestra por pantalla el precio final usando una f-string, pero aplicando el formateo necesario para que SOLO se muestren 2 decimales y el simbolo `€`.
### 🔹 Ejercicio 4: Códigos de Factura con Ceros
En tu sistema de facturación, los números de cliente deben tener siempre 4 dígitos. Si un cliente tiene el ID 7, la factura debe poner "0007". DDada la variable `id_cuenta = 54`, usa el formateo de f-strings para imprimir el ID formateado con ceros a la izquierda hasta cumplir los 4 dígitos.
### 🔹 Ejercicio 5: El Ticket de Compra II
Queremos pintar un miniticket en la consola donde el nombre del producto ocupe exactamente 15 caracteres (alineado a la izquierda) y el precio ocupe 6 caracteres (alineado a la derecha).
Prueba a usar los modificadores de alineación `<` y `>` dentro de una f-string para maquetar estas dos líneas y que queden perfectamente en columna:
* Producto: "Pan", Precio: 1.25
* Producto: "Manzanas", Precio: 3.40