# Construye un simulador

Desarrollar un programa donde una vez enviado un valor decimal a una función
este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor
analógico digital.

# Explicación de la solución

El programa principal llama a una función `dec_to_binary(dec_num)` pasando el número decimal a convertir como argumento.

Esta función llama a una función recursiva y esta se llama a si misma con el número que se le ha pasado como argumento entre dos (dejándolo en número entero)
hasta que este sea 1 o 0. Luego, cada una de ellas añade a una variable string `tmp` el resto que queda al dividir el número entre dos.

Ejemplo:

|         | ejec_1       | ejec_2      | ejec_3     | ejec_4    | ejec_5   | ejec_6  |
|---------|--------------|-------------|------------|-----------|----------|---------|
| num     | 57           |             |            |           |          |         |
| num     |              | 28          |            |           |          |         |
| num     |              |             | 14         |           |          |         |
| num     |              |             |            | 7         |          |         |
| num     |              |             |            |           | 3        |         |
| num     |              |             |            |           |          | 1       |
| returns |              |             |            |           |          | "**1**" |
| returns |              |             |            |           | "1**1**" |         |
| returns |              |             |            | "11**1**" |          |         |
| returns |              |             | "111**0**" |           |          |         |
| returns |              | "1110**0**" |            |           |          |         |
| returns | "11100**1**" |             |            |           |          |         |

En el ejemplo se convierte el número 57 en binario.
Las filas "num" representan una llamada a la función recursiva con num como argumento
y las filas "returns" representan lo que devuelve la función recursiva.
Las columnas representan cada ejecución de la función. Siempre hay tantas como dígitos tenga el número binario resultante.

Se llama una primera vez a la función recursiva pasando como argumento el número 57.
Esta vuelve a llamar a la función recursiva pasando el número anterior entre dos en número entero. Es decir, 57 // 2 = 28.

Se repite este procedimiento hasta llegar a 1 en la sexta llamada, entonces, procedemos a resolver las funciones empezando por la más profunda, la sexta.

Cada resultado que se revuelve se concatena al final de la variable `tmp` en forma de string resultando finalmente en el número binario que se quería obtener.
Se hace aportando el número que ha obtenido como argumento resto 2. Es decir, un 1 si es un número impar o un 0 si es un número par.

# Ejecución

El proyecto entero está desarrollado con Python 3.6.4

Ejecutar comando `python main.py /numéro a convertir/` en la terminal para ejecutar el programa.

Por ejemplo, ejecutar `python main.py 57` para convertir a binario el número 57.

