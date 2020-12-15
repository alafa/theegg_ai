# Análisis del rendimiento de las aplicaciones de IA

La suma de los n primeros números se puede calular o bien sumando todos uno a uno o aplicando la fórmula de la suma aritmética de Gauss.

Se pide escribir el código para ambas formas y ejecutarlas de forma que se calcule la suma de los n primeros números de las
dos maneras diferentes para comparar tiempos de computo.

Se hará para 4 valores diferentes de n:
1) n= 1 000 000
2) n= 10 000 000
3) n= 100 000 000
4) n= 1 000 000 000

# Solución

La función `suma_lineal(n)` es la que va a sumar cada elemento uno a uno y por tanto, tendrá que hacer tantas operaciones
como grande sea el número de entrada. Es decir, tiene una notación O lineal.

La función `suma_constante(n)` simplemente aplica la formula de Gaus al número N, que sin importar lo grande que sea, siempre
será una única operación. Por esta razón, tiene una notación 0 constante.

Cuando ejecutamos el programa desde la terminal con `python main.py` podemos ver como la eficiencia de cada una de las formas
queda reflejada en el tiempo que tardan en ejecutarse.

![result](https://github.com/alafa/theegg_ai/blob/master/tarea_44/images/exec.png?raw=true)

La función `suma_constante(n)` se ejecuta practicamente de forma instantanea sin importar el valor de N. En cambio, vemos
que la función `suma_lineal(n)` tarda más a N más grande.

Si visualizamos los tiempos de ejecución de  `suma_lineal(n)` vemos:

![result](https://github.com/alafa/theegg_ai/blob/master/tarea_44/images/graph1.png?raw=true)

La razón por la que no vemos un incremento constante a medida que crece N es porque N cada vez se ha multiplicado por 10.
Es decir, N no ha crecido linealmente.

Pero si colocamos en el eje X el valor de N de forma que esté alejada una de la otra a la distancia que le correspondería:
![result](https://github.com/alafa/theegg_ai/blob/master/tarea_44/images/graph2.png?raw=true)

¡Voila! Aquí sí que podemos comprobar visualmente como el tiempo de ejecución a crecido exponencialmente.


# Ejecución

El proyecto está desarrollado con Python 3.7.3

Se debe ejecutar `python main.py` para lanzar el script.