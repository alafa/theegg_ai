# Diccionario

## Búsqueda binaria

Es un algoritmo de búsqueda de un elemento numérico en una lista ordenada.
Se empieza buscando en la posición situada en la mitad de la lista y en caso de no coincidir, se buscará en la primera o segunda mitad
de la lista según el número encontrado sea mayor o menos al que tenemos que encontrar.

De esta forma, la complejidad del algoritmo es mucho menos con respecto al de la búsqueda secuencial. Eso sí, si no tenemos una lista ordenada en primer lugar
habrá que contar también con ello.

## Búsqueda secuencial

Es un algoritmo de búsqueda de un elemento en una lista que consiste en recorrer la lista elemento a elemento hasta dar con el elemento que se busca. 
Si llega al final de la lista y no lo ha encontrado, significa que el elemento no está en la lista.

Aunque es un algoritmo sencillo de implementar, no es muy eficiente ya que la complejidad crece linearmente según se hace más grande la lista.

## Notación Big-O

También conocido como notación asintótica o anotación Landau.
Es una anotación que indica el nivel de complejidad de un algoritmo. Explica en qué manera crece el tiempo de ejecución al aumentar el tamaño del input. Puede quedarse igual o ser lineal, exponencial.. etc.

Se tiene en cuenta la componente del algoritmo que más afecta al rendimiento y se desprecian las demás.





