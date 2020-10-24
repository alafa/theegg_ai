## El Biólogo

Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el 
objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), 
guanina (G) y timina (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida.

Fuente original: http://www.nachocabanes.com/retos/reto.php?n=005

### Solución planteada

Después de leer los parámetros de entrada, que serán nuestras dos strings a comparar (s1 y s2), se aplica la función
`get_comparable_strings(s1, s2)` que, como ya veremos en detalle más adelante, se encarga de devolver pares de strings del
 mismo tamaño. Se itera por cada par de strings devuelto por la función anterior y a cada par se le aplica la función
 `common_string(one_pair)` para hallar el substring común de máxima longitud entre los dos strings.
 
 Por cada par de strings, se va guardando en un registro, cúal ha sido el susbtring con mayor longitud. Este será,
 al final del programa, lo que se imprimirá por pantalla.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram1.jpg?raw=true)

Vamos a ver más en detalle las funciones `get_comparable_strings(s1, s2)` y  `common_string(one_pair)`:

La primera, se encarga de devuelve un _generator_. Un generator, en Python, es una estructura iterable que se va generando
bajo demanda. Esto quiere decir que no se carga entero en la memoria RAM si no que se genera según se necesite.
Es recomendable usar este tipo de estructuras en vez de una lista o tupla cuando puede contener mucha información y ser
demasiado pesado para la memoria RAM de la máquina.


Lo primero que hace esta función es identificar que string es el largo y cual el corto (y si son iguales, indistintamente).
Una vez esto hecho, existen tres fases: "La de entrar", "la de desplazarse dentro" y "la de salir".

Vamos a verlo paso a paso:

Tenemos dos strings s1 y s2. S1 tiene una longitud de 6 y s2 de 4.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair1.png?raw=true)

**FASE 1: Entrar**

Tenemso al string más largo fijo y vamos a ir introduciendo desde la cabeza al string más corto. Por lo que en la primera
iteración tenemos:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair2.png?raw=true)

Nuestros par de strings son: (c1) y (c4)

En la siguiente iteración, introducimos una posición más s2 en s1 y nos queda que:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair3.png?raw=true)

Nuestros par de strings son: (c1, c2) y (c3, c4)

Volvemos a introducir una posición más:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair4.png?raw=true)

Ahora nuestros par de strings son: (c1, c2, c3) y (c2, c3, c4)

Aún queda una posición de s1 que introducir. Lo hacemos y nos queda:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair5.png?raw=true)

Nuestros par de strings son: (c1, c2, c3, ,c4) y (c1, c2, c3, c4)

Vale. Fin de la fase de entrar, porque s2 ha entrado completamente en s1.

**FASE 2: Desplazamiento**

En esta fase s2 se va a mover una posición en cada iteración dentro de s1.

Empezamos:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair6.png?raw=true)

En la primera iteración de la fase 2 nuestros par de strings son: (c1, c2, c3, c4) y (c1, c2, c3, c4)

Segunda iteración, se vuelve a desplazar una posición más:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair7.png?raw=true)

Nuestros par de strings son: (c3, c4, c5, c6) y (c1, c2, c3, c4)

Como s2 ya no se puede desplazar más posiciones dentro de s1, pasamos a la tercera y última fase.

**FASE 3: Salir**

La cabeza de s2 empieza a salir de s1. En la primera iteración de esta fase tenemos:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair8.png?raw=true)

Nuestros par de strings son: (c4, c5, c6) y (c1, c2, c3)

Avanzamos otra posición más:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair9.png?raw=true)

Nuestros par de strings son: (c5, c6) y (c1, c2)

Solo nos queda una posición más para que s2 salga completamente de s1:

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair10.png?raw=true)

Nuestros par de strings son: (c6) y (c1)

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram2.jpg?raw=true)


Todas las parejas de strings que se han devuelto recogen todas las posibilidades en las que podemos encontrar un string común.
La función `common_string(one_pair)` se encarga de analizar cada una de estas parejas de strings y devolver su string común.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram3.jpg?raw=true)



# Ejecución

El proyecto está desarrollado con Python 3.7.3.

Ejecutar comando `python main.py /string1/ /string2/`
en la terminal para ejecutar el programa.

Por ejemplo:
`python main.py ctcgcccgcttggcgct cggctgcggctcgctcgctcg`