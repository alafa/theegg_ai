# Tarea 22: El lechero

## Eunciado
Cómo ya recordamos en alguna otra tarea la definición de google un algoritmo es: "Un conjunto
ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la solución de un tipo de
problemas".
En esta tarea debes desarrollar (en el lenguaje o lenguajes de programación que tú quieras) el siguiente
algoritmo:
Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.


***Entrada:*** Número total de vacas que están a la venta.

***Entrada:*** Peso total que el camión puede llevar.

***Entrada:*** Lista de pesos de las vacas.

***Entrada:*** Lista de la producción de leche por vaca, en litros por día.

***Salida:*** Cantidad máxima de producción de leche se puede obtener.


[Fuente del reto](http://www.nachocabanes.com/retos/reto.php?n=07)

## Soluciones

Se proponen dos soluciones a este problema: La solución recursiva y la solución programación dinámica.

Las dos soluciones están descritas en sus respectivos READMES dentro de sus directorios.


## Ejecutables

El proyecto entero está desarrollado con Python 3.6.4

Hay tres ejecutables. Uno por cada solución sugerida y que se encuentran en sus perspectivos directorios.
Las instrucciones de ejecución de cada uno de forma independiente se encuentran en los readmes propios.

Existe un tercer ejecutable *runtimes.py* que, dados unos casos prestablecidos, ejecuta ambas soluciones y devuelve los tiempos que han tardado en ejecutarse.
Para así poder comparar el rendimiento de cada solución.

Ir en la terminal al directorio donde se encuentra este README.md y ejecutar comando `python runtimes.py` en la terminal para ver los resultados del rendimiento de cada solución.

## Conclusiones

La solución de la programación dinámica es mucho más rápido. Especialmente para aquellos casos donde entran muchas vacas en juego.

Los factores que pueden afectar al rendimiento de la solución dinámica son:
- Aumento de los valores únicos en los pesos de las vacas.
- La diferencia de peso entre la vaca más ligera y la más pesada.


La situación real determinará que solución que conviene utilizar.