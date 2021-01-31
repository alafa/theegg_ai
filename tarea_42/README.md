# Tarea 42

Para esta tarea se pide desarrollar una página web básica, añadir algo de color por CSS y añadir algún video.
De forma opcional se pide permitir controlar la reproducción del video mediante comandos de voz.

# Tecnología utilizada

Se ha desarrollado utilizado Python 3.9.1 y se ha hecho uso del framework para desarrollo web Django.

Para la reproducción del video por comandos de voz se ha utilizado
[la API de Iframe de youtube](https://developers.google.com/youtube/iframe_api_reference?hl=es-419)
y el lenguaje de peogramación web Javascript.

# Instrucciones por reconocimiento de voz

Dentro de la págian de detalle de cada video se permite ver el video y controlarlo por comandos de voz.

Existen tres acciones que se pueden realizar sobre el video mediante el reconocimiento de voz.
Estas son:
1) Iniciar o continuar el video.
2) Pausar el video.
3) Terminar el video.

Las instrucciones que el sistema comprende son:
reproducir, play, ver, empezar, comenzar, continuar, pausa, pausar, parar, stop, terminar, fin y salir.

Hace falta activar los permisos del microfono del navegador y hacer clic al botón "Instrucción por voz" antes de pronunciar
 en voz alta la orden.

# Puesta en marcha

Se necesita instalar Django y Pillow.

`python -m pip install django`

`python -m pip install Pillow`

Para lanzar el servidor web solo hay que ejecutar:

`python manage.py runserver`

La web estará accesible en local en el puerto 8000: http://127.0.0.1:8000/

