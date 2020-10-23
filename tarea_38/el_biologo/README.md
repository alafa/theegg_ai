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

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/pair1.jpg?raw=true)


![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram2.jpg?raw=true)
![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram3.jpg?raw=true)



# Ejecución

El proyecto está desarrollado con Python 3.7.3

`python main.py ctcgcccgcttggcgct cggctgcggctcgctcgctcg`