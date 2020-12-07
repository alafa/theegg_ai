# Tu primera expresión regular

Para esta tarea proponemos el siguiente ejercicio: el @egger mediante técnicas de Regex debe
calcular **el número de caracteres**, **el número palabras** y **ranking de palabras por frecuencia de uso**
del siguiente texto. La aplicación debe servir para cualquier otro texto:


> En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así.

# Solución planteada

Para utilizar la librería de expresiones regulares en Python hay que importar la librería regex `import re`.

Para hallar el número de carácteres se ha utilizado la expresión `.` ya que un punto contabiliza cualquier carácter.
Para contar las palabras se ha utilizado la expresión `\w+`.

El contador de palabras se ha implementado a partir de obtener un listado de palabras en el punto anterior. Por cada palabra
se ha generado una expresión regex específica entre `\\b`, que delimita como empieza y como termina una palabra. Además,
se ha añadido la opción que no sea sensible a mayuscúlas y minúsculas.

El restultado es el que sigue:

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_41/images/Capture.PNG?raw=true)


# Ejecución

El proyecto está desarrollado con Python 3.7.3

Se debe ejecutar `python main.py` para lanzar el script.

Si se desea modificar el texto o procesar una nuevo, se tiene que reemplazar en `text.txt`.
