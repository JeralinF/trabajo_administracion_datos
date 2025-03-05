''''import sns
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
    st.write(f"Capitalización de mercado: {capitalizacion_mercado} USD")'''

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib
import seaborn as sns
import matplotlib.pyplot as plt


# Cargar el modelo entrenado y el escalador
def load_model_and_scaler():
    model = joblib.load("svm_model.pkl")
    scaler = joblib.load("scaler.pkl")  # Asegúrate de guardar el escalador al entrenar el modelo
    return model, scaler


# Función para predecir si el precio sube o baja
def predict_price_change(precio_usd, cambio_24h, capitalizacion_mercado, model, scaler):
    data = np.array([[precio_usd, cambio_24h, capitalizacion_mercado]])
    data_scaled = scaler.transform(data)  # Usar el escalador previamente ajustado
    prediction = model.predict(data_scaled)
    return prediction[0]


# Título de la app
st.title("Clasificador de Cambio de Precio de Criptomonedas")
st.markdown(
    "### Ingresa los valores para predecir si el precio de una criptomoneda subirá o bajará en las próximas 24 horas.")

# Crear columnas para entradas del usuario
col1, col2, col3 = st.columns(3)

with col1:
    precio_usd = st.number_input("Precio en USD", min_value=0.0, value=100.0,
                                 help="Precio actual de la criptomoneda en USD")

with col2:
    cambio_24h = st.number_input("Cambio en 24h (%)", min_value=-100.0, value=0.0, help="Cambio porcentual en 24 horas")

with col3:
    capitalizacion_mercado = st.number_input("Capitalización de Mercado (en USD)", min_value=0.0, value=1000000.0,
                                             help="Capitalización de mercado actual en USD")

# Predecir el cambio de precio
if st.button("Predecir", key="predict_button"):
    # Validación de entradas
    if precio_usd <= 0:
        st.warning("El precio en USD debe ser mayor que 0.")
    elif cambio_24h < -100 or cambio_24h > 100:
        st.warning("El cambio en 24h debe estar entre -100 y 100.")
    elif capitalizacion_mercado <= 0:
        st.warning("La capitalización de mercado debe ser mayor que 0.")
    else:
        model, scaler = load_model_and_scaler()
        prediction = predict_price_change(precio_usd, cambio_24h, capitalizacion_mercado, model, scaler)

        # Mostrar el resultado
        if prediction == 1:
            st.success("El precio de la criptomoneda subirá.")
        else:
            st.error("El precio de la criptomoneda bajará.")

        # Mostrar una tabla con los datos de entrada
        st.markdown("### Datos de entrada para la predicción:")
        input_data = pd.DataFrame({
            'Precio en USD': [precio_usd],
            'Cambio en 24h (%)': [cambio_24h],
            'Capitalización de mercado (USD)': [capitalizacion_mercado]
        })
        st.write(input_data)

        # Visualización de datos de entrada
        st.markdown("### Visualización de datos:")
        fig, ax = plt.subplots()
        sns.barplot(data=input_data, orient='h', ax=ax)
        st.pyplot(fig)

        # Guardar la predicción en el historial
        if 'predictions' not in st.session_state:
            st.session_state['predictions'] = []

        st.session_state['predictions'].append({
            'Precio en USD': precio_usd,
            'Cambio en 24h (%)': cambio_24h,
            'Capitalización de mercado (USD)': capitalizacion_mercado,
            'Predicción': 'Subirá' if prediction == 1 else 'Bajará'
        })

        # Mostrar el historial de predicciones
        st.markdown("### Historial de Predicciones")
        st.write(pd.DataFrame(st.session_state['predictions']))
