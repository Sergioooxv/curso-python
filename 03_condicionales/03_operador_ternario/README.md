# ⚡ Lección 3: El Operador Ternario (Condicionales en línea)
El operador ternario es una herramienta de optimización sintáctica (conocida como *Syntactic Sugar*). Nos permite evaluar una condición y asignar un valor a una variable en una única línea de código, sustituyendo el clásico bloque `if-else` de cuatro líneas.

---

## 🏗️ 1. Anatomía del Operador Ternario
A diferencia de otros lenguajes que usan los símbolos `?` y `:`, Python utiliza las propias palabra clave `if` y `else` en un orden que se lee de manera muy natural en inglés:

```python
variable = valor_si_true if condicion else valor_si_false

# Con if-else clásico (Enfoque Tradicional 4 Líneas)
if nota >= 5:
    resultado = "Aprobado"
else:
    resultado = "Suspenso"

# Con Operador Ternario (Enfoque Ternaio 1 línea)
resultado = "Aprobado" if nota >= 5 else "Suspenso"
```

## 🎯 Ejercicios Prácticos de este Bloque
Abre tu IDE favorito y vamos a programar!!
Recuerda que tienes la solución de cada ejercicio en su respectivo archivo, pero recomiendo que hagas y te peles con el código tu mismo vamos a programar.

### 🔹 Ejercicio 1: Validación de Estado de Pedido
Un comercio online ofrece envío gratuito si la compra supera los 50€. Si no la supera, el envío cuesta 4.90€. Pide al usuario el 'total_carrito' (float). A continuación, calcula el 'coste_envio' utilizando una ÚNICA LÍNEA con el operador ternario. Muestra por pantalla el coste del envío y el total absoluto.
### 🔹 Ejercicio 2: Control de Mayores de Edad para Web
Pide al usuario su 'edad' (int) por consola. Usa el operador ternario en una sola línea para guardar en una variable llamada 'estado' el texto "Acceso Autorizado" si tiene 18 años o más, o "Acceso Denegado" si es menor. Imprime el valor de la variable 'estado'.
### 🔹 Ejercicio 3: Configurador de Modo Oscuro
El sistema opeerativo de un móvil cambia su interfaz según la hora. Pide al usuario la 'hora_actual' (int, formato de 0 a 23). Aplica esta regla en una sola línea con operador ternario: Si la hora es mayor o igual a las 20 (8PM) o menor o igual a las 6 (6 AM), la variable 'modo_pantalla' debe ser "DARK". En cualquier otro horario, debe ser "LIGHT". Cruza operadores lógicos dentro del ternario.
### 🔹 Ejercicio 4: Validador de Estado de Rango Militar
En un videojuego de estrategia, un jugador recibe el rango de "Veterano" si sus 'puntos_experiencia' (int) superan los 5000 puntos. Si tiene 5000 o menos, su rango se mantiene en "Recluta". Pide por consola los 'puntos_experiencia' y, utilizando el operador ternario en una sola línea, asigna el texto correspondiente a la variable 'rango'. Imprime un mensaje elegante mostrando el resultado.
### 🔹 Ejercicio 5: El Calculador de Recargos por Pasarela  de Pago
Una tienda online cobra una comisión fija por gestión de 2.50€ si el cliente decide pagar con "PAYPAL". Si paga con "Tarjeta", la comisión es de 0.0€. Pide al usuario el 'importe_articulo' (float) y el 'metodo_pago' (texto). Usa el operador ternario en una sola línea para calcular la variable 'comision', asegurándote de sanitizar el método de pago con '.upper()'. Muestra en la terminal el desglose con el total final formateado.
