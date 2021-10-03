# Algoritmos de búsqueda

Tenemos la siguiente lista de elementos: [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].

1.- Construye tu propio algoritmo para ordenarlo de menor a mayor.

2.-Busca el número 874 utilizando el algoritmo secuencial y el binario. En cada iteración se debe sumar +1
de modo que al final del programa se debe indicar el número de iteraciones realizadas por cada
algoritmo hasta encontrar el elemento.

3.- Realiza el análisis en Notación Big O (visto en la tarea #44) y describe tu conclusiones en un
documento de texto

# Resolución 

El código de los algoritmos se ha desarrollado en las clases de Python que llevan su nombre:
- Algoritmo de ordenación Quicksort: `quickSort.py`
- Algoritmo de búsqueda binaria: `binarySearch.py`
- Algoritmo de búsqueda lineal: `linealSearch.py`

Los ejercicios se han resuelto en los notebooks presentes en este directorio importando las clases mencionadas anteriormente.

# Conclusiones

La búsqueda binaria necesita tener una lista ordenada para poder ser aplicada. Si no se tiene garantia de que la lista esté ordenada habrá que aplicar previamente un algoritmo de ordenación, lo que necesariamente va a resultar en un aumento de la cumplejidad de aplicar el algoritmo de la búsqueda binaria. Cúanto aumenta dependerá del algoritmo de ordenación elegido, que en este caso ha sido Quicksort.

Los resultados muestran que tanto la búsqueda lineal como la búsqueda binaria presentan una complejidad lineal O(n). Al menos, utilizando el algoritmo de ordenación Quicksort para la búqueda binaria.

Para listas no ordenadas es más optimo utilizar el algoritmo de búsqueda lineal aunque tampoco hay muchísima diferencia entre los dos. Eso sí, para listas que están ya previamente ordenadas es mucho más optimo aplicar la búsqueda binaria, especialmente en auquellos casos en los que la lista tiene muchos elementos.

