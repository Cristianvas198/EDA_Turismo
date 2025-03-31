
from utils import *

######################### PRIMERA HIPOTESIS #############################################################
#                                                                                                       #
#¿El turismo en España sigue una fuerte estacionalidad, con picos en verano y descensos en invierno?    #
#_______________________________________________________________________________________________________#

turismo = pd.read_excel("./src/data/tourism_dataset.xlsx") #Importa Dataset de la carpeta src
turismo=pd.DataFrame(turismo) #Convierte a formato Dataframe

#Creo un dataframe aparte para limpiar el nombre de las columnas
reemplazo_comunidad=turismo[" "].str.split(expand=True)
reemplazo_comunidad= reemplazo_comunidad.drop(columns = [0, 2, 3, 4])
#reemplazo_comunidad

#Union entre el datafram principal y el datafram de nombres limpios
turismo= pd.concat([turismo, reemplazo_comunidad], axis=1)
turismo = turismo.rename(columns={1: 'Comunidad'}) #Renombra la columna recien concatenada
turismo= turismo.drop(columns = [" "]) #Elimina la columna original 

#Numeros y caracteres innecesarios en las fechas
turismo.columns=turismo.columns.str.replace("M", " ")
turismo.columns=turismo.columns.str.replace(".5", "")
turismo.columns=turismo.columns.str.replace(".4", "")
turismo.columns=turismo.columns.str.replace(".3", "")
turismo.columns=turismo.columns.str.replace(".2", "")
turismo.columns=turismo.columns.str.replace(".1", "")

turismo = turismo.set_index("Comunidad") #Nuevo indice seranlos nombres de las comunidades
turismo = turismo.transpose() #Se revierte el orden para poner las fechas como indices

#Convertir los valores a STR para poder reemplazar simbolos y luego convertir a formato numerico
turismo = turismo.astype(str)
turismo = turismo.replace('\\.', '', regex=True)
turismo = turismo.replace(',', '.', regex=True)  # Cambia comas por puntos
turismo = turismo.apply(pd.to_numeric, errors='coerce')

turismo = turismo.loc[:, ~turismo.columns.duplicated()]#Elimina columnas duplicadas
turismo = turismo[~turismo.index.duplicated(keep='first')]

nuevo_índice = pd.to_datetime(turismo.index, format='%Y %m').to_period('M') #Convierto a formato fecha quedandome solo con mes y año.
turismo.index = nuevo_índice #Actualizo el indice en el Dataframe principal
turismo = turismo.sort_index()  # Ordena en ascendente


total_nacional = ('Nacional') #Condensa el total por año de toda españa 

#Media y mediana nacional por año desde 1990 hasta 2024
media_nacional = turismo['Nacional'].groupby(turismo.index.year).mean()
mediana_nacional = turismo['Nacional'].groupby(turismo.index.year).median()

#Datos COVID
# Analisis de turismo, pre, durante y post covid
pre_covid = estacion(turismo, año=(2017, 2019), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #Muestra turismo pre covid en España
covid = estacion(turismo, año=(2020, 2021), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #Muestra turismo durante el covid en España
post_covid = estacion(turismo, año=(2022, 2024), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #Muestra turismo post covid en España
covid_general = estacion(turismo, año=(2019, 2024), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #Muestra turismo post covid en España

#Muestras Verano
verano_nacional = estacion(turismo, año=(2020, 2023), comunidades=total_nacional, temporadas=("verano",)) #España completa

#Muestras Invierno
invierno_nacional = estacion(turismo, año=(2020, 2023), comunidades=total_nacional, temporadas=("invierno",)) #España completa

año1999=estacion(turismo, año=(1999, 1999), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #España completa
año2024=estacion(turismo, año=(2024, 2024), comunidades=total_nacional, temporadas=("primavera","verano", "otoño", "invierno")) #España completa

prueba = pd.concat([año1999, año2024], join='outer')



######################### SEGUNDA HIPOTESIS #############################################################
#                                                                                                       #
# ¿El turismo en España es más de turistas o excursionistas?                                            #
#_______________________________________________________________________________________________________#

tipologia = pd.read_excel("./src/data/tipologia_viaje.xlsx") #Importa el archivo
tipologia.columns=tipologia.columns.str.replace("M", " ")#Reemplaza la M de las fechas por un espacio
pd.options.display.float_format = '{:.1f}'.format #sE modifican los valores que tenian anotacion cientifica y confirma el formato float.
tipologia=tipologia.set_index(" ")
tipologia = tipologia[tipologia.columns[::-1]]
tipologia=tipologia.drop(["2015 10", "2015 11", "2015 12"], axis=1)
tipologia=tipologia.transpose()
tipologia = tipologia.apply(pd.to_numeric, errors='coerce')

nuevo_índice_tipologia = pd.to_datetime(tipologia.index, format='%Y %m').to_period('M') #Convierto a formato fecha quedandome solo con mes y año.
tipologia.index = nuevo_índice_tipologia #Actualizo el indice en el Dataframe principal
tipologia = tipologia.sort_index()  # Ordena en ascendente
tipologia.columns = tipologia.columns.str.strip()

tipologia_2=tipologia.drop(["Acumulado en lo que va de año", "Tasa de variación anual", "Tasa de variación acumulada"], axis=1)
tipologia_2 = tipologia_2.iloc[:, 1:]
tipologia_2.columns.values[1] = "Datos Turista"  # Cambia la segunda columna
tipologia_2.columns.values[3] = "Datos Excursionista"
tipologia_2=tipologia_2.drop(["Turista", "Excursionista"], axis=1)
#tipologia_2 = tipologia_2[["Datos Turista", "Datos Excursionista"]]  # Selecciona solo las columnas útiles

total_turistas = tipologia_2["Datos Turista"].sum()
total_excursionistas = tipologia_2["Datos Excursionista"].sum()



######################### TERCERA HIPOTESIS #############################################################
#                                                                                                       #
# ¿España es un país en el que los viajes por negocios van en aumento?                                  #
#_______________________________________________________________________________________________________#

motivo_viaje = pd.read_excel("./src/data/motivo_viaje.xlsx")
motivo_viaje.columns=motivo_viaje.columns.str.replace("M", " ")#Reemplaza la M de las fechas por un espacio
motivo_viaje = motivo_viaje.transpose()
motivo_viaje.columns = motivo_viaje.iloc[0].astype(str).str.strip()  #Convierte valores string y elimina los espacios
motivo_viaje = motivo_viaje.drop(motivo_viaje.index[0])  #Elimina la fila con los nombres
#motivo_viaje.columns
#motivo_viaje

motivo_viaje.columns.values[5] = "Total Ocio"
motivo_viaje.columns.values[10] = "Total Negocios"
motivo_viaje.columns.values[15] = "Total Otros motivos"

negocios = motivo_viaje[['Total Negocios']].copy()
negocios = negocios.transpose()
negocios = negocios[negocios.columns[::-1]]
negocios



######################### CUARTA HIPOTESIS #############################################################
#                                                                                                       #
# ¿Los turistas de ciertos países gastan más dinero en España que otros?                                #
#_______________________________________________________________________________________________________#

pais = pd.read_excel("./src/data/Gasto_segun_paisxlsx.xlsx")
pais.columns=pais.columns.str.replace("M", " ")#Reemplaza la M de las fechas por un espacio
pais=pais.set_index(" ")
pais = pais.transpose()
tipologia = tipologia.apply(pd.to_numeric, errors='coerce')