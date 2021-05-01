# Convertir una computadora tonta en algo más inteligente: bash scripting

EN DESARROLLO...

## Script 1: Mover a carpeta archivo aquellos ficheros que lleven más de un tiempo dado sin una modificación.

Lo primero se le pide al usuario insertar por comando el número de minutos que se quiere tomar como tiempo límite. Posteriormente, marca todos los archivos del directorio "./ficheros" cuyo tiempo desde la última actualización sea menor al tiempo especificado anteriormente.

Para marcarlos, se añadirá al principio del nombre de cada fichero "OLD_".

## Script 2: Rotación automática de fondo de pantalla

Cada cinco minutos cambia de fondo de pantalla utilizando las imágenes de fondo de pantalla disponibles en '/usr/share/backgrounds/'.
Cuando termina con todas ellas vuelve al principio en un bucle infinito.

## Script 3: Countdown

Al ejecutar este script comienza un countdown y cuando llega a 0... ¿Apagamos máquina?



## Ejecuciones

Se ha desarrollado en un sistema operativo Linux Ubuntu 20.04.2 LTS.

Si al lanzar el script en la terminal de Linux da un error.
Probar a cambiar los permisos de ejecución:

'chmod +x script.sh'


