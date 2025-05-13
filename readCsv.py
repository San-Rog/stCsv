import pandas as pd
import streamlit as st
from datetime import date

df = pd.read_csv('feriadosNacionais.csv')
st.dataframe(data=df, hide_index=True) 
