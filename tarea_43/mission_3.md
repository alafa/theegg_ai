## Enunciado de la misión

![Enunciado](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/3.1.PNG?raw=true)

Se pide escribir una consulta para obtener todos los registros de la tabla "mailing_list" pero se especifica que solo
nos interesan tres propiedades: "GivenName", "EmailAddress" y "Joined".

## SQL Query

![sql_query](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/3.2.PNG?raw=true)

La solución sigue siendo muy parecida a las anteriores, con la excepción de que se piden limitar los campos que se obtienen
a unos en concreto.
Con `SELECT GivenName, EmailAddress, Joined` se indican los campos que se quieren obtener. Y con `FROM mailing_list`
se indica cual es la tabla de la que se quieren los datos.
 El `;` al final es obligatorio.

## Resultados en la base de datos

![result](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/3.3.PNG?raw=true)

Efectivamente, se obtienen las tres propiedades especificadas en la consulta de todos los registros de la tabla.