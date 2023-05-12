import streamlit as st

# Página 1
def page1():
    st.write("Contador de celulas")

# Página 2
def page2():
    st.write("Graficador de curva")

# Configuración de la barra lateral
pages = {
    "Página 1": page1,
    "Página 2": page2
}
selection = st.sidebar.radio("Ir a", list(pages.keys()))

# Mostrar la página seleccionada
pages[selection]()



