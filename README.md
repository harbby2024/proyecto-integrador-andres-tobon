# Aplicación Streamlit - Nuevas Tecnologías de Programación

Este proyecto es una aplicación web desarrollada con Streamlit que permite visualizar y completar las actividades y evaluaciones del curso de Nuevas Tecnologías de Programación del programa de Desarrollo de Software.

## Características

- Interfaz de usuario intuitiva y responsive
- Múltiples páginas organizadas por momentos y actividades
- Estructura de proyecto organizada y mantenible
- Secciones específicas para cada actividad y evaluación

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona o descarga este repositorio en tu computadora

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv .venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación:

```
streamlit run Inicio.py
```

La aplicación estará disponible en tu navegador en `http://localhost:8501`.

## Estructura del proyecto

```
├── .streamlit/            # Configuración de Streamlit
│   └── config.toml        # Archivo de configuración (tema, servidor, etc.)
├── assets/                # Recursos estáticos
│   ├── foto.jpg           # Foto del estudiante
│   └── logo-Cesde-2023.svg # Logo de CESDE
├── data/                  # Carpeta para almacenar datos
├── pages/                 # Páginas de la aplicación
│   ├── 1_📌_M2 Actvidad 1.py   # Actividad 1 del Momento 2
│   ├── 2_📌_M2 Actvidad 2.py   # Actividad 2 del Momento 2
│   ├── 3_📌_M2 Actvidad 3.py   # Actividad 3 del Momento 2
│   ├── 4_📌_M2 Actvidad 4.py   # Actividad 4 del Momento 2
│   ├── 5_📌_M2 Actvidad 5.py   # Actividad 5 del Momento 2
│   ├── 6_📋_M2 Evaluación.py   # Evaluación del Momento 2
│   ├── 7_📌_M3 Actvidad 1.py   # Actividad 1 del Momento 3
│   ├── 8_📌_M3 Actvidad 2.py   # Actividad 2 del Momento 3
│   ├── 9_📌_M3 Actvidad 3.py   # Actividad 3 del Momento 3
│   ├── 10_📌_M3 Actvidad 4.py  # Actividad 4 del Momento 3
│   ├── 11_📌_M3 Actvidad 5.py  # Actividad 5 del Momento 3
│   └── 12_📋_M3 Evaluación.py  # Evaluación del Momento 3
├── .gitignore             # Archivos ignorados por Git
├── Inicio.py              # Punto de entrada de la aplicación
├── README.md              # Este archivo
└── requirements.txt       # Dependencias del proyecto
```

## Navegación por la aplicación

1. **Página de inicio (Inicio.py)**: Muestra información general del estudiante y del curso.

2. **Actividades del Momento 2**: Páginas numeradas del 1 al 5, cada una contiene una actividad específica del Momento 2.

3. **Evaluación del Momento 2**: Página 6, contiene la evaluación final del Momento 2.

4. **Actividades del Momento 3**: Páginas numeradas del 7 al 11, cada una contiene una actividad específica del Momento 3.

5. **Evaluación del Momento 3**: Página 12, contiene la evaluación final del Momento 3.

## Personalización

### Información del estudiante

Para personalizar la información del estudiante, edita el archivo `Inicio.py` y modifica los siguientes elementos:

1. Reemplaza la imagen `assets/foto.jpg` con tu propia foto.
2. Actualiza la información personal (nombre, programa, semestre, enlace al repositorio).

### Completar actividades

Para completar cada actividad o evaluación:

1. Navega a la página correspondiente desde la barra lateral.
2. Lee la descripción y objetivos de la actividad.
3. Implementa tu solución en la sección designada.
4. Guarda los cambios y actualiza la página para ver los resultados.

## Dependencias principales

- streamlit: Framework para crear aplicaciones web interactivas
- pandas: Manipulación y análisis de datos
- numpy: Computación numérica
- matplotlib y seaborn: Visualización de datos
- plotly: Gráficos interactivos

Consulta el archivo `requirements.txt` para ver la lista completa de dependencias.

## Consejos para el desarrollo

- Utiliza la función `st.help()` para obtener ayuda sobre cualquier función de Streamlit.
- Consulta la [documentación oficial de Streamlit](https://docs.streamlit.io/) para más información.
- Utiliza `st.write()` para depurar variables durante el desarrollo.
- Aprovecha los widgets interactivos de Streamlit para hacer tus actividades más dinámicas.

