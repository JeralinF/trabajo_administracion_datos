# Predicción del Precio de Criptomonedas

Este proyecto utiliza un modelo de Máquina de Vectores de Soporte (SVM)
para predecir si el precio de una criptomoneda subirá o bajará en las próximas 24 horas,
basándose en datos como el precio actual, el cambio en las últimas 24 horas y la capitalización de mercado.

## Índice

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

Este proyecto tiene como objetivo predecir los movimientos de los precios de las criptomonedas usando datos históricos de precios, cambios en las 24 horas y capitalización de mercado. Utiliza el modelo de clasificación SVM para determinar si el precio subirá o bajará en las próximas 24 horas.

El modelo se entrena con datos extraídos de un archivo CSV y está listo para predecir en función de las entradas del usuario.

## Instalación

### Requisitos previos

- Python 3.x
- Librerías: `scikit-learn`, `pandas`, `matplotlib`, `streamlit`, etc.

### Pasos para instalar

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/JeralinF/trabajo_administracion_datos.git
    ```

2. Cambiar al directorio del proyecto:

    ```bash
    cd cripto_prediccion
    ```

3. Crear un entorno virtual:

    ```bash
    python -m venv .venv
    ```

4. Activar el entorno virtual:
   
    - En Windows:

        ```bash
        .\.venv\Scripts\activate
        ```

    - En macOS/Linux:

        ```bash
        source .venv/bin/activate
        ```

5. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar la aplicación, simplemente usa Streamlit. Asegúrate de que tu entorno virtual esté activado.

1. Ejecuta el siguiente comando:

    ```bash
    streamlit run app.py
    ```

2. Abre el navegador en la dirección que te proporcione Streamlit y sigue las instrucciones para ingresar los datos de la criptomoneda y realizar una predicción.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Empuja tus cambios (`git push origin feature-nueva`).
5. Crea un pull request para que los cambios sean revisados.

## Licencia

Este proyecto está licenciado bajo la licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
