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
Desarrollar una aplicación web interactiva utilizando Streamlit que permita a los usuarios explorar y manipular un DataFrame de Pandas, haciendo uso intensivo de los métodos .loc y .iloc para realizar selecciones, filtros y modificaciones de datos. La temática y el diseño de la aplicación son libres, permitiendo expresar su creatividad..
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
Desarrollar una aplicación web interactiva utilizando Streamlit que permita a los usuarios explorar y manipular un DataFrame de Pandas, haciendo uso intensivo de los métodos .loc y .iloc para realizar selecciones, filtros y modificaciones de datos. La temática y el diseño de la aplicación son libres, permitiendo expresar su creatividad.
""")

st.header("Solución")

data = {
    'Título': ['ICobra Kai', 'Ronja, la hija del bandolero', 'Cien años de soledad ', ' No Good Deed', 'Supacell'],
    'Año': [2018, 2024, 2024, 2024, 2024],
    'Temporadas': [6, 2,  1, 1, 1],
    'Episodios': [60, 12, 8, 8, 6]
}
df = pd.DataFrame(data)

st.title("🎬 Explorador de series de Netflix con .loc y .iloc")

st.markdown("Selecciona y modifica los datos del DataFrame utilizando `.loc` y `.iloc`.")

st.subheader("📊 DataFrame original")
st.dataframe(df)

st.subheader("🔍 Selección con .loc")

row_label = st.slider("Fila (índice):", 0, len(df)-1, 0)
column_label = st.selectbox("Columna:", df.columns)

if st.button("Mostrar valor con .loc"):
    value_loc = df.loc[row_label, column_label]
    st.success(f"Valor en .loc[{row_label}, '{column_label}']: {value_loc}")

st.subheader("🔍 Selección con .iloc")

row_index = st.slider("Fila (posición):", 0, len(df)-1, 0, key='iloc_row')
col_index = st.slider("Columna (posición):", 0, len(df.columns)-1, 0, key='iloc_col')

if st.button("Mostrar valor con .iloc"):
    value_iloc = df.iloc[row_index, col_index]
    st.success(f"Valor en .iloc[{row_index}, {col_index}]: {value_iloc}")

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
    df.to_csv("Series_netflix_modificado.csv", index=False)
    st.success("Archivo guardado como Series_netflix_modificado.csv")
