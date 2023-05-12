import streamlit as st
pip install matplotlib
import matplotlib.st.pyplot as plt
import numpy as np

# Página 1: Conteo de células
def cell_count():
    st.write("# Conteo de células en cámara de Neubauer")
    cells_counted = st.number_input("Introduce el número de células contadas por cuadrante:", min_value=0, value=0, step=1)
    dilution_factor = st.number_input("Introduce el factor de dilución de la muestra:", min_value=0, value=0, step=1)
    
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    
    st.write(f"El número de células por mililitro es: {cells_per_ml}")

# Página 2: Graficador
def plot_data():
    st.write("# Graficador de datos")
    x = st.text_input("Introduce los valores del eje X (separados por comas):")
    y = st.text_input("Introduce los valores del eje Y (separados por comas):")
    
    # Convertir los valores a listas de números
    x_values = [float(val.strip()) for val in x.split(",")]
    y_values = [float(val.strip()) for val in y.split(",")]
    
    # Graficar los datos
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    st.pyplot(fig)

# Configuración de la barra lateral
pages = {
    "Conteo de células": cell_count,
    "Graficador de datos": plot_data
}
selection = st.sidebar.radio("Ir a", list(pages.keys()))

# Mostrar la página seleccionada
pages[selection]()




