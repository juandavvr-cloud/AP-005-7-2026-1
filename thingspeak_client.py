import time
import requests
import config

def start_cloud_upload():
    """Hilo encargado de subir el voltaje a ThingSpeak cada 15 segundos"""
    print(f" Iniciando cliente IoT. Clave configurada: {config.THINGSPEAK_API_KEY}")
    
    while True:
        try:
            # Lectura segura de la variable global
            with config.data_lock:
                voltaje_actual = config.latest_data["voltaje"]
            
            # Preparación de la petición GET para la API de ThingSpeak
            payload = {
                'api_key': config.THINGSPEAK_API_KEY,
                'field1': voltaje_actual
            }
            
            # Envío de datos
            response = requests.get(config.THINGSPEAK_URL, params=payload, timeout=5)
            
            if response.status_code == 200 and response.text != '0':
                print(f"[NUBE] Sincronización exitosa. Voltaje enviado: {voltaje_actual}V")
            else:
                print("[NUBE] Error: ThingSpeak no aceptó el dato (espera el intervalo de 15s).")

        except Exception as e:
            print(f"[NUBE] Error de conexión: {e}")
            
        time.sleep(config.THINGSPEAK_INTERVAL)