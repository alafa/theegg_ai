# Simulador de redes

## En qué consiste la tarea

Con un simulador de redes vamos a construir distintas arquitecturas de redes informáticas.

Se pide montar en Cisco Packer Tracer:

- A) Red con servidor web y servidor de DNS
- B) Red con servidor DHCP
- C) Red VLAN básica
- D) Unir dos redes VLAN con un router
- E) Enrutamiento estático

## Ejercicio A: Red con servidor web y servidor de DNS

Los elementos en juego son: Un ordenador personal, un servidor web y un servidor DNS. Todos conectados al mismo switch.
Las direcciones IP de cada elemento pertenecen a la misma red.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/A.PNG?raw=true)


Direcciones IP utilizadas:

- Ordenador portatil: 176.30.0.6
- Servidor web: 176.30.0.5
- Servidor DNS: 176.30.0.15

En el servidor DNS se ha incluido un registro en el que la dirección web "www.miweb.com" esté asociada a la IP 176.30.0.5.

Para comprobar que todo funciona perfectamente se ha navegado a la web de "www.miweb.com" desde el ordenador portatil y
se ha visualizado su contenido.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/A_check.PNG?raw=true)

## Ejercicio B: Red con servidor DHCP

Un servidor DHCP se encarga de asignar IPs a los dispositivos conectados a la red que soliciten.
Para resolver este ejercicio necesitamos un servidor de DHCP y varios ordenadores conectados a un mismo switch.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/B.PNG?raw=true)

Lo primero de todo es configurar el servidor DHCP asignandole una IP propia, la IP default gateway, la del servicio DNS y estableciendo el
rango de IPs para asignar.

Lo hemos hecho así:
- IP del servidor DHCP: 172.16.1.254
- Default gateway: 172.16.1.1
- DNS server: 172.16.1.100

También, se ha establecido un límite de 100 IPs para asignar.

No hay que olvidar activar el servicio DHCP, que por defecto estará desactivado.

Después de tener configurado nuestro servidor DHCP, hay que especificar en los ordenadores que obtengan una IP mediante DHCP.
Y una vez que se les ha asignado una IP, entramos a la consola de comandos de uno de ellos a comprobar que todo ok y que 
hay una conexión funcionando correctamente tanto con el servidor como con el resto de ordenadores de la red.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/B_check.PNG?raw=true)


## Ejercicio C: Red VLAN básica

## Ejercicio D: Unir dos redes VLAN con un router

## Ejercicio E: Enrutamiento estático