import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import random


#Funcion para sacar las muestras del Dataframe Turismo por Comunidad, Año y Temporada
def estacion(df = turismo, año = 2024, comunidades=("Madrid",), temporadas=("invierno",)):
    '''
    Filtra el DataFrame principal con:
    - Rango de años.
    - Ciudades Seleccionadas en España.
    - Temporadas Seleccionadas.

    P/ejem: 
    estacion(turismo, (2020, 2024), ["Madrid", "Barcelona"], ("invierno", "primavera"))
    '''
    
    temporada_dict={  #Con el diccionario el argumento de la funcion se compara con los numeros y determina los numeros a filtrar del Dataframe
        "primavera":(3,4,5),
        "verano" : (6,7,8),
        "otoño" : (9,10,11),
        "invierno" : (12, 1, 2)}
    
    meses = sum((temporada_dict[temporada] for temporada in temporadas), ())
    
    if isinstance(comunidades, str):
        comunidades = [comunidades]
        # df = df.to_timestamp()
    filtro = (
        (df.index.strftime('%Y').astype(int) >= año[0]) &
        (df.index.strftime('%Y').astype(int) <= año[1]) &
        (df.index.strftime('%m').astype(int).isin(meses))
    )
    
    # Devuelve el DataFrame filtrado para las comunidades seleccionadas
    return df.loc[filtro, comunidades]


def comunidades(turismo, comunidad):
    # Diccionario de comunidades y provincias
    comunidades_autonomas = {
        "Andalucía": ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"],
        "Aragón": ["Huesca", "Teruel", "Zaragoza"],
        "Asturias": ["Asturias"],
        "Balears, Illes": ["Balears, Illes"],
        "Canarias": ["Palmas, Las", "Santa Cruz de Tenerife"],
        "Cantabria": ["Cantabria"],
        "Castilla y León": ["Ávila", "Burgos", "León", "Palencia", "Salamanca", "Segovia", "Soria", "Valladolid", "Zamora"],
        "Castilla - La Mancha": ["Albacete", "Ciudad Real", "Cuenca", "Guadalajara", "Toledo"],
        "Cataluña": ["Barcelona", "Girona", "Lleida", "Tarragona"],
        "Comunitat Valenciana": ["Alicante/Alacant", "Castellón/Castelló", "Valencia/València"],
        "Extremadura": ["Badajoz", "Cáceres"],
        "Galicia": ["Coruña, A", "Lugo", "Ourense", "Pontevedra"],
        "Madrid": ["Madrid"],
        "Murcia": ["Murcia"],
        "Navarra": ["Navarra"],
        "País Vasco": ["Araba/Álava", "Bizkaia", "Gipuzkoa"],
        "Rioja, La": ["Rioja, La"],
        "Ceuta": ["Ceuta"],
        "Melilla": ["Melilla"]
    }
    provincias = comunidades_autonomas.get(comunidad, [])
    if provincias:
        return turismo.loc[:, turismo.columns.intersection(provincias)]
    else:
        print(f"La comunidad '{comunidad}' no existe.")
        return None
    
def format_millions(x, p):
    return f'{int(x/500000)}M'