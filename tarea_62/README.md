# Convertir una computadora tonta en algo más inteligente: bash scripting

En esta tarea se pide desarrollar tres programar de bash scripting en la que se automaticen ciertos procesos.

Los procesos que se han querido automatizar son:
1) Editar el nombre de unos ficheros con la palabra "OLD" cuando no se hayan modificado en más de x tiempo.
2) Cambiar el fondo de pantalla automáticamente cada 5 minutos.
3) Apagar automáticamente la máquina tras completarse una cuenta atrás.

## Script 1: Marcar los ficheros viejos

Lo primero se le pide al usuario insertar por comando el número de minutos que se quiere tomar como tiempo límite.
Posteriormente, marca todos los archivos del directorio "./ficheros" cuyo tiempo desde la última actualización sea menor al tiempo especificado anteriormente.

Para marcarlos, se añadirá al principio del nombre de cada fichero "OLD_".

## Script 2: Rotación automática de fondo de pantalla

Un script pensado para que no te aburras del fondo de pantalla.

Cada cinco minutos cambia de fondo de pantalla utilizando las imágenes de fondo de pantalla disponibles en '/usr/share/backgrounds/'.
Cuando termina con todas ellas vuelve al principio en un bucle infinito.

Nota: Para comprobar su funcionamiento quizá os interese modificar los 5 minutos por 5 segundos en el código.
5m -> 5

## Script 3: 5 minutos más y lo dejo

Al ejecutar este script se pide al usuario insertar un número de minutos que queremos que espere la cuenta atrás.

Seguidamente, comienza un countdown y cuando llega a 0, se apagará la máquina.
Es ideal para cuando debes dejar el ordenador para ponerte a hacer otras cosas pero por voluntad propia no lo consigues.


## Ejecuciones

Se ha desarrollado en un sistema operativo Linux Ubuntu 20.04.2 LTS.

Si al lanzar el script en la terminal de Linux da un error es posible que sea debido a que no tiene configurados los permisos de ejecución.
Para solucionar esto simplemente ejecutar los siguientes comandos:

`chmod +x script1.sh`
`chmod +x script2.sh`
`chmod +x script3.sh`

Para ejecutar cada script simplemente lanzar en la línea de comandos de Linux:

`./script1.sh`
`./script2.sh`
`./script3.sh`

