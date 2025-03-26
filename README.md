# ¿Cómo viajan los turistas en España? Un estudio de tendencias y comportamiento

## Descripción del Proyecto
Este proyecto analiza cómo ha evolucionado el turismo en España, estudiando los patrones de visitantes, sus motivos de viaje y las tipologías de turismo. A través de un análisis de datos detallado, buscamos entender las tendencias clave y descubrir historias detrás de los números, como la estacionalidad, la influencia del turismo de negocios o el impacto de eventos culturales. Un enfoque claro y accesible para quienes quieren explorar la riqueza del turismo español.

## Hipótesis
- **Hipótesis 1**: El turismo en España sigue una fuerte estacionalidad, con picos en verano y descensos en invierno.
- **Hipótesis 2**: El turismo de ocio y recreo es el más predominante en España frente a otros motivos de viaje como negocios o estudios.
- **Hipótesis 3**: El turismo de negocios se concentra en ciertas comunidades autónomas más que en otras.
- **Hipótesis 4**: Los turistas de ciertos países gastan más dinero en España que otros.
- **Hipótesis 5**: Algunas comunidades autónomas han experimentado un crecimiento más acelerado en el número de turistas que otras.

## Datasets y Fuentes de Datos
A continuación, se listan los datasets utilizados en el análisis y sus respectivas fuentes:

1. **Viajeros y pernoctaciones por comunidades autónomas y provincias**  
   - Archivo: `datos_turismo.csv`  
   - Fuente: [INE - Tabla 2074](https://www.ine.es/jaxiT3/Tabla.htm?t=2074)  
   - Carga de datos: `df_1 = pd.read_csv("./data/datos_turismo.csv", delimiter=',')`

2. **Número de visitantes según tipología**  
   - Archivo: `datos_tipologia.csv`  
   - Fuente: [INE - Tabla 10821](https://www.ine.es/jaxiT3/Tabla.htm?t=10821)  
   - Carga de datos: `df_2 = pd.read_csv("./data/datos_tipologia.csv", delimiter=',')`

3. **Número de turistas según motivo principal del viaje**  
   - Archivo: `datos_motivo.csv`  
   - Fuente: [INE - Tabla 13864](https://www.ine.es/jaxiT3/Tabla.htm?t=13864)  
   - Carga de datos: `df_3 = pd.read_csv("./data/datos_motivo.csv", delimiter=',')`

4. **Gasto de los turistas internacionales según país de residencia**  
   - Archivo: `datos_gasto_pais.csv`  
   - Fuente: [INE - Tabla 10838](https://www.ine.es/jaxiT3/Tabla.htm?t=10838)  
   - Carga de datos: `df_4 = pd.read_csv("./data/datos_gasto_pais.csv", delimiter=',')`

5. **Gasto de los turistas internacionales según motivo principal del viaje**  
   - Archivo: `datos_sector.csv`  
   - Fuente: [INE - Tabla 23995](https://www.ine.es/jaxiT3/Tabla.htm?t=23995)  
   - Carga de datos: `df_5 = pd.read_csv("./data/datos_sector.csv", delimiter=',')`

## Objetivos del Análisis
- Identificar patrones de estacionalidad en el turismo español.
- Analizar las principales motivaciones de los turistas.
- Evaluar la distribución del turismo de negocios en distintas regiones.
- Comparar el gasto según la nacionalidad de los turistas.
- Estudiar el crecimiento del turismo en distintas comunidades autónomas.

## Herramientas Utilizadas
- **Python**: Lenguaje principal para el análisis de datos.
- **Librerías utilizadas:**
  - `pandas` para la manipulación de datos.
  - `numpy` para operaciones numéricas.
  - `seaborn` para visualización de datos.
  - `matplotlib.pyplot` para generación de gráficos.
- **Jupyter Notebook**: Para la documentación y ejecución del código.

## Instrucciones de Uso
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Cristianvas198/EDA-Turismo.git
   cd EDA-Turismo
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el análisis en un entorno Jupyter Notebook o en un script de Python.

## Contacto
Si tienes preguntas o sugerencias, no dudes en ponerte en contacto a través de tu [GitHub](https://github.com/Cristianvas198/EDA-Turismo).

---
Este README proporciona una estructura clara y profesional para tu EDA. Puedes modificarlo según lo necesites. ¡Éxito con tu análisis!



