import pandas as pd
import json
import logging
import os
import socket
import requests
from cryptography.fernet import Fernet
from sklearn.preprocessing import MinMaxScaler

# Configuración de logging
logging.basicConfig(
    filename="audit_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Obtención usuario e IP del sistema
def get_user_info():
    user = os.getlogin()
    ip = socket.gethostbyname(socket.gethostname())
    return user, ip


# Carga del JSON
def load_roles(config_file="config.json"):
    with open(config_file, "r") as f:
        return json.load(f)


roles = load_roles()

# Generar clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)


# Guardar clave de encriptación
def save_key(key, filename="clave.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)
    logging.info("Clave de encriptación generada y guardada correctamente.")


save_key(key)


# Función para verificar permisos
def check_access(role):
    if role not in roles:
        logging.warning(f"Acceso denegado: Rol {role} no registrado")
        raise PermissionError("Acceso denegado: Rol no registrado")
    return roles[role]["access_level"]


# Extraer datos desde CoinGecko API
def extract_data_from_api():
    api_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        logging.info("Datos extraídos exitosamente desde la API.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al extraer datos de la API: {e}")
        raise


# Guardar datos en CSV
def save_data_to_csv(data, filename="datos_cripto.csv"):
    df = pd.DataFrame([{
        "nombre": coin["name"],
        "simbolo": coin["symbol"],
        "precio_usd": coin["current_price"],
        "cambio_24h": coin["price_change_percentage_24h"],
        "capitalizacion_mercado": coin["market_cap"]
    } for coin in data])

    df.to_csv(filename, index=False)
    logging.info(f"Datos guardados en {filename} correctamente.")
    print(f"Datos guardados en {filename} correctamente.")


# Encriptar datos
def encrypt_file(filename, cipher):
    with open(filename, "rb") as file:
        datos = file.read()
    datos_encriptados = cipher.encrypt(datos)

    with open(f"{filename}.enc", "wb") as file:
        file.write(datos_encriptados)
    logging.info(f"Datos encriptados y guardados en {filename}.enc correctamente.")
    print(f"Datos encriptados y guardados en {filename}.enc correctamente.")


# Desencriptar datos
def decrypt_file(encrypted_filename, decrypted_filename, cipher):
    with open(encrypted_filename, "rb") as file:
        datos_encriptados = file.read()
    datos_desencriptados = cipher.decrypt(datos_encriptados)

    with open(decrypted_filename, "wb") as file:
        file.write(datos_desencriptados)
    logging.info(f"Datos desencriptados y guardados en {decrypted_filename} correctamente.")
    print(f"Datos desencriptados y guardados en {decrypted_filename} correctamente.")


if __name__ == "__main__":
    try:
        data = extract_data_from_api()
        save_data_to_csv(data)
        encrypt_file("datos_cripto.csv", cipher_suite)
        decrypt_file("datos_cripto.csv.enc", "datos_cripto_desencriptados.csv", cipher_suite)
    except Exception as e:
        logging.error(f"Error en el pipeline: {e}")
