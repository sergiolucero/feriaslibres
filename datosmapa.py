import pydeck as pdk
import pandas as pd

capas = {'TODAS': pdk.Layer(
            "ScatterplotLayer",
            data=pd.read_csv("FeriasLibresSantiago.csv"),
            get_position=["Latitud", "Longitud"],
            get_color=[200, 30, 0, 160],
            get_radius=5,
            radius_scale=0.05,
        ),
        }
