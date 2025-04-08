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

st.header("Objetivo de la actividad")
st.markdown("Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.")

st.header("DataFrames desde diferentes fuentes:")
st.subheader("DataFrames desde Diccionario")
info_libros ={"Titulo": ["Harry Potter y la piedra filosofa", "Lucky boy", "Atravez de ti","La Riqueza de las naciones"]},
            { "Autor": ["J. K. Rowling", "Shanthi Sekeran", "Ariana Godoy", "Adam Smith "] },
            { "Año de publicación":[2000, 2017, 2021, 1992] },
            {"Genero":["Ficción", "Drama" , "Romantica" , "Política" ]},

df_libros = pd.DataFrame(info_libros)
st.write(df_libros)
st.write(df_libros.describe())





