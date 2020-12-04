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

Esta estructura consiste de dos switch conectados entre sí cada uno son 4 ordenadores conectados. Dos ordenadores de cada
switch están en una red diferente pero en la misma red que otros dos ordenadores conectados al otro switch.

Es como si tuvieramos una empresa con dos sedes y dos departamentos diferentes en cada sede (Sistemas y Recusos humanos) y quisieramos
tener una VLAN para cada departamento. 

El objetivo es que cada departamento esté conectado con el mismo departamento en la otra sede, pero no con los demás.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/C.PNG?raw=true)

Las IPs de los ordenadores del mismo departamento tienes que estar en el mismo rango de IPs. Se ha asignado:
- Switch1, VLAN2, Ordenador1: 172.16.1.1
- Switch1, VLAN2, Ordenador2: 172.16.1.2
- Switch1, VLAN3, Ordenador1: 172.16.2.1
- Switch1, VLAN3, Ordenador2: 172.16.2.2
- Switch2, VLAN2, Ordenador1: 172.16.1.3
- Switch2, VLAN2, Ordenador2: 172.16.1.4
- Switch2, VLAN3, Ordenador1: 172.16.2.3
- Switch2, VLAN3, Ordenador2: 172.16.2.4

Por otra parte los switchs tienen que estar configurados de tal manera que se asigne a VLAN2 los puertos 01 y 02 y
a VLAN 3 los puertos 3 y 4. Y además los puertos tienen que estar en modo "trunk" para permitir el envio de datos entre
switches.

Para comprobar que todo está configurado de la forma correcta podemos ejecutar los siguientes comandos en la terminal
del cliente de cada switch.

Configuración de VLAN: `sh vlan`

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/C_conf.PNG?raw=true)

Configuración modo "trunk" de las interfaces: `sh interface trunk`

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/C_trunk.PNG?raw=true)


## Ejercicio D: Unir dos redes VLAN con un router

En esta estructura tenemos 3 departamentos (VLAN) utilizando cada uno su propia red pero queremos comunicar estas subredes
entre sí utilizando un Router.

El resultado final queda de la siguiente manera:

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/D.PNG?raw=true)

Lo primero se asignan IPs a los PCs y a sus gateways.

- VLAN2, Default gateway: 172.16.1.1
- VLAN2, Ordenador1: 172.16.1.2
- VLAN2, Ordenador2: 172.16.1.3


- VLAN3, Default gateway: 172.16.2.1
- VLAN3, Ordenador1: 172.16.2.2
- VLAN3, Ordenador2: 172.16.2.3


- VLAN4, Default gateway: 172.16.3.1
- VLAN4, Ordenador1: 172.16.3.2
- VLAN4, Ordenador2: 172.16.3.3

El switch tiene 24 puertos Ethernet disponibles. El último los reservamos para el router y el resto se dividen para VLAN.
Reservamos para VLAN2 (Departamento de sistemas) los puertos del 1 al 8, para VLAN3 (Departamento de desarrollo) los 
puertos 9-16 y para VLAN3 (Departamento de redes) los puertos 17-23. Siendo posible en cada VLAN conectar hasta 7 u 8 ordenadores.

Conectamos los ordenadores  al switch pora un puerto correspondiente a su VLAN y configuramos el switch desde la terminal de comandos.
Hay que crear las VLANs dandoles un nombre (SISTEMAS, DESARROLLO y REDES) y asignar a cada una de ellas sus puertos.
También hay que configurar el puerto 24, que es el que va a ir al router, para que esté en modo trunk.

Una vez se tiene esto se puede comprobar si hay conectividad entre dos ordenadores dentro de una misma VLAN. Entre VLANs
fallará la conexión porque necesitamos un router.

El router se configura para que dentro de un mismo puerto físico tengamos 3 puertos virtuales (uno para cada VLAN) y cada uno
tenga una IP que coincida con la dirección gateway que tenemos configuradas en los PCs (172.16.1.1, 172.16.2.1 y 172.16.3.1).
Y por último se levantan estos puertos. Quedando de esta manera la configuración del router:

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/D_router_conf.PNG?raw=true)

Con esta configuración los ordenadores de diferentes VLANs pueden comunicarse entre si.

## Ejercicio E: Enrutamiento estático

Este último ejercicio consiste en conectar 3 redes locales utilizando en enrutamiento estático entre routeres.

![Solucion ejercicio A](https://github.com/alafa/theegg_ai/blob/master/tarea_39/images/E.PNG?raw=true)

Tenemos tres redes locales cada una con 2 PCs conectados a un switch por Ethernet.
Asignamos IPs a cada ordenador y la IP de gateway.

- Red 1, Default gateway: 192.168.1.1
- Red 1, Ordenador1: 192.168.1.2
- Red 1, Ordenador2: 192.168.1.3


- Red 2, Default gateway: 172.16.1.1
- Red 2, Ordenador1: 172.16.1.2
- Red 2, Ordenador2: 172.16.1.3


- Red 3, Default gateway: 10.1.50.1
- Red 3, Ordenador1: 10.1.50.2
- Red 3, Ordenador2: 10.1.50.3

Cada red necesita un Router para poder comunicarse con las otras redes.
Los routers están conectados entre si por conexión serie. Esta conexión no viene instalada por defecto por lo que hay que agregarsela manualmente.
En cada router hay que hacer una serie de configuraciones:
- Asignar la IP de la gateway de la red correspondiente al puerto Ethernet y levantarlo.
- Configurar la opción de "clock rate" a aquellos routers que tengan una conexión saliente a otro router.
- Asignar IPs a los puertos serie de los routers de tal forma que dos puertos de una misma conexión tengan IPs de una misma red.
- Enrutar las IPs de los puertos serie de los routers.