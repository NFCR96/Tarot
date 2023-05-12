import streamlit as st

# Página 1
def page1():
    st.write("Este es el contenido de la página 1")

# Página 2
def page2():
    st.write("Este es el contenido de la página 2")

# Configuración de la barra lateral
pages = {
    "Página 1": page1,
    "Página 2": page2
}
selection = st.sidebar.radio("Ir a", list(pages.keys()))

# Mostrar la página seleccionada
pages[selection]()



