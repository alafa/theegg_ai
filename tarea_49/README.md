# Aprender a pensar como un programador: Introducción a la POO

## Enunciados
### Ejercicio 1: Persona

Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes
métodos para la clase:
. Un constructor, donde los datos pueden estar vacíos.
. Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de
datos.
. mostrar(): muestra los datos de la persona.
. esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad.


### Ejercicio 2: Cuenta
Crea una clase llamada Cuenta que tendrá los siguientes atributos:
. titular (que es una persona)
. cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
. Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo
ingresando o retirando dinero.
. mostrar(): muestra los datos de la cuenta.
. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se
hará nada.
. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

# Solución

`cuenta.py` y `persona.py` contienen las clases Cuenta y Persona respectivamente.

Se han utilizado los decorators propios de python `@property` y `@property.setter` para implementar los getters y setters.
Estos decorators permiten realizar validaciones y transformaciones antes de guardar o devolver los atributos a la vez que
permiten acceder a las propiedades de una forma aparentemente directa (Ej: `una_persona.edad`).

En [este video](https://www.youtube.com/watch?v=jCzT9XFZ5bw&ab_channel=CoreySchafer) lo explican muy bien.

# Unit tests

Se han implementado unit tests para comprobar el correcto funcionamiento de las clases Persona y Cuenta. Para lanzar estos
tests hace falta ejecutar en la línea de comandos:

```
python test_cuenta.py -v
```

```
python test_persona.py -v
```

El parámetro `-v` es opcional pero es recomendable para ver qué tests pasa y cuales no.

# Version Python

Los ejercicios están desarrollado con Python 3.7.3


