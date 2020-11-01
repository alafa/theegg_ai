## Invertir palabras

Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras. La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.

http://www.nachocabanes.com/retos/reto.php?n=002


### Solución planteada

El número de frases se recoge en el primer argumento. Se comprueba que es un número entero y se itera tantas veces como
el número que se haya indicado.
Para cada iteración, se pide al usuario una frase a introducir. Y por cada frase introducida, se guarda la frase
con el orden de palabras al revés en un registro.

Cuando no quedan más frases, se imprimen todas las frases inversas que se habían guardado en el registro.

![diagrama de flujo](https://github.com/alafa/theegg_ai/blob/master/tarea_38/invertir_palabras/diagramas/diagram.jpg?raw=true)

# Ejecución

El proyecto está desarrollado con Python 3.7.3

`python main.py /numero de frases a invertir/`

Por ejemplo: `python main.py 3` ejecutará el programa para invertir 3 frases.

