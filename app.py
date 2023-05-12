import streamlit as st
import matplotlib.pyplot as plt

def cells_per_ml():
    # Introducción manual del número de células contadas y el factor de dilución
    cells_counted = st.number_input("Introduce el número de células contadas por cuadrante: ")
    dilution_factor = st.number_input("Introduce el factor de dilución de la muestra: ")
    
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    
    # Gráfica de los datos ingresados
    days = st.text_input("Ingrese los días contados separados por comas:")
    days_list = [int(x) for x in days.split(",")]
    plt.plot(days_list, [cells_per_ml]*len(days_list), 'ro')
    plt.xlabel('Días')
    plt.ylabel('Número de células')
    st.sidebar.pyplot()
    
    return cells_per_ml

# Crear una gráfica vacía en la barra lateral
st.sidebar.subheader("Gráfica de células por día")
plt.figure()
st.sidebar.pyplot()

# Ejemplo de uso
result = cells_per_ml()
st.write(f"El número de células por mililitro es: {result}")






