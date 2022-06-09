import pydeck as pdk
import pandas as pd

capas = {'TODAS': pdk.Deck(
            "ScatterplotLayer",
            data=pd.read_csv("FeriasLibresSantiago.csv"),
            get_position=["Longitud", "Latitud"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        }
