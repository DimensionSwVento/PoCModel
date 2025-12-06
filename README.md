# PoCModel

## Uso

Ejecutar main.py en la raíz y luego abrir el archivo de salida 'map_output.html' para visualizar el mapa de viabilidad

## Librerías usadas
- numpy
- pandas
- folium

## Descripción

### Modelos matemáticos

En la carpeta raíz se encuentran dos archivos, estos corresponden a la implementación matemática de algunos de los MCDM revisados:
- topsis.py: En este archivo hay una implementación del MCDM TOPSIS para la generación de un ranking de alternativas
- wsm.py: En este archivo, similarmente hay una implementación del método de suma ponderada

Para ambos archivos estpa implementada la característica de selección de criterios para el análisis. También vale la pena mencionar que en ambas pruebas, la asignación de pesos a los criterios se realiza con AHP y se usa la misma valoración y set de alternativas para la comparación

Para visualizar los rankings de las alternativas ingresadas, ejecutar el archivo correspondiente

### Visualización

- En la carpeta 'data' se encuentran los datos de entrada (alternativas, criterios, matriz de comparació) en formato .csv
- En la carpeta 'mcdm' se encuentran los archivos con las funciones para el procesamiento de los datos
- En la carpeta 'visualization' se encuentran los archivos con la configuración para la creación del mapa y HeatMap