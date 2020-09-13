# Cifrado y descifrado con el solitario

Se necesita dos barajas de cartas con dos comodines incluidos. Una para cifrar y otra para descifrar el mensaje.

Este algoritmo está pensado para realizarse manualmente sin ningún programa informático. Pero aquí lo hemos desarrollado en Python.

## Procedimientos:

#### Cifrar un mensaje
  1. Generar una llave tan larga como el mensaje a cifrar. (Ver más adelante como crear la clave)
  2. Convertir las letras del mensaje a cifrar a números (A=1, B=2, C=3, ...).
  3. Sumar el mensaje convertido a números con la llave con módulo 26 (Si el resutlado es mayor de de 26, se resta 26).
  4. Convertir los números del resultado a letras.
  
#### Descrifrar un mensaje
  1. Generar la misma llave que el emisor.
  2. Convertir el mensaje encriptado recibido a números.
  3. Restar la ristra numérica al mensaje numérico (módulo 26).
  4. Convertir a letras el resultado de la resta.
  
#### Generar la llave para cifrar
 1. Mover el comodín A a una posición atrás (si ya era la última carta, se pone la segunda).
 2. Mover el comodín B dos posiciones atrás.
 3. Cortar la baraja por los comodines en tres partes (ambos comodines se quedan en la parte del medio). Y se intercambia la primera parte con la tercera.
 4. Convertir la última carta en un número del 1 al 53.
 
 Para hacer la conversión de carta a número:
 
 El valor de la carta +
 - Si es de treboles: +0
 - Si es de rombos: +13
 - Si es de corazones: +26
 - Si es de picas: +39
 - Joker: 53
 
 5. Convertir la carta con la posición del resultado anterior en un número del 1 al 53 siguiendo el mismo método.
 6. Poner el resultado en la llave
 7. Repetir pasos 1-7 tantas veces como letras tenga el mensaje que se quiera encriptar/desencriptar.
 
### Apuntes adicionales:

- El mensaje a cifrar/descifrar no puede contener espacios.
- Las dos barajas deben partir con un mismo orden de cartas.


## Código

### Clases definidas

#### Clase "Card"

Es una clase muy sencilla y también el elemento más básico del programa. Representa una carta física de la baraja.

##### Atributos
- **type:** El palo de la carta: spaces (picas), diamonds (diamantes), hearts (corazones), clubs (tréboles) o joker.
- **num:** El número de la carta. De 1 a 13 o A/B en el caso de los jokers
- **value:** El valor correspondiente a cada carta (del 1 al 53)

##### Métodos
- **\_\_init__(type, num):** Se asigna un value según el palo y número de la carta especificado.

#### Clase "DeckOfCards"

Representa una baraja de cartas.

##### Atributos
- **cards:** Un array de clases "Card" en un orden determinado.

##### Métodos
- **\_\_init__():** Se genera una baraja de cartas completa de 54 cartas.
- **shuffle():** De forma aleatoria todas las cartas de la baraja toman una nueva posición.
- **move_card( type, num, positions):** Mueve la carta con los atributos definidos tantas posiciones como se indiquen.
- **cut_and_swap_by_jokers():** Corta la baraja por los jokers e intercambia losdos extremos.
- **get_first_card_value():** Devuelve el valor de la carta posicionada en el primer lugar de la baraja.
- **get_card(position):** Devuelve la carta posicionada en la posición especificada.
- **set_cards_as(other_deck):** Adopta las cartas (y el orden) de otra baraja proporcionada.

#### Clase "Solitaire"

Se trata de la clase madre de las clases SolitaireEncryptor y SolitaireDecryptor.
Aquí se recogen todas aquellas funciones que son comunes al encifrar y descifrar. Como por ejemplo, generar una llave.

##### Atributos
- **deck:** La baraja de cartas con la que se va a encriptar/desencriptar.
- **letter_conversion_dict:** El diccionario que se utiliza para convertir letrás a números y viceversa. Se lee de un fichero .json.

##### Métodos

- **generate_key(length_of_key):** Genera una llave del tamaño que se especifique.

#### Clase "SolitaireEncryptor"

Hereda los atributos y métodos de su clase madre "Solitaire". Además, tiene un método propio método para encriptar un mensaje dado.

##### Atributos
- / Los heredados de la clase Solitaire /

##### Métodos

- / Los heredados de la clase Solitaire /
- **encrypt_msg(msg):** Encripta el mensaje y devuelve el resultado.

#### Clase "SolitaireDecryptor"

Hereda los atributos y métodos de su clase madre "Solitaire". Además, tiene un método propio método para desencriptar un mensaje dado.

##### Atributos
- / Los heredados de la clase Solitaire /

##### Métodos

- / Los heredados de la clase Solitaire /
- **encrypt_msg(msg):** Desencripta el mensaje y devuelve el resultado.

## Ejecución

El proyecto entero está desarrollado con Python 3.6.4

Ejecutar comando `python main.py DONOTUSEPC` en la terminal para ejecutar el programa.
El mensaje DONOTUSEPC se encriptará y luego se desencriptará solo con la información del mensaje encriptado y la baraja de cartas.

Se puede sustituir el mensaje por el que se quiera siempre teniendo cuidado de no incluir espacios.