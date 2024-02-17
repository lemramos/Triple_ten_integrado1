import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Exploración de Anuncios de Venta de Coches')

# Crear botones o casillas de verificación para generar los gráficos
build_histogram = st.checkbox('Construir un Histograma de Odómetro')
build_scatter_plot = st.checkbox('Construir un Gráfico de Dispersión Precio vs. Año del Modelo')

# Histograma
if build_histogram:
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches - Odómetro')
    fig_histogram = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig_histogram, use_container_width=True)

# Gráfico de dispersión
if build_scatter_plot:
    st.write('Gráfico de Dispersión Precio vs. Año del Modelo')
    # Asegurarse de filtrar datos nulos para evitar errores en el gráfico
    filtered_data = car_data.dropna(subset=['price', 'model_year'])
    fig_scatter = px.scatter(filtered_data, x="model_year", y="price", title="Precio vs. Año del Modelo", color="fuel")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Configuración de Streamlit para Render
# No olvides agregar el archivo config.toml con las configuraciones indicadas a tu repositorio
