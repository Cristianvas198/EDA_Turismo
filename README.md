# ¿Cómo viajan los turistas en España?

### Un estudio de tendencias y comportamiento del turismo en España

![Turismo](./src/Imagenes/Turismo_banner.png)

## Descripción
Este proyecto es un Análisis Exploratorio de Datos (EDA) sobre las tendencias y el comportamiento del turismo en España. Utiliza datos del Instituto Nacional de Estadística (INE) para examinar patrones de estacionalidad, tipología de viaje, turismo de negocios y gasto de los turistas según su país de origen.

## Hipótesis a trabajar en este EDA
1. ¿El turismo en España sigue una fuerte estacionalidad?
2. ¿Es más frecuente el turismo de estancia o la excursión?
3. ¿El turismo de negocios está creciendo en España?
4. ¿Los turistas de ciertos países gastan más que otros en España?

## Librerías utilizadas
```python
import pandas as pd
import numpy as np
import seaborn as sb
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import plotly.graph_objects as go
import qrcode
import warnings
from datetime import datetime
from matplotlib.ticker import FuncFormatter
```

## Dataset y Fuentes
Este proyecto utiliza datos abiertos del Instituto Nacional de Estadística de España (INE):

- **Viajeros y pernoctaciones por comunidades autónomas y provincias**  
  Dataset: `./data/tourism_dataset.xlsx`  
  Fuente: [INE - Tabla 2074](https://www.ine.es/jaxiT3/Tabla.htm?t=2074)
  
- **Número de visitantes según tipología**  
  Dataset: `./data/tipologia_viaje.xlsx`  
  Fuente: [INE - Tabla 10821](https://www.ine.es/jaxiT3/Tabla.htm?t=10821)
  
- **Número de turistas según motivo principal del viaje**  
  Dataset: `./data/motivo_viaje.xlsx`  
  Fuente: [INE - Tabla 13864](https://www.ine.es/jaxiT3/Tabla.htm?t=13864)
  
- **Gasto de los turistas internacionales según país de residencia**  
  Dataset: `./data/Gasto_segun_paisxlsx.xlsx`  
  Fuente: [INE - Tabla 10838](https://www.ine.es/jaxiT3/Tabla.htm?t=10838)
  
- **Gasto de los turistas internacionales según motivo principal del viaje**  
  Dataset: `./data/Gasto_por_sector.xlsx`  
  Fuente: [INE - Tabla 23995](https://www.ine.es/jaxiT3/Tabla.htm?t=23995)
  
## Repositorio
Puedes encontrar el código y los archivos de este proyecto en GitHub:  
[Repositorio en GitHub](https://github.com/Cristianvas198/Turismo_Spain.git)

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio.

---

© 2025 Cristian Vásquez






 
