import streamlit as st
def cells_per_ml():
    # Introducción manual del número de células contadas y el factor de dilución
    cells_counted = int(input("Introduce el número de células contadas por cuadrante: "))
    dilution_factor = int(input("Introduce el factor de dilución de la muestra: "))
    
    # Cálculo del número de células por mililitro
    cells_per_mm2 = cells_counted * 4  # Se cuentan las células en 4 cuadrantes
    cells_per_ml = cells_per_mm2 * 10**4 * dilution_factor
    return cells_per_ml

# Ejemplo de uso
result = cells_per_ml()
print(f"El número de células por mililitro es: {result}")import matplotlib.pyplot as plt



