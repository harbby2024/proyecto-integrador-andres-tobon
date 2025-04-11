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

with st.code():
info_libros ={"Titulo": ["Harry Potter y la piedra filosofa", "Lucky boy", "Atravez de ti","La Riqueza de las naciones"], 
            "Autor":["J. K. Rowling", "Shanthi Sekeran", "Ariana Godoy", "Adam Smith "], 
            "Año de publicación":[2000, 2017, 2021, 1992], 
            "Genero":["Ficción", "Drama" , "Romantica" , "Política" ]}

df_libros = pd.DataFrame(info_libros)
st.write(df_libros)
st.write(df_libros.describe())
with st.expander("Ver el código fuente"):
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

#Actividad 1 punto 03 Lista de Lista

st.subheader("DataFrames desde lista de lista")

inventario = [["sudadera manga larga", 20.000, 60], ["Jogger dama", 150.000, 120], ["Camiseta tipo polo", 90.000, 73]]

df_inventario = pd.DataFrame(inventario, columns=["Nombre de producto", "Precio", "Stock"])
st.dataframe(df_inventario)

#Actividad 1 punto 04  Series

st.subheader("DataFrames desde Series")

personas = pd.Series(["Andrés", "Daniel", "Johana","Esteban"])
edades = pd.Series([29, 29, 29,32])
ciudades = pd.Series(["Bello", "Sabaneta", "Bello","Bello"])

info_personas = pd.DataFrame({"Personas":personas , "Edad": edades, "Ciudad":ciudades})
st.dataframe(info_personas)

#Actividad 1 punto 04  Archivo CSV (local)

st.subheader("DataFrames desde Archivo CSV (local)")

data = pd.read_csv('static/datasets/data.csv')
st.dataframe(data)

#Actividad 1 punto 05  Archivo Excel

st.subheader("DataFrames desde Archivo Excel")

dataXlsx = pd.read_excel("static/datasets/data.xlsx")
st.dataframe(dataXlsx)

#Actividad 1 punto 06  Archivo JASON

st.subheader("DataFrames desde Archivo JASON")






#Crea tres Series separadas: una con nombres de personas, otra con sus edades y otra con sus ciudades (asegúrate de que tengan la misma cantidad de elementos, por ejemplo, 4 personas).
#Combina estas Series en un diccionario donde las claves sean los nombres de las columnas (como "nombre", "edad", "ciudad") y luego crea un DataFrame a partir de ese diccionario.
#En Streamlit, agrega un texto como "Datos de Personas" y usa st.dataframe() para mostrar el DataFrame

