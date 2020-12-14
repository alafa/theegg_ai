## Enunciado de la misión

![Enunciado](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/8.1.PNG?raw=true)

En esta misión nos piden registros únicos además de obtener los resultados en un orden determinado.

## SQL Query

![sql_query](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/8.2.PNG?raw=true)

Con `SELECT DISTINCT Email, Promotions` estamos indicando que no queremos valores repetidos con mismo Email y Promotions.
Es decir, puede que se obtengan dos emails distintos pero cada uno tendrá un valor en Proportions diferente (y viceversa).
Pero si que nos aseguramos que con el mismo email no vamos a tener dos registros con el mismo valor en Promotions.

A su vez, con `ORDER BY Promotions DESC` estamos indicando que queremos obtener los registros en un orden descendente
según el valor de la columna Promotions.

## Resultados en la base de datos

![result](https://github.com/alafa/theegg_ai/blob/master/tarea_43/images/8.3.PNG?raw=true)