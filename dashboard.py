import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="AeroSight", layout="wide")
st.title("AeroSight: Satellite Weather Detection and Orbital Object Tracking")

if not Path("aerosight.db").exists():
    st.warning("No database yet. Run detect.py first.")
    st.stop()

con = sqlite3.connect("aerosight.db")
df = pd.read_sql("SELECT * FROM detections ORDER BY id DESC", con)
con.close()

c1, c2 = st.columns(2)
c1.metric("Photos analysed", len(df))
c2.metric("Weather types seen", df["weather"].nunique())

st.subheader("Detection results")
st.dataframe(df)

st.subheader("Weather count")
st.bar_chart(df["weather"].value_counts())

st.subheader("Annotated photos")
cols = st.columns(3)
for i, name in enumerate(df["photo"].unique()):
    path = Path("outputs") / name
    if path.exists():
        cols[i % 3].image(str(path), caption=name)
        st.subheader("Satellite orbit (ground track)")
if Path("orbit.csv").exists():
    orbit = pd.read_csv("orbit.csv")
    st.map(orbit[["lat", "lon"]])
else:
    st.info("Run orbit.py to see the orbit.")