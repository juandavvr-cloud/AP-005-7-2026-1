import pandas as pd
import numpy as np
import config

def update_statistics():
    """ Lee el archivo CSV, calcula las estadísticas con Pandas/NumPy y actualiza config.latest_data """
    try:
        # 1. Verificar si el archivo CSV existe y tiene datos
        try:
            df = pd.read_csv(config.CSV_FILE_PATH)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            return

        # Si el archivo está vacío o solo tiene los encabezados, salimos
        if df.empty or len(df) < 1:
            return

        # 2. Extraer las últimas muestras individuales directas
        last_row = df.iloc[-1]
        t_ms = int(last_row['tiempo_ms'])
        adc_val = int(last_row['adc'])
        volt_val = float(last_row['voltaje'])

        # 3. Cálculos estadísticos usando las herramientas vectoriales de Pandas y NumPy
        total_muestras = int(df.shape[0])
        promedio_voltaje = float(df['voltaje'].mean())
        min_voltaje = float(df['voltaje'].min())
        max_voltaje = float(df['voltaje'].max())
        
        # Desviación estándar calculada con NumPy (manejando el caso de una sola muestra)
        if total_muestras > 1:
            std_voltaje = float(df['voltaje'].std())
        else:
            std_voltaje = 0.0

        # 4. Cálculo del Promedio Móvil (Ventana de las últimas 10 muestras)
        # Usamos min_periods=1 para que calcule el promedio incluso si van menos de 10 datos
        df['rolling_mean'] = df['voltaje'].rolling(window=10, min_periods=1).mean()
        promedio_movil_actual = float(df['rolling_mean'].iloc[-1])

        # 5. Clasificación por umbral según el voltaje actual
        if volt_val < 1.0:
            estado_actual = "BAJO"
        elif volt_val <= 2.5:
            estado_actual = "NORMAL"
        else:
            estado_actual = "ALTO"

        # 6. Guardar todo el análisis en la estructura global compartida de forma segura (Lock)
        with config.data_lock:
            config.latest_data["tiempo_ms"] = t_ms
            config.latest_data["adc"] = adc_val
            config.latest_data["voltaje"] = volt_val
            config.latest_data["muestras_totales"] = total_muestras
            config.latest_data["promedio"] = promedio_voltaje
            config.latest_data["minimo"] = min_voltaje
            config.latest_data["maximo"] = max_voltaje
            config.latest_data["desviacion_estandar"] = std_voltaje
            config.latest_data["promedio_movil"] = promedio_movil_actual
            config.latest_data["estado"] = estado_actual

    except Exception as e:
        print(f"Error procesando estadísticas en analyzer.py: {e}")