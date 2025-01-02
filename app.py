import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model dari file pickle
with open('rf_model_before_normalization.pkl', 'rb') as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("Prediksi Kualitas Air")
st.write("Aplikasi ini memprediksi apakah air layak diminum atau tidak berdasarkan parameter kualitas air.")

# Input data pengguna
st.sidebar.header("Masukkan Parameter Kualitas Air")
ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
hardness = st.sidebar.slider("Hardness", 0.0, 500.0, 200.0)
solids = st.sidebar.slider("Solids", 0.0, 50000.0, 20000.0)
chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.sidebar.slider("Sulfate", 0.0, 500.0, 300.0)
conductivity = st.sidebar.slider("Conductivity", 0.0, 700.0, 400.0)
organic_carbon = st.sidebar.slider("Organic Carbon", 0.0, 30.0, 15.0)
trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 120.0, 60.0)
turbidity = st.sidebar.slider("Turbidity", 0.0, 10.0, 5.0)

# Buat DataFrame dari input pengguna
input_data = pd.DataFrame({
    'ph': [ph],
    'Hardness': [hardness],
    'Solids': [solids],
    'Chloramines': [chloramines],
    'Sulfate': [sulfate],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'Trihalomethanes': [trihalomethanes],
    'Turbidity': [turbidity]
})

# Tampilkan input pengguna
st.write("Data yang dimasukkan:")
st.write(input_data)

# Prediksi menggunakan model
if st.button("Prediksi"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Air ini **layak diminum**.")
    else:
        st.error("Air ini **tidak layak diminum**.")