import streamlit as st
import streamlit as st
import folium

# Creamos una función para generar el mapa
def generate_map():
    # Creamos el mapa centrado en una coordenada específica
    mapa = folium.Map(location=[19.4326, -99.1332], zoom_start=10)

    # Añadimos un marcador al mapa
    folium.Marker(location=[19.4326, -99.1332], popup="Ciudad de México").add_to(mapa)

    # Convertimos el mapa a HTML para mostrarlo en Streamlit
    map_html = folium.Map(location=[19.4326, -99.1332], zoom_start=10).get_root().render()
    return map_html

# Creamos una página de Streamlit para mostrar el mapa
st.title("Ejemplo de mapa con Streamlit y Folium")
st.markdown("Este es un ejemplo de cómo crear un mapa con Streamlit y Folium.")
st.markdown("---")
map_html = generate_map()
st.markdown(map_html, unsafe_allow_html=True)






