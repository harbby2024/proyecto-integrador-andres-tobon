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

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("DataFrames desde diferentes fuentes:")
st.subheader("Diccionario")

info_libros =[{"Titulo":"Harry Potter y la piedra filosofa", "Autor": "J. K. Rowling", "Año de publicación": 2000, "Genero": "Ficción" },
              {"Titulo":"Lucky boy", "Autor": "Shanthi Sekeran", "Año de publicación": 2017, "Genero": "Drama" },
              {"Titulo":"Atravez de ti", "Autor": "Ariana Godoy", "Año de publicación": 2021, "Genero": "Romantica" },
              {"Titulo":"La Riqueza de las naciones", "Autor": "Adam Smith ", "Año de publicación": 1992, "Genero": "Política" },
              ]

df_libros = pd.DataFlame(info_libros)

print(df_libros)