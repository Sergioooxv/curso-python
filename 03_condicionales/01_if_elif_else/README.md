# 🚦 Bloque 3: Estructuras de Control - Condicionales
En programación, el código por defecto se ejecuta de arriba a bajo, de forma secuencial. Sn embargo, para crear programas inteligentes (como un control de acceso, un carrito de compra o un videojuego), necesitamos que el programa **tome decisiones** en tiempo real. Los condicionales nos permite abrir "Bifurcaciones" en el camino: si una condición se cumple, el programa va por la izquierda; si no se cumple, va por la derecha.

---

## 🔑 1. El Concepto de Indentación (El talón de Aquiles de Python)
A diferencia de lenguajes como JavaScript, C++ o Java (que usan llaves `{}` para encerrar bloques de código), Python utiliza la **indentación** (los 4 espacios de tabulacion).
* La línea que inicia el condicional siempre termina con dos puntos (`:`).
* Todo lo que esté "un paso hacia adentro" (tabulado) pertenecerá a ese bloque condicional.
* En el momento en que vuelves al margen izquierdo, sales del condicional.

> ⚠️ **Error de Novato:** Si olvidas tabular el código dentro de un `if`, Python lanzara un error de tipo `IndentationError` y detendrá el programa.

---

## ⚖️ 2. Los Operadores de Comparación (Los Jueces)
Para que un condicional funcione , necesita una condición que evalúe a `True` (Verdadero) o `False` (Falso). Para ello usamos los operadores relacionales:

| Operador | Significado | Ejemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `==` | **Igual a** (No confundir con `=` de asignar) | `"admin" == "admin"` | `True` |
| `!=` | **Diferente de** (No es igual) | `5 != 3` | `True` |
| `>` | **Mayor que** | `10 > 20` | `False` |
| `<` | **Menor que** | `18 < 25` | `True` |
| `>=` | **Mayor o igual que** | `18 >= 18` | `True` |
| `<=` | **Menor o igual que** | `12 <= 10` | `False` |

---

## 🗺️ 3. Mapa de Ruta de este Bloque
Navegaremos a través de las 4 subcarpetas de tu directorio para dominar la toma de decisiones:
1. **`01_if_elif_else`**: La estructura básica y las decisiones encadenadas cuando hay múltiples opciones exclusivas.
2. **`02_operadores_logicos`**: Cómo combinar varias condiciones en una sola línea usando `and` (Y), `or` (O) y `not` (NO).
3. **`03_operador_ternario`**: El arte de escribir un `if-else` simple en una única línea de código para hacer asignaciones ultra rápidas.
4. **`04_match_case`**: La estructura moderna (introducida en Python 3.10) que sustituye a los `if-elif` infinitos cuando evaluamos una misma variable frente a muchos valores fijos.