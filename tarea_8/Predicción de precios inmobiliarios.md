# Predicción de precios inmobiliarios

### Estado del arte

1) Habría que definir el alcance geográfico que queremos tener ¿El país entero? ¿Solo nuestra CCAA? etc.

2) También habría que definir si queremos centrarnos solo en las viviendas de las grandes urbes, en la compra o alquiler de la vivienda o si excluimos o no oficinas y locales.
Cuanto más especifico sea nuestro objetivo, mejores estimaciones se podrán hacer. Eso sí, siempre que tengamos el histórico del precio del m2 (o algún dato similar) de las características elegidas.

3) Además, para que nuestra aplicación pueda llegar a dar respuestas más acertadas habría que definir el periodo de predicción (Ej: A un año vista). *Llamemos a este periodo 'T'*.
De esta forma, podremos seleccionar variables que veamos que tengan el mayor impacto en el precio de la vivienda en el periodo de interés.

4) Brain storming de datos que pudieran estar relacionados con la variación de precios inmobiliarios:

Necesitariamos datos historicos cada T al menos desde 5 veces T. Es decir, si hemos elegido predecir a 1 año vista, mínimo necesitariamos datos de cada año desde hace 5 años atrás.

Datos económicos, políticos y sociales:
- PIB per capita
- Tasa de paro
- Precio de la luz
- Partido político en el poder
- Año de elecciones sí/no
- Nº nacimientos
- Población
- Salarío mínimo interprofesional
- Salario medio interprofesional
- Otros (consultar con experto)


Datos relacionados directamente con el sector inmobiliario:

- Nº de viviendas vacías
- Nº viviendas nuevas construidas
- Nº viviendas asignadas de VPO
- Otros (consultar con experto)
- Precio del m2 T años más tarde (desconocido en el último año)


### Adquisición de datos:

Existen varias fuentes que nos pueden proporcionar datos de esta índole cómo por ejemplo el Instito Nacional de Estadística, Eustat o Eurostat.

### Procedimiento

1. Secolectar todas las variables que pudieran tener relación con el precio inmobiliario y que estén disponibles.

2. Montar un set de datos normalizando cada una de las variables.

3. Realizar un análisis de reducción de la dimensión para descartar las variables que menos aportan.

4. Entrenar el modelo de forma supervisada siendo la variable objetivo *el precio del m2 T años más tarde*. Guardando el último año conocido para testing.

5. Evaluar el rendimiento de la aplicación. Si fuera necesario habría que revisar desde el primer punto y encontrar nuevas variables.





