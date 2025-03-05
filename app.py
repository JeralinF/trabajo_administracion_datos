import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar el modelo entrenado
def load_model():
    # Si has guardado tu modelo en un archivo con joblib, lo puedes cargar aquí
    model = joblib.load("svm_model.pkl")
    return model

# Función para predecir si el precio sube o baja
def predict_price_change(precio_usd, cambio_24h, capitalizacion_mercado, model):
    data = np.array([[precio_usd, cambio_24h, capitalizacion_mercado]])
    # Escalar los datos
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    prediction = model.predict(data_scaled)
    return prediction[0]

# Título de la app
st.title("Clasificador de Cambio de Precio de Criptomonedas")

# Instrucciones
st.write("Ingresa los valores para predecir si el precio de una criptomoneda subirá o bajará en las próximas 24 horas.")

# Recibir entradas del usuario
precio_usd = st.number_input("Precio en USD", min_value=0.0, value=100.0)
cambio_24h = st.number_input("Cambio en 24h (%)", min_value=-100.0, value=0.0)
capitalizacion_mercado = st.number_input("Capitalización de Mercado (en USD)", min_value=0.0, value=1000000.0)

# Predecir el cambio de precio
if st.button("Predecir"):
    # Cargar el modelo SVM
    model = load_model()

    # Realizar la predicción
    prediction = predict_price_change(precio_usd, cambio_24h, capitalizacion_mercado, model)

    # Mostrar el resultado
    if prediction == 1:
        st.success("El precio de la criptomoneda subirá.")
    else:
        st.error("El precio de la criptomoneda bajará.")

    # Mostrar una tabla con los datos de entrada
    st.write("Datos de entrada para la predicción:")
    st.write(f"Precio en USD: {precio_usd}")
    st.write(f"Cambio en 24h: {cambio_24h}%")
    st.write(f"Capitalización de mercado: {capitalizacion_mercado} USD")


