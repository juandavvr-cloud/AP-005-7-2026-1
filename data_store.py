import os
import csv
import config

def initialize_csv():
    """Crea la carpeta data y el archivo CSV con sus encabezados si no existen."""
    # Asegura que la carpeta 'data/' exista en el directorio
    os.makedirs(os.path.dirname(config.CSV_FILE_PATH), exist_ok=True)
    
    # Si el archivo no existe, lo crea y le escribe los encabezados obligatorios
    if not os.path.exists(config.CSV_FILE_PATH):
        with open(config.CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['tiempo_ms', 'adc', 'voltaje'])
        print(f"Archivo CSV inicializado con éxito en: {config.CSV_FILE_PATH}")

def save_reading_to_csv(tiempo_ms, adc, voltaje):
    """Guarda una fila con la nueva medición real dentro del archivo CSV."""
    try:
        with open(config.CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([tiempo_ms, adc, voltaje])
    except Exception as e:
        print(f"Error crítico al guardar datos en el CSV: {e}")