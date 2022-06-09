import pandas as pd
import streamlit as st
import pydeck as pdk
from datosmapa import capas

st.set_page_config(
    page_title="🍉Ferias Libres de Chile🍏", page_icon="🍅", layout="wide"
)

st.title("Ferias Libres de Chile")

fdf = pd.read_csv('FeriasLibresSantiago.csv')

selected_layers = [capas['TODAS']]

st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": -33.5,
                    "longitude": -70.7,
                    "zoom": 8,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
st.dataframe(fdf)
