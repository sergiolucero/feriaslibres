import pydeck as pdk

capas = {'TODAS': pdk.Deck(
            "ScatterplotLayer",
            data=from_data_file("FeriasLibresSantiago.csv"),
            get_position=["Longitud", "Latitud"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        }
