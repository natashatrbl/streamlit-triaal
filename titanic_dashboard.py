import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout='wide')
st.title("Titanic Dashboard")

df = pd.read_csv(r"D:\PROJECT TASHA\PYTHON\learning\streamlit\data\titani_data.csv")

df['Embarked'] = df['Embarked'].fillna('Unknown')

