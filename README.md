### ¿Cómo viajan los turistas en España? Un estudio de tendencias y comportamiento

## Descripción

Este proyecto analiza los patrones de turismo en España, identificando tendencias de viaje y las regiones más visitadas. Se utiliza un conjunto de datos con información detallada sobre la cantidad de turistas en diferentes comunidades autónomas y provincias.

## Dataset

**Fuente:**
- [Número de turistas según comunidad autónoma de destino principal](https://www.ine.es/jaxiT3/Datos.htm?t=10823)
- [Eurostat - Turismo](https://ec.europa.eu/eurostat/web/tourism/database)

**Columnas:**

- Nombre de la comunidad autónoma o provincia.
- Cantidad de turistas.
- Periodo de tiempo.
- Otras variables relevantes.

## Preprocesamiento de Datos

- Conversión de columnas de tipo objeto a float.
- Manejo de valores nulos.
- Normalización de nombres de columnas.

## Análisis Exploratorio de Datos (EDA)

- Histogramas y distribuciones de turistas por provincia.
- Tendencias temporales.
- Comparaciones entre regiones.

## Librerías Utilizadas

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
```

## Carga de Datos

```python
turismo = pd.read_excel("./data/tourism_dataset.xlsx")
```

## Conclusiones

- [Incluir hallazgos clave del análisis]

## Autor

Cristian Vasquez

## Repositorio

[GitHub - EDA Turismo](https://github.com/Cristianvas198/EDA-Turismo.git)

