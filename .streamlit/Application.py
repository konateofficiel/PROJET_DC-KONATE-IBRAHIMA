import streamlit as st
import pandas as pd
import numpy as np


st.markdown("<h2 style='text-align: center; color: black;'>Application de projet de data collection</h2>", unsafe_allow_html=True)

st.markdown("""
Cette application affiche les données issues du site expa-dakar
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")


# Fonction de loading des données
def charge(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
charge(pd.read_csv('data/motos_scooters1.csv'), 'Motocycles data 1', '1')
charge(pd.read_csv('data/motos_scooters2.csv'), 'Motocycles data 2', '2')
charge(pd.read_csv('data/motos_scooters3.csv'), 'Motocycles data 3', '3')
charge(pd.read_csv('data/motos_scooters4.csv'), 'Motocycles data 4', '4')
charge(pd.read_csv('data/motos_scooters5.csv'), 'Motocycles data 5', '5')




 


