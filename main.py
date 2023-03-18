from fastapi import FastAPI, Request, Form
import pandas as pd
import numpy as np
from flask import Flask, request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional
'''
#------------>>>> Abrimos consola, ejecutamos uvicorn main:app --reload      <<<----------
#------------>>>>Esto hará que cada ctrl+s que hagamos, el server se carge y actualice    <<<-----------
#------------>>>>Los enlaces de cada consulta se encuentran en el archivo ipynb "funciones_para_app   <<<-----------
'''

# Creamos la aplicación FastAPI y cargamos la base de datos

app = FastAPI(tiitle='Proyecto Individual',
              title='Consulta de peliculas en las plataformas de streaming: Amazon, Disney+, Hulu y Netflix')

df_api = pd.read_csv('base_datos_completa_api.csv', sep=',')


# Definimos el método
@app.get('/about')
async def read_intro():
    return 'API creada con FastAPI y Uvicorn'

# Aplicamos las consutlas que fueron solicitadas:
'''
1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.
'''


@app.get("/get_max_duration/")
async def get_max_duration(anio: int, plataforma: str, duracion: str, ):
        plataformas_df = df_api.copy()  # Copiamos el DataFrame original
        if plataforma == "amazon":
                df1 = plataformas_df[(plataformas_df["type"] == "movie") & (plataformas_df["release_year"] == anio) & (
                    plataformas_df["duration_type"] == duracion) & (plataformas_df["id"].str.findall("a"))]
        elif plataforma == "disney":
                df1 = plataformas_df[(plataformas_df["type"] == "movie") & (plataformas_df["release_year"] == anio) & (
                    plataformas_df["duration_type"] == duracion) & (plataformas_df["id"].str.findall("d"))]
        elif plataforma == "hulu":
                df1 = plataformas_df[(plataformas_df["type"] == "movie") & (plataformas_df["release_year"] == anio) & (
                    plataformas_df["duration_type"] == duracion) & (plataformas_df["id"].str.findall("h"))]
        elif plataforma == "netflix":
                df1 = plataformas_df[(plataformas_df["type"] == "movie") & (plataformas_df["release_year"] == anio) & (
                    plataformas_df["duration_type"] == duracion) & (plataformas_df["id"].str.findall("n"))]
        else:
                print("No contamos con la base de datos de dicha plataforma")

        df2 = df1[df1["duration_int"] == (df1["duration_int"].max())]
        return f'Peliculas de {plataforma} del año {anio} con mayor duracion en {duracion}: {df2.iloc[0, 2]}'

'''
2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
'''


@app.get("/get_score_count/")
def get_score_count(platform: str, scored: int, year: int):
    plataformas_df = df_api.copy()  # Copiamos el DataFrame original
    df5 = plataformas_df[(plataformas_df["score_mean"] > scored) & (
        plataformas_df["release_year"] == year)]  # Filtro de busqueda por Score y Año
    if platform == "amazon":
        # ------->>>>>> Generamos un dataframe general con filtros especificos segun busqueda
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("a"))]
    elif platform == "disney":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("d"))]
    elif platform == "hulu":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("h"))]
    elif platform == "netflix":
        df_gsc = df5[(df5["type"] == "movie") & (df5["id"].str.findall("n"))]
    else:
        print("Try again")

    return "Peliculas de {} del año {} con puntaje mayor en score a {} es: {}".format(platform, year, scored, df_gsc.shape[0])


'''
3. Cantidad de peliculas por plataforma.
'''


@app.get("/get_count_platform/")
def get_count_plaform(platform: str):
    plataformas_df = df_api.copy()  # Copiamos el DataFrame original
    if platform == "amazon":
       df1 = plataformas_df[(plataformas_df["type"] == "movie") & (
           plataformas_df["id"].str.contains("a"))]
    elif platform == "disney":
       df1 = plataformas_df[(plataformas_df["type"] == "movie") & (
           plataformas_df["id"].str.contains("d"))]
    elif platform == "hulu":
       df1 = plataformas_df[(plataformas_df["type"] == "movie") & (
           plataformas_df["id"].str.contains("h"))]
    elif platform == "netflix":
       df1 = plataformas_df[(plataformas_df["type"] == "movie") & (
           plataformas_df["id"].str.contains("n"))]
    else:
        print("No contamos con esta plataforma")
    df2 = len(df1)
    return f'La cantidad de películas de de la paltaforma {platform} es {df2}'


'''
4. Actor que más se repite según plataforma.
'''


@app.get("/get_actor/")
def get_actor(platform: str, year: int):
     plataformas_df = df_api.copy()  # Copiamos el DataFrame original
     if platform == "amazon":
       df1 = plataformas_df[(plataformas_df["release_year"] == year) & (plataformas_df["id"].str.contains("a"))]
     elif platform == "disney":
        df1 = plataformas_df[(plataformas_df["release_year"] == year) & (plataformas_df["id"].str.contains("d"))]
     elif platform == "hulu":
        df1 = plataformas_df[(plataformas_df["release_year"] == year) & (plataformas_df["id"].str.contains("h"))]
     elif platform == "netflix":
        df1 = plataformas_df[(plataformas_df["release_year"] == year ) & (plataformas_df["id"].str.contains("n"))]
     else:
           print("No contamos con esta plataforma")
           return
     if df1["cast"].isna().all():
        return "No hay información de actores para la plataforma y año seleccionados"

     actors = df1["cast"].str.split(",", expand=True).stack().str.strip().reset_index(level=1, drop=True)
     top_actor = actors.value_counts().index[0]
     return f'El actor que más aparece en la plataforma {platform} y en el año {year} es {top_actor}'