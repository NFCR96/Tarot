import streamlit as st

st.sidebar.[Graficar]
def cells_per_ml(cells_counted, dilution_factor):
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    return cells_per_ml

# Creamos una página de Streamlit para mostrar la interfaz gráfica
st.title("Cálculo del número de células por mililitro")
st.markdown("Este es un ejemplo de cómo calcular el número de células por mililitro a partir del número de células contadas y el factor de dilución.")
st.markdown("---")

# Introducción manual del número de células contadas y el factor de dilución
cells_counted = st.number_input("Introduce el número de células contadas por cuadrante: ")
dilution_factor = st.number_input("Introduce el factor de dilución de la muestra: ")

# Calculamos el número de células por mililitro y lo mostramos en la página
if st.button("Calcular"):
    result = cells_per_ml(cells_counted, dilution_factor)
    st.write(f"El número de células por mililitro es: {result}")





