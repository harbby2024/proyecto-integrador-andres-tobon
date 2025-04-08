import streamlit as st
import pandas as pd

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

#Actividad 1 punto 02 Dataframes lista de Diccionario

st.subheader("DataFrames desde Lista de Diccionario")

poblacion_ciudades =[{"Nombre":"Tokio", "Población": "37,3 millones de habitantes.", "Pais":"Japón"},
            {"Nombre":"Delhi", "Población": "29,3 millones de habitantes. ​", "Pais":"India" },
            {"Nombre":"Shanghái", "Población": "26,3 millones de habitantes.", "Pais":"China" },
            {"Nombre":"São Paulo", "Población": "22 millones de habitantes.", "Pais":"Brasil"},]

df_poblacion_ciudades = pd.DataFrame(poblacion_ciudades)

st.subheader("Población de las ciudades más grandes del mundo")
st.dataframe(df_poblacion_ciudades)

#Actividad 1 punto 03 Lista de Lista

st.subheader("DataFrames desde lista de lista")

inventario = [["sudadera manga larga", 20.000, 60], ["Jogger dama", 150.000, 120], ["Camiseta tipo polo", 90.000, 73]]

df_inventario = pd.DataFrame(inventario, columns=["Nombre de producto", "Precio", "Stock"])
st.dataframe(df_inventario)

#nombre del producto, precio y cantidad en stock
#Convierte esta lista en un DataFrame con Pandas, especificando los nombres de las columnas (pista: usa el parámetro columns en la función de creación).
#En Streamlit, añade un texto como "Productos en Inventario" y muestra el DataFrame con st.dataframe().

