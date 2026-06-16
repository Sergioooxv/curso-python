# ✍️ Lección 5: Comentarios y Documentación en Python
Escribir código que funcione es solo la mitad del trabajo de un programador, la otra mitad es escribir código que los humanos puedan entender. En esta sección aprenderás a usar los comentarios para explicar el "porque" de tus decisiones y a dejar notas limpias sin alterar la ejecución de tu programa.

---

## 💬 1. Tipos de Comentarios en Python
Python ignora por completo los comentarios cuando ejecuta el programa, lo que te da total libertad para escribir en lenguaje humano.

### 🔹 A) Comentarios de una sola línea (`#`)
Se crean anteponiendo el símbolo de la almohadilla o hash. Todo lo que vaya a la derecha de ese simbolo es un comentario.
```python
# Esto es un comentario que explica la siguiente variable
precio = 99.9 # Tambiénse puede poner al final de una línea de código
```
### 🔹 B) Comentarios multilínea o Bloques (""")
Aunque Python técnicamente los procesa como cadenas de texto sin asignar (multiline strings), los desarrolladores los usamso para escribir explicaciones o párrafos que ocupan varias líneas sin tener que poner # en cada una.
```python
"""
Este es un bloque de comentario largo.
Ideal para explicar algoritmos complejos o dejar
Instrucciones detalladas de uso.
"""
```

## 🧠 2. Filosofía del Buen Programador
**💡 Regla de oro:** El buen código se explica a sí mismo; los buenso comentarios explican por qué lo hiciste, no qué hace el código.
* **Mal comentario (Evitalo):** `x = 10 #Guarda el número 10 en la variable x` (Esto es obvio, satura el código).
* **Buen comentario (Suma valor):** `tipo_cambio = 1.09 # Tasa oficial del BCE a fecha de junio 2026` (Aporta contexto real).

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Limpiando el Caos
El siguiente código funciona, pero es una masa de texto ilegible. Organizalo separándolo visualmente en 3 seccciones claras usando comentarios de una sola línea (#): "1. Configuración", "2. Cálculo" y "3. Resultado".
### 🔹 Ejercicio 2:
Este programa da un error al ejecutarse proque la variable 'numero_secreto' intenta sumar un texto. En lugar de borrar la línea rota, "comentala" para desactivarla y escribe una nueva línea abajo que sume el número correctamente como entero.
### 🔹 Ejercicio 3:
Cuando trabajas en una empresa, los scripts suelen llevar una cabecera con metadatos. Usa un bloque de comillas triples o múltiples almohadillas para crear una documentación al principio de este archivo que indique:
- Autor: Tu nombre
- Fecha: Fecha Actual
- Version: 1.0
- Proposito: Script básico de bienvenida.
### 🔹 Ejercicio 4:
El siguiente código calcula el precio de un producto con descuento, pero las variables tienen nombres pésimos (a,b,c). Añade comentarios al final de cada línea (inline_comments) explicando qué almacena matemáticamente cada variable para que otro humano pueda entenderlo.
### 🔹 Ejercicio 5:
El siguiente código esta sobresaturado de comentarios inútiles. Limpia el archivo borrando los comentarios molestos y dejando ÚNICAMENTE aquel comentario qeu de verdad aporte una información que no se vea a simple vista.