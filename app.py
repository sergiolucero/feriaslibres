import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Ferias Libres de Chile", page_icon="🍅", layout="wide"
)

st.title("Ferias Libres de Chile")

fdf = pd.read_csv('FeriasLibresSantiago.csv')
st.dataframe(fdf)
