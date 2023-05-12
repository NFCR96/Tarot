import streamlit as st

# Agregar una barra lateral
options = ["Opción 1", "Opción 2", "Opción 3"]
selected_option = st.sidebar.selectbox("Selecciona una opción", options)

# Agregar widgets a la página principal
st.write(f"Has seleccionado: {selected_option}")
st.write("Este es el contenido de la página principal")


