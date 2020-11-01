## Palíndromos

Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras. Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. Usted debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.

Por ejemplo, si N es 31, entonces la respuesta es 101.

Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.

Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.


http://www.nachocabanes.com/retos/reto.php?n=008

### Solución planteada

Aquí quedan tres funciones diferenciadas muy claras. Una, la que se encarga de encontrar el número más pequeño a partir
del número proporcionado que cumpla las condiciones que nos piden. Otra que chequea si es un número palíndromo y otra que
chequee si es un número primo.

La función general simplemente itera hasta encontrar un número que cumpla las dos condiciones. Empezando por el número
que se proporciona, en cada vuelta incrementa uno el valor y chequea si se cumples las dos condiciones.

Es importate que chequee primero si es palindromo antes de si es primo, ya que la función `check_if_prime(num)` es más costosa
que la función `check_if_palindromo()` y si ya no se cumple esta, nos ahorramos el comprobar si es primo. Lo que hace que el programa
sea mucho más rápido en casos de números altos.


![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/primos_y_palindromos/diagramas/diagram.jpg?raw=true)

La función que comprueba si el número es palindromo simplemente convierte el número a string y recorre el número desde
sus extremos hasta el centro y en el momento que se encuentra que los valores situados en 
las posiciones `i` y `len(num_str)-1` no son iguales, devuelve `False`. Si termina las iteraciones y no ha devuelto nada, entonces
es que trata de un número palindromo y devuelve `True`.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/primos_y_palindromos/diagramas/diagram3.jpg?raw=true)

La función que comprueba si es un número primo va comprobando si el resto de la operacion de dividir el número por otro da cero.
Este número por el que divide empieza en 2 y se va incrementando en uno cada iteración.
En el momento que al dividir el número por otro el resto da cero, se puede afirmar que el número no es primo y se devuelve `False`.
Si el número divisor que se va incrementando en cada iteración alcanza el valor de nuestro número original, se puede afirmar
que es un número primo porque no se ha encontrado ningún otro número que el resto dé cero al dividirlo por él, y se devuelve `True`.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/primos_y_palindromos/diagramas/diagram22.jpg?raw=true)

# Ejecución

El proyecto está desarrollado con Python 3.7.3

Ejecutar `python main.py /numero/` en la terminal para encontrar un número palindromo y primo mayor o igual al número
proporcionado como argumento.

Por ejemplo, ejecutar `python main.py 456789` para encontrar en siguiente número palindromo y primo mayor que 456789.