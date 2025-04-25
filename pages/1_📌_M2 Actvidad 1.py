import pymongo
import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from pymongo import MongoClient
import os

# Configuración de la página
st.set_page_config(
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1 - Creación de DataFrames")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

#Actividad 1 punto 01 Dataframes Diccionario

st.header("Objetivo de la actividad")
st.markdown("Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.")

st.title("DataFrames desde diferentes fuentes:")
st.subheader("DataFrames desde Diccionario")

info_libros ={"Titulo": ["Harry Potter y la piedra filosofa", "Lucky boy", "Atravez de ti","La Riqueza de las naciones"], 
            "Autor":["J. K. Rowling", "Shanthi Sekeran", "Ariana Godoy", "Adam Smith "], 
            "Año de publicación":[2000, 2017, 2021, 1992], 
            "Genero":["Ficción", "Drama" , "Romantica" , "Política" ]}

df_libros = pd.DataFrame(info_libros)
st.write(df_libros)
st.write(df_libros.describe())

#Vista de codigo -- Actividad 1 punto 01 Dataframes Diccionario

codigo = '''
import streamlit as st
import pandas as pd

info_libros = {
    "Titulo": ["Harry Potter y la piedra filosofal", "Lucky boy", "A través de ti", "La Riqueza de las Naciones"], 
    "Autor": ["J. K. Rowling", "Shanthi Sekeran", "Ariana Godoy", "Adam Smith"], 
    "Año de publicación": [2000, 2017, 2021, 1992], 
    "Genero": ["Ficción", "Drama", "Romántica", "Política"]
}

df_libros = pd.DataFrame(info_libros)
st.write(df_libros)
st.write(df_libros.describe())
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 02 Dataframes lista de Diccionario

st.subheader("DataFrames desde Lista de Diccionario")

poblacion_ciudades =[{"Nombre":"Tokio", "Población": "37,3 millones de habitantes.", "Pais":"Japón"},
            {"Nombre":"Delhi", "Población": "29,3 millones de habitantes. ​", "Pais":"India" },
            {"Nombre":"Shanghái", "Población": "26,3 millones de habitantes.", "Pais":"China" },
            {"Nombre":"São Paulo", "Población": "22 millones de habitantes.", "Pais":"Brasil"},]

df_poblacion_ciudades = pd.DataFrame(poblacion_ciudades)

st.markdown("Población de las ciudades más grandes del mundo")
st.dataframe(df_poblacion_ciudades)

#Vista de codigo -- Actividad 1 punto 02 Dataframes lista de Diccionario

codigo = '''
import streamlit as st
import pandas as pd
poblacion_ciudades =[{"Nombre":"Tokio", "Población": "37,3 millones de habitantes.", "Pais":"Japón"},
            {"Nombre":"Delhi", "Población": "29,3 millones de habitantes. ​", "Pais":"India" },
            {"Nombre":"Shanghái", "Población": "26,3 millones de habitantes.", "Pais":"China" },
            {"Nombre":"São Paulo", "Población": "22 millones de habitantes.", "Pais":"Brasil"},]

df_poblacion_ciudades = pd.DataFrame(poblacion_ciudades)

st.markdown("Población de las ciudades más grandes del mundo")
st.dataframe(df_poblacion_ciudades)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')


#Actividad 1 punto 03 Lista de Lista

st.subheader("DataFrames desde lista de lista")

inventario = [["sudadera manga larga", 20.000, 60], ["Jogger dama", 150.000, 120], ["Camiseta tipo polo", 90.000, 73]]

df_inventario = pd.DataFrame(inventario, columns=["Nombre de producto", "Precio", "Stock"])
st.dataframe(df_inventario)

#Vista de codigo -- Actividad 1 punto 03 Lista de Lista

codigo = '''
import streamlit as st
import pandas as pd

inventario = [["sudadera manga larga", 20.000, 60], ["Jogger dama", 150.000, 120], ["Camiseta tipo polo", 90.000, 73]]

df_inventario = pd.DataFrame(inventario, columns=["Nombre de producto", "Precio", "Stock"])
st.dataframe(df_inventario)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 04  Series

st.subheader("DataFrames desde Series")

personas = pd.Series(["Andrés", "Daniel", "Johana","Esteban"])
edades = pd.Series([29, 29, 29,32])
ciudades = pd.Series(["Bello", "Sabaneta", "Bello","Bello"])

info_personas = pd.DataFrame({"Personas":personas , "Edad": edades, "Ciudad":ciudades})
st.dataframe(info_personas)

#Vista de codigo -- Actividad 1 punto 04  Series

codigo = '''
import streamlit as st
import pandas as pd

personas = pd.Series(["Andrés", "Daniel", "Johana","Esteban"])
edades = pd.Series([29, 29, 29,32])
ciudades = pd.Series(["Bello", "Sabaneta", "Bello","Bello"])

info_personas = pd.DataFrame({"Personas":personas , "Edad": edades, "Ciudad":ciudades})
st.dataframe(info_personas)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')


#Actividad 1 punto 05  Archivo CSV (local)

st.subheader("DataFrames desde Archivo CSV (local)")

data = pd.read_csv('static/datasets/data.csv')
st.dataframe(data)

#Vista de codigo -- Actividad 1 punto 05  Archivo CSV (local)

codigo = '''
import streamlit as st
import pandas as pd

data = pd.read_csv('static/datasets/data.csv')
st.dataframe(data)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 06  Archivo Excel

st.subheader("DataFrames desde Archivo Excel")

dataXlsx = pd.read_excel("static/datasets/data.xlsx")
st.dataframe(dataXlsx)

#Vista de codigo -- Actividad 1 punto 06  Archivo Excel

codigo = '''
import streamlit as st
import pandas as pd

dataXlsx = pd.read_excel("static/datasets/data.xlsx")
st.dataframe(dataXlsx)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 07  Archivo JASON

st.subheader("DataFrames desde Archivo JASON")

dato_cliente = pd.read_json("static/datasets/data.json")
st.dataframe(dato_cliente)

#Vista de codigo -- Actividad 1 punto 07  Archivo JASON

codigo = '''
import streamlit as st
import pandas as pd

dato_cliente = pd.read_json(".static/datasets/data.json")
st.dataframe(dato_cliente)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')


#Actividad 1 punto 08 URL

st.subheader("DataFrames desde URL")

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
datos = pd.read_csv(url)
st.dataframe(datos)

#Vista de codigo -- Actividad 1 punto 08 URL
codigo = '''
import streamlit as st
import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
datos = pd.read_csv(url)
st.dataframe(datos)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 09 Base de datos SQLite

st.subheader("DataFrames desde Base de datos SQLite")

conn = sqlite3.connect('static/estudiantes.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    calificacion INTEGER NOT NULL
)
''')
cursor.executemany('''
INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)
''', [
    ('Ana', 85),
    ('Luis', 90),
    ('Carlos', 78)
])

conn.commit()
consulta_sql = "SELECT * FROM estudiantes"
df = pd.read_sql(consulta_sql, conn)

import streamlit as st

st.dataframe(df)

conn.close()

#Vista de codigo -- Actividad 1 punto 09 Baase de datos SQLite
codigo = '''
import streamlit as st
import pandas as pd

conn = sqlite3.connect('static/estudiantes.db')
cursor = conn.cursor()
cursor.execute('
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    calificacion INTEGER NOT NULL
)
')
cursor.executemany('
INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)
', [
    ('Ana', 85),
    ('Luis', 90),
    ('Carlos', 78)
])

conn.commit()
consulta_sql = "SELECT * FROM estudiantes"
df = pd.read_sql(consulta_sql, conn)

import streamlit as st

st.dataframe(df)

conn.close()
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 10  Archivo Excel

st.subheader("DataFrames Array de NumPy")

cosas = np.array([["zapatos","Samsung" ,7 ],
                                ["camisa", "Apple",  8],
                                ["jeans","Oppo", 9]])

df_array = pd.DataFrame(cosas, columns=['Ropa', 'Marcas tecnolog+ia', 'numeros'])

st.dataframe(df_array)

#Vista de codigo -- Actividad 1 punto 09 Baase de datos SQLite
codigo = '''
import streamlit as st
import pandas as pd
import numpy as np

cosas = np.array([["zapatos","Samsung" ,7 ],
                                ["camisa", "Apple",  8],
                                ["jeans","Oppo", 9]])

df_array = pd.DataFrame(cosas, columns=['Ropa', 'Marcas tecnología', 'numeros'])

st.dataframe(df_array)
'''
with st.expander("👀 Ver el código fuente"):
    st.code(codigo, language='python')

#Actividad 1 punto 10  desde Firebase

st.subheader("DataFrames desde Firebase")






#______________________Actividad 1 punto 09 Base de datos SQLite

st.subheader("DataFrames desde Base de datos SQLite")


#Actividad 1 punto 12 desde MongoDBdd

st.subheader("DataFrames desde MongoDB")
clientes = MongoClient("mongodb+srv://harbby:3206912806andres@cluster0.f5ft4fz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Seleccionar la base de datos y la colección
db = clientes["clientes_data"]  # Nombre de la base de datos
coleccion = db["clientes"]      # Nombre de la colección

# Recuperar los documentos de la colección


df = pd.DataFrame(coleccion)

st.dataframe(df)
