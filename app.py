import streamlit as st
st.write('Calculadora de Celulas por mililitro, *World!* :sunglasses:')
def cells_per_ml():
    # Introducción manual del número de células contadas y el factor de dilución
    cells_counted = st.text_input("Celulas en total por los cuadrantes: ")
    dilution_factor = st.text_input("Introduce el factor de dilución de la muestra: ")
    
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    return cells_per_ml

# Ejemplo de uso
result = cells_per_ml() <module>
print(f"El número de células por mililitro es: {result}")





