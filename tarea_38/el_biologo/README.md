# Resolución de más algoritmos

Se presentan tres algoritmos. Para cada solución hay que presentar un diagrama de flujo y el código correspondiente.

## El Biólogo

Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C), guanina (G) y timina (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño que se encuentra en ambas formas de vida.

http://www.nachocabanes.com/retos/reto.php?n=005

### Algoritmo utilizado

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram1.jpg?raw=true)
![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram2.jpg?raw=true)
![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/el_biologo/diagramas/diagram3.jpg?raw=true)



# Ejecución

El proyecto está desarrollado con Python 3.7.3

`python main.py ctcgcccgcttggcgct cggctgcggctcgctcgctcg`