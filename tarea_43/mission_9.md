## Enunciado de la misión

![Enunciado](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/9.1.PNG?raw=true)

La novedad de esta misión es que se nos pide ordenar los registros obtenidos por más de una propiedad.
Es decir, los registros se ordenaran por "NumberOfPosts" pero los registros con mismo valor de "NumberOfPosts" seguiran
el criterio de ordenarse por "AccessTime".

## SQL Query

![sql_query](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/9.2.PNG?raw=true)

`ORDER BY` admite varias columnas cada una con su criterio ASC/DESC. Primero ordenará por la primera, luego por la 
segunda... y asi sucesivamente.

## Resultados en la base de datos

![result](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/9.3.PNG?raw=true)