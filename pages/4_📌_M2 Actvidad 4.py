import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

st.header("Solución")


# Datos de ejemplo
data = {
    'Título': ['Inception', 'The Matrix', 'Interstellar', 'Parasite', 'The Godfather'],
    'Año': [2010, 1999, 2014, 2019, 1972],
    'Género': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Drama', 'Crime'],
    'Rating': [8.8, 8.7, 8.6, 8.6, 9.2]
}
df = pd.DataFrame(data)

st.title("🎬 Explorador de Películas con .loc y .iloc")

st.markdown("Selecciona y modifica los datos del DataFrame utilizando `.loc` y `.iloc`.")

# Mostrar DataFrame original
st.subheader("📊 DataFrame original")
st.dataframe(df)

# Selección con .loc
st.subheader("🔍 Selección con .loc")

row_label = st.slider("Fila (índice):", 0, len(df)-1, 0)
column_label = st.selectbox("Columna:", df.columns)

if st.button("Mostrar valor con .loc"):
    value_loc = df.loc[row_label, column_label]
    st.success(f"Valor en .loc[{row_label}, '{column_label}']: {value_loc}")

# Selección con .iloc
st.subheader("🔍 Selección con .iloc")

row_index = st.slider("Fila (posición):", 0, len(df)-1, 0, key='iloc_row')
col_index = st.slider("Columna (posición):", 0, len(df.columns)-1, 0, key='iloc_col')

if st.button("Mostrar valor con .iloc"):
    value_iloc = df.iloc[row_index, col_index]
    st.success(f"Valor en .iloc[{row_index}, {col_index}]: {value_iloc}")

# Modificación con .loc
st.subheader("✏️ Modificar valor con .loc")

edit_row = st.number_input("Fila (índice) a editar:", min_value=0, max_value=len(df)-1, value=0)
edit_col = st.selectbox("Columna a editar:", df.columns, key='edit_col')
new_value = st.text_input("Nuevo valor:")

if st.button("Modificar valor"):
    df.loc[edit_row, edit_col] = new_value
    st.success(f"Valor modificado en .loc[{edit_row}, '{edit_col}']")
    st.dataframe(df)

# Guardar los cambios (opcional)
if st.button("💾 Guardar como CSV"):
    df.to_csv("peliculas_modificado.csv", index=False)
    st.success("Archivo guardado como peliculas_modificado.csv")
