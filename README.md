# PoCModel

## Capturas de resultados

<img width="354" height="280" alt="image" src="https://github.com/user-attachments/assets/7587e88b-9b46-4e85-99f0-3bb580632e02" />

_*AHP outputs*_

<img width="393" height="239" alt="image" src="https://github.com/user-attachments/assets/f351b931-31e7-4ee6-b38c-6a4e73a11d4d" />

_*Ranking results by method*_

<img width="1394" height="859" alt="image" src="https://github.com/user-attachments/assets/41e045dc-bfcf-4740-9543-d1cece267436" />

_*Heatmap for TOPSIS ranking*_

<img width="1445" height="849" alt="image" src="https://github.com/user-attachments/assets/3dad3ed5-6ff2-4eb0-b7af-3fcb394ab29b" />

_*Heatmap for WSM ranking*_

## Uso

Ejecutar main.py en la raíz y luego abrir los archivos de salida 'map_topsis.html' y 'map_wsm.html' para visualizar los mapas de viabilidad

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
