import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""Usando el dataset estudiantes_colombia.csv, crea una aplicación en Streamlit que permita al usuario:
Ver las primeras 5 filas y las últimas 5 filas del dataset.
Mostrar un resumen con .info() y .describe().
Seleccionar columnas específicas (ej. "nombre", "edad", "promedio") para mostrarlas.
Filtrar estudiantes con promedio mayor a un valor definido por el usuario (usando un slider).
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Inspección y resumen de datos en dataset usando los métodos básicos como .head(), .tail(), .info(), .describe().
- Filtrado básico de filas y columnas
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

st.subheader("Columnas especificas nombre, edad y promedio")
st.write(df_estudiantes_colombia[["nombre", "edad","promedio"]])

st.subheader("Estudiantes con promedio mayor")
st.write(df_estudiantes_colombia[["nombre", "edad","promedio"]])

valor = st.selectbox(input("¿Quiere ver los valores mayores a? "))
