import threading

# ==============================================================================
# CONFIGURACIÓN GENERAL DEL SISTEMA
# ==============================================================================
# Puerto y velocidad para la comunicación con la ESP32
SERIAL_PORT = 'COM5'  
SERIAL_BAUDRATE = 115200  # <--- Agregada con el nombre exacto que pide el lector

# Ruta para el almacenamiento de datos
CSV_FILE_PATH = 'data/lecturas.csv'

# Estructura de datos global para el intercambio entre hilos
latest_data = {
    "voltaje": 0.0,
    "promedio": 0.0,
    "estado": "NORMAL",
    "tiempo_ms": 0,
    "muestras_totales": 0
}

# Seguridad para acceso concurrente
data_lock = threading.Lock()

# ==============================================================================
# CONFIGURACIÓN DE RED Y NUBE (IoT)
# ==============================================================================
SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = 9000

# Parámetros de ThingSpeak
THINGSPEAK_API_KEY = 'A53AIALZZQVUU0D7'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'
THINGSPEAK_INTERVAL = 5