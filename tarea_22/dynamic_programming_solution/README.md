# Programación dinámica

La programación dinámica es un algoritmo que se utiliza para resolver problemas del tipo "Knapsack problem" (o problema de la mochila).

[Más información sobre el problema de la mochila.](https://es.wikipedia.org/wiki/Problema_de_la_mochila)

El procedimiento/algoritmo consiste en ir apuntando en un grid la mejor opción según se van añadiendo objetos (en este caso vacas).

El procedimiento se realiza, además para el peso máximo permitido, para todas las posibilidades de peso máximo restante permitido que se pudiera dar.

## Diagrama de flujo

![diagrama de flujo](https://drive.google.com/uc?export=view&id=16hdSh4E-EGlvr_Ksx4gZUUxz1pI1zDBJ)

## Paso a paso

### La pizarra

La pizarra es la chuleta en la que vamos a ir apuntando la mejor solución en diferentes situaciones.

#### Las columnas en la pizarra

Las columnas son diferenes valores posibles que puede tener la mochila (o camión) de capacidad (en nuestro caso kilogramos).
Cuando el camión está vacio, su capacidad restante es igual al peso máximo permitido pero está va a disminuir a medida que metamos vacas en el camión.

Hay que recoger todos los valores posibles de esta capacidad restante del camión, ponerlos en orden de menor a mayor y asignarlos a las columnas de la pizarra.


Por ejemplo, si el peso máximo de nuestro camión es de 5kg las columnas de la pizarra podrían corresponder a los valores: 1kg, 2kg, 3kg, 4kg y 5kg.
#### Las filas en la pizarra

Por cada fila que vamos bajando de la pizarra, una nueva vaca entra en juego. La primera fila (posición cero) corresponde a la situación en la que no hay ninguna vaca que elegir, la segunda fila corresponde a la sitiación en la que tenemos una vaca que elegir, la segunda fila corresponde a la situación en la que tenemos la vaca anterior y otra más para elegir, y así sucesivamente.

#### Preparar e inicializar la pizarra

Lo primero que hay que hacer es generar las columnas. Se podría hacer empezando desde 1 e incrementar por 1 hasta alcanzar la capacidad máxima original pero para valores muy altos de capacidad, no sería lo más óptimo ya que muchos de esos valores no garían falta.
Lo que se propone en este desarrollo es coger el mayor común divisor de los pesos de las vacas y que sea ese el incremento desde uno hasta la capacidad máxima.

También, otra cosa que se hace en la inicialización es crear ya la primera fila (posición cero) donde no hay vacas que elegir, por tanto la solución para cada celda va a ser 0 litros.

#### Evolución de la pizarra

En el programa principal hay dos loops.
El primero que recorre las filas y otro que recorre las columnas. Por cada celda se apunta en la pizarra la mejor opción que se tiene para cada capacidad correspondiente (columna) y para cada selección de vacas donde podemos elegir.

La mejor opción para cada celda siempre va a ser una entre dos:
A) La anterior mejor opción de la misma columna + La vaca nueva a considerar (si cabe)
o
B) La vaca nueva a considerar (si cabe) + la mejor solución de la misma fila y de la columna correspondiente al espacio restante (la capacidad menos el peso de la vaca nueva a considerar en esta fila)

#### Ejemplo de pizarra

Aqui un ejemplo muy básico de como quedaría la pizarra después de resolver una situación en la que tenemos dos vacas y un camión que soporta 30kg.

![Ejemplo pizarra](https://drive.google.com/uc?export=view&id=1nZfNgDUIOZYsn2YhdigJXTJ9Bieri92T)


## Ejecución

Ir en la terminal al directorio donde se encuentra este README.md y ejecutar en la terminal el siguiente comando:
 
`python app.py` seguido de los argumentos:

***Arg. 1*** Número total de vacas que están a la venta.

***Arg. 2*** Peso total que el camión puede llevar.

***Arg. 3*** Lista de pesos de las vacas.

***Arg. 4:*** Lista de la producción de leche por vaca, en litros por día.
 
 Ejemplo:
`python app.py 3 100 50,60,10 7,8,2`
