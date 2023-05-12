import streamlit as st
import matplotlib.pyplot as plt

def cells_per_ml(cells_counted, dilution_factor):
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    return cells_per_ml

# Creamos una página de Streamlit para mostrar la interfaz gráfica
st.set_page_config(page_title="Cálculo de células y gráfica",
                   page_icon=":microscope:",
                   layout="wide")

st.title("Cálculo del número de células por mililitro y gráfica")
st.markdown("Este es un ejemplo de cómo calcular el número de células por mililitro a partir del número de células contadas y el factor de dilución. Además, puedes generar una gráfica para visualizar los resultados.")
st.markdown("---")

# Introducción manual del número de células contadas y el factor de dilución
cells_counted = st.number_input("Introduce el número de células contadas por cuadrante: ")
dilution_factor = st.number_input("Introduce el factor de dilución de la muestra: ")

# Calculamos el número de células por mililitro y lo mostramos en la página
if st.button("Calcular"):
    result = cells_per_ml(cells_counted, dilution_factor)
    st.write(f"El número de células por mililitro es: {result}")
    
    # Creamos una sección para la gráfica
    st.markdown("---")
    st.subheader("Gráfica de evolución de células")
    st.markdown("Puedes introducir los datos de la gráfica a continuación:")
    st.markdown("---")
    
    # Introducción manual de los datos de la gráfica
    days = st.text_input("Introduce los días contados (separados por comas): ")
    cells = st.text_input("Introduce el número de células por día (separados por comas): ")
    
    # Convertimos los datos de la gráfica en listas de números
    days_list = [int(x) for x in days.split(",")]
    cells_list = [int(x) for x in cells.split(",")]
    
    # Creamos la gráfica y la mostramos en la página
    if st.button("Crear gráfica"):
        fig, ax = plt.subplots()
        ax.plot(days_list, cells_list)
        ax.set_xlabel("Días contados")
        ax.set_ylabel("Número de células")
        ax.set_title("Evolución del número de células")
        st.pyplot(fig)






