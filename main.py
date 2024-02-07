from funciones import *
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
def bienvenida():
    return {'API de consultas a una base de datos de Steam desarrollada por JUAN CARLOS SANCHEZ COTES, en proyecto PI_ML_OPS de HENRY,/docs en el link para acceder a las funciones de consulta.'}

#Cantidad de elementos y porcentaje de juegos gratuitos por desarrollador
@app.get('/developer/{desarrollador}')
def developer(desarrollador:str):
    """
    Esta función realiza el cálculo para un desarrollador de juegos y proporciona la cantidad de elementos junto con el porcentaje de contenido gratuito para cada año.
    params:
    desarrollador:str Desarrolador
    """
    try:
        return developer_func(desarrollador)
    except Exception as e:
        return {"Error":str(e)}

#Cantidad de dinero invertido por usuario  
@app.get('/user{user}')
def userdata(user:str):
    """
    Esta función ofrece para un usuario la cantidad de dinero invertido, el número de elementos adquiridos y el porcentaje de recomendaciones positivas en relación con el total de sus sugerencias.
    params:
    user:str ID de un usuario
    """
    try:
        return userdata_func(user)
    except Exception as e:
        return {"Error":str(e)}

#Usuario con mas horas de juego por genero
@app.get('/genero')
def UserForGenre(genero:str):
    """
   Esta función proporciona, para un género específico, el usuario que ha dedicado más horas desde el lanzamiento del juego, junto con la cantidad total de horas acumuladas en cada año.
    params:
    genero:str Genero de un juego
    """
    try:
        return UserForGenre_func(genero)
    except Exception as e:
        return {"Error":str(e)}

#ranking desarrolladores por año    
@app.get('/best_developer_year/{year}')   
def best_developer_year(year:int):
    """
    Esta función determina, para un año específico, el ranking de los tres desarrolladores con la mayor cantidad de juegos.
    params:
    year:int : Año
    """
    try:
        return best_developer_year_func(year)
    except Exception as e:
        return {"Error":str(e)}

#Cantidad de reseñas por desarrollador, positivas y negativas.  
@app.get('/recommend/{developer_rec}') 
def developer_rec(developer_rec:str):
    """
    Esta función evalúa la cantidad de usuarios que han proporcionado reseñas positivas y negativas para un desarrollador específico.
    params:
    developer_rec:str : Desarrolador
    """
    try:
        return developer_rec_func(developer_rec)
    except Exception as e:
        return {"Error":str(e)}

# Sugerencia por usuario
@app.get('/recommend_user_games/{user}') 
def ser_recommend(user:str):
    """
    Esta función sugiere los 5 juegos más destacados para un usuario específico.
    Params:
    user:str - Usuario al que se le esta realizando la sugerencia de los juegos.
    Returns:
    Un diccionario con los 5 juegos sugeridos para ese usuario.
    """
    try:
        return user_recommend_fuc(user)
    except Exception as e:
        return {"Error":str(e)}

# Sugerencia por item
@app.get('/recommend_item/{item}') 
def item_recommend(item_id:int):
    """
    Esta función sugiere 5 items  dado un item especifico.
    Params:
    item_id:int - id del item del cual se quieren sugerir.
    Returns:
    Un diccionario con los 5 juegos sugeridos.
    """
    try:
        return item_recommend_func(item_id)
    except Exception as e:
        return {"Error":str(e)}