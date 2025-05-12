import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad 1 Practica de filtrado en Pandas (Google Colab)")
st.markdown("""
Esta actividad está diseñada para que practiques las técnicas de filtrado en Pandas explicadas previamente (operadores de comparación, lógicos, isin, query, where, mask, str, between, isnull, notnull y fechas). Usa el DataFrame creado (df_nuevo) para resolver los siguientes 30 ejercicios. Cada ejercicio incluye una instrucción clara y el método de filtrado sugerido, aunque puedes experimentar con otros enfoques si lo deseas.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Aplicar técnicas de filtrado de datos en Pandas utilizando operadores de comparación y operadores lógicos.
- Utilizar métodos específicos de Pandas para el filtrado, tales como isin(), query(), where(), mask(), str, between(), isnull() y notnull().
""")

st.header("Solución de Actividad")


# Crear un DataFrame de ejemplo con datos de salud
data = {
    'edad': np.random.randint(15, 90, size=100),
    'municipio': np.random.choice(['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'], size=100),
    'colesterol': np.random.randint(100, 300, size=100),  # Nivel de colesterol
    'enfermedad': np.random.choice(['Hipertensión', 'Diabetes', 'Asma', 'Cancer', 'Obesidad', 'Artritis'], size=100),
    'fecha_diagnostico': pd.to_datetime(np.random.randint(2010, 2024, size=100), format='%Y'),
    'tipo_tratamiento': np.random.choice(['Medicamento', 'Cirugía', 'Terapia', 'Dieta'], size=100),
    'acceso_atencion': np.random.choice([True, False], size=100),
    'ingreso_mensual': np.random.choice([np.nan, *range(800000, 12000000)], size=100),  # Con valores nulos
    'nombre_completo': ['Paciente ' + str(i) for i in range(1, 101)],
}

df_salud = pd.DataFrame(data)

# Barra lateral
st.sidebar.title('Filtros Interactivos de Salud')

# 1. Filtro por rango de edad
activar_edad = st.sidebar.checkbox("Filtrar por rango de edad")
if activar_edad:
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 90, (15, 90))
    df_salud = df_salud[df_salud['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios
activar_municipios = st.sidebar.checkbox("Filtrar por municipios")
if activar_municipios:
    municipios_seleccionados = st.sidebar.multiselect(
        "Selecciona los municipios", 
        ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'],
        default=['Barranquilla', 'Santa Marta']
    )
    if municipios_seleccionados:
        df_salud = df_salud[df_salud['municipio'].isin(municipios_seleccionados)]

# 3. Filtro por nivel de colesterol
activar_colesterol = st.sidebar.checkbox("Filtrar por nivel de colesterol")
if activar_colesterol:
    colesterol_minimo = st.sidebar.slider("Selecciona el nivel mínimo de colesterol", 100, 300, 200)
    df_salud = df_salud[df_salud['colesterol'] >= colesterol_minimo]

# 4. Filtro por enfermedad
activar_enfermedad = st.sidebar.checkbox("Filtrar por enfermedad")
if activar_enfermedad:
    enfermedades_seleccionadas = st.sidebar.multiselect(
        "Selecciona las enfermedades", 
        ['Hipertensión', 'Diabetes', 'Asma', 'Cancer', 'Obesidad', 'Artritis']
    )
    if enfermedades_seleccionadas:
        df_salud = df_salud[df_salud['enfermedad'].isin(enfermedades_seleccionadas)]

# 5. Filtro por tratamiento
activar_tratamiento = st.sidebar.checkbox("Filtrar por tipo de tratamiento")
if activar_tratamiento:
    tratamientos_seleccionados = st.sidebar.multiselect(
        "Selecciona el tipo de tratamiento", 
        ['Medicamento', 'Cirugía', 'Terapia', 'Dieta']
    )
    if tratamientos_seleccionados:
        df_salud = df_salud[df_salud['tipo_tratamiento'].isin(tratamientos_seleccionados)]

# 6. Filtro por nombres que contienen una cadena
activar_nombre = st.sidebar.checkbox("Filtrar por nombre")
if activar_nombre:
    texto = st.sidebar.text_input("Ingresa la subcadena para filtrar por nombre")
    if texto:
        df_salud = df_salud[df_salud['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de diagnóstico
activar_fecha_diagnostico = st.sidebar.checkbox("Filtrar por año de diagnóstico")
if activar_fecha_diagnostico:
    año_seleccionado = st.sidebar.selectbox("Selecciona el año de diagnóstico", list(range(2010, 2024)))
    df_salud = df_salud[df_salud['fecha_diagnostico'].dt.year == año_seleccionado]

# 8. Filtro por acceso a atención médica
activar_acceso = st.sidebar.checkbox("Filtrar por acceso a atención médica")
if activar_acceso:
    acceso = st.sidebar.radio("¿Tiene acceso a atención médica?", ["Sí", "No"])
    if acceso == "Sí":
        df_salud = df_salud[df_salud['acceso_atencion'] == True]
    else:
        df_salud = df_salud[df_salud['acceso_atencion'] == False]

# 9. Filtro por ingresos nulos
activar_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos")
if activar_ingresos_nulos:
    df_salud = df_salud[df_salud['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de diagnóstico
activar_fechas_diagnostico = st.sidebar.checkbox("Filtrar por rango de fechas de diagnóstico")
if activar_fechas_diagnostico:
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", min_value=pd.to_datetime('2010-01-01'), max_value=pd.to_datetime('2023-12-31'))
    fecha_fin = st.sidebar.date_input("Fecha de fin", min_value=pd.to_datetime('2010-01-01'), max_value=pd.to_datetime('2023-12-31'))
    df_salud = df_salud[df_salud['fecha_diagnostico'].between(fecha_inicio, fecha_fin)]

# Mostrar los datos filtrados
st.write(df_salud)



