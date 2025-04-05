import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución Actividad #2 segundo momento")

df_estudiantes_colombia = pd.read_csv("static/estudiantes_colombia.csv")

st.header("Data base estudiantes Colombia")
st.dataframe(df_estudiantes_colombia)

st.subheader("Primeras 5 filas Dataset estudiantes Colombia")
st.write(df_estudiantes_colombia.head(5))

st.subheader("Ultimas 3 filas Dataset estudiantes Colombia")
st.write(df_estudiantes_colombia.tail(3))

st.subheader("Información Dataset estudiantes Colombia")
st.text(df_estudiantes_colombia.info())

st.subheader("Estadísticas descriptivas")
st.write(df_estudiantes_colombia.describe())





