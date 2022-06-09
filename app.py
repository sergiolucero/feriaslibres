import pandas as pd
import streamlit as st
import pydeck as pdk
from datosmapa import capas
from streamlit_folium import st_folium
import folium
##################################
st.set_page_config(
    page_title="🍉Ferias Libres de Chile🍏", page_icon="🍅", layout="wide"
)

st.title("Ferias Libres de Chile")

fdf = pd.read_csv('FeriasLibresSantiago.csv')
m = folium.Map(location=[-33.5, -70.7], zoom_start=12)
for _, row in fdf.iterrows():
    folium.Marker(
        [row['Latitud'],row['Longitud']], 
        popup=row['Horarios'], tooltip=row['Nombre']
    ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)

#selected_layers = [capas['TODAS']]

#st.pydeck_chart(
#            pdk.Deck(
#                map_style="mapbox://styles/mapbox/light-v9",
#                initial_view_state={
#                    "latitude": -33.5,
#                    "longitude": -70.7,
#                    "zoom": 8,
#                    "pitch": 50,
#                },
#                layers=selected_layers,
#            )
#        )
st.dataframe(fdf)
