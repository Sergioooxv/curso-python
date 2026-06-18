# 🔀 Lección 2: Operadores Lógicos (`and`, `or`, `not`)
Los operadores lógicos nos permiten combinar varias condiciones de comparación en una sola sentencia. Son los bloques de construcción esenciales para crear reglas de negocio complejas sin llenar nuestro código de escaleras infinitas de `if` anidados.

---

## 🗺️ 1. Los 3 Operadores del Motor de Python
### 🤝 A) El Operador `and` (Exigente)
Para que todo el bloque sea Verdadero (`True`), **TODAS** las condiciones individuales tienen que cumplirse. Con que una sola falle, todo se desmorona.
* *Ejemplo:* Para becar a un alumno necesita: `nota >= 9` **and** `renta_baja == True`.

### 🔀 B) El Operador `or` (Permisivo)
Para que el bloque sea Verdadero, **BASTA CON QUE UNA** de las condiciones se cumpla. Solo da Falso si absolutamente todas las condiciones fallan.
* *Ejemplo:* Para entrar a un concierto sirve: `tienen_entrada == True` **or** `es_lista_invitados == True`

### 🔄 C) El Operador `not` (Inversor)
Este operador le da la vuelta al valor booleano actual. Si algo es `True`, lo convierte en `False` y viceversa. Es ideal para evaluar estados de "apagado" o "ausencia".
* *Ejemplo:* `if not tiene_deudas:` (Si NO tiene deudas, avanza).

---

## 📊 2. Tabla de la Verdad Rápida

| Condición A | Condición B | A `and` B | A `or` B | `not` A |
| :---: | :---: | :---: | :---: | :---: |
| `True` | `True` | **`True`** | **`True`** | `False` |
| `True` | `False` | `False` | **`True`** | `False` |
| `False` | `True` | `False` | **`True`** | **`True`** |
| `False` | `False` | `False` | `False` | **`True`** |

---

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Aprobación de Hipoteca Bancaria
Un banco necesita automatizar el pre-análisis de hipotecas. Pide al usuario tres datos: 'ingresos_mensuales' (float), 'tiene_deudas' (booleando / Texto convertido) y 'antiguedad_laboral_meses' (int).

Reglas para conceder la Hipoteca (Debe Cumplir TODAS):
1. Los ingresos mensuales deben ser estrictamente superiores a 2500€.
2. NO debe tener deudas pendientes (usa el operador `not`).
3. La antiguedad laboral en su empresa debe ser mayor o igual a 12 meses.
Escribe una única condición combinada usando `and` y `not`
### 🔹 Ejercicio 2: Beca Universitaria (Combinando AND y OR)
Una universidad otorga becas si el alumno cumple el Criterio A o si cumple el Criterio B. Pide por consola: 'nota_media' (float) y 'distancia_km' (int) desde su casa a la facultad.
- Criterio A: Tener una 'nota_media' mayor o igual a 9.0 (independientemente de la distancia).
- Criterio B: Tener una 'nota_media' mayor o igual a 7.0  Y vivir a más de 50 km ('distancia_km > 50').

¡Ojo! Para agrupar condiciones y que el 'or' no rompa la prioridad mátemática, debes utilizar paréntesis '()' para aislar el bloque del Criterio B.
### 🔹 Ejercicio 3: Central de Alarmas Doméstica
Enunciado: Programamos el software de una alarma. Pide dos datos por consola:
'sensor_movimiento' (si/no) y 'sistema_activado' (si/no).

La alarma debe dispararse (imprimir "🚨 ¡ALERTA! Intruso detectado...") si:
- El 'sensor_movimiento' se activa (da True) Y el 'sistema_activado' NO está 
en modo mantenimiento (es decir, el sistema está encendido, True).

Si el sensor detecta movimiento pero la alarma estaba apagada, debe imprimir 
"Aviso silencioso: Movimiento detectado con alarma desactivada". En cualquier 
otro caso, imprimir "Sistema seguro". Usa operadores lógicos para resolverlo.
### 🔹 Ejercicio 4: Liquidación de Descuentos Black Friday
Enunciado: Un e-commerce aplica un 30% de descuento si se da alguna de 
estas condiciones corporativas:
- Que el cliente sea "VIP" Y realice la compra cualquier día de la semana.
- Que la compra se realice en el día "VIERNES" (sea VIP o no).
#
Pide al usuario la 'moneda_gasto' (float), si es 'es_vip' (si/no) y el 
'dia_semana' (texto). Si tiene descuento, calcula el nuevo precio. Si no, 
mantiene el original. Aplica 'and', 'or' y métodos de string.
### 🔹 Ejercicio 5: Firewall de Seguridad (EL GRAN DESAFIO COMBINADO)
Enunciado: Vamos a simular el cortafuegos de un servidor militar. 
- El acceso solo se concede si se cumple una de las siguientes dos grandes vías:
- Vía 1 (Superusuario): El 'usuario' es exactamente "root" y la 'clave' es "1234".
- Vía 2 (Usuario estándar verificado): El 'usuario' es un empleado dado de alta 
(cualquiera diferente a "root"), la 'clave' es correcta, la 'ip_permitida' 
es True Y además estamos dentro del 'horario_laboral' (True).
 Pide los datos necesarios y monta una estructura condicional robusta para 
#autorizar o denegar el acceso.