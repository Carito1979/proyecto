"""
Imagina que esta API es una biblioteca de peliculas
la funciòn load_movies() es como una biblioteca que carga el catologo de libros (peliculas) cuandod se abre la biblioteca
la funcion get_movies() muestra el catalogo cuando alguien lo pide
la funcion get_movie(id) es como si alguien preguntara por un libro especifico es decir, por un codigo de identificaciòn
la funcion chatbot (query) es un asistente que busca peliculas segun palabras clave y sinonimo
la funcionget_movies_by_category(category) ayuda a encontrar peliculas segun su genero  (accion, comedia, etc...)
"""

# Importamos las herramientas necesarias para continuar nuestra API
from fastapi import FastAPI, HTTPException # FastAPI nos ayuda a crear la API, HTTPException nos ayuda a manejar errores
from fastapi.responses import HTMLResponse, JSONResponse # HTMLResponse nos ayuda a manejar respuestas HTML, JSONResponse nos ayuda a manejar respuestas en formato JSON
import pandas as pd # pandas nos ayuda a manejar datos en tablas como si fuera un Excel
import nltk # nltk es una libreria para procesar texto y analizar palabras
from nltk.tokenize import word_tokenize # word_tokenize nos ayuda a tokenizar texto, es decir, a convertirlo en palabras
from nltk.corpus import wordnet # wordnet es una libreria para analizar sinonimos

# indicamos la ruta donde nltk buscara los datos descargados en nuestro computador
nltk.data.path.append('c:\Users\dpinz\AppData\Roaming\nltk_data')
nltk.download('punkt')