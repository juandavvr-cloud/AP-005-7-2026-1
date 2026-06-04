import serial
import config
import data_store
import time

def start_serial_reading():
    """Se conecta al puerto serial y lee continuamente los datos del ESP32."""
    print(f"--- Intentando abrir conexión en el puerto {config.SERIAL_PORT} ---")
    try:
        # Configuramos la conexión serial con los parámetros de config.py
        ser = serial.Serial(config.SERIAL_PORT, config.SERIAL_BAUDRATE, timeout=1)
        time.sleep(2)  # Pausa de seguridad para que el canal serial se estabilice
        print(f"Conexión UART establecida con éxito en {config.SERIAL_PORT}!")

        while True:
            # Si hay datos esperando en el buffer del puerto serial
            if ser.in_waiting > 0:
                # Leemos la línea, la decodificamos a texto y limpiamos espacios vacíos
                line = ser.readline().decode('utf-8').strip()
                
                if line:
                    # Separamos los tres campos usando la coma como divisor
                    parts = line.split(',')
                    if len(parts) == 3:
                        try:
                            # Convertimos los textos a los tipos de datos correctos
                            t_ms = int(parts[0])
                            adc_val = int(parts[1])
                            volt_val = float(parts[2])

                            # 1. Guardar la medición inmediatamente en el archivo CSV
                            data_store.save_reading_to_csv(t_ms, adc_val, volt_val)

                            # 2. Actualizar la memoria compartida usando el bloqueo (Lock) obligatorio
                            with config.data_lock:
                                config.latest_data["tiempo_ms"] = t_ms
                                config.latest_data["adc"] = adc_val
                                config.latest_data["voltaje"] = volt_val
                            
                            # Imprimimos en consola para ver que esté funcionando en vivo
                            print(f"UART Recibido -> Tiempo: {t_ms}ms | ADC: {adc_val} | Voltaje: {volt_val}V")
                        
                        except ValueError:
                            print(f"Advertencia: Línea con formato de datos corrupto: {line}")
                            
            time.sleep(0.01)  # Pequeño respiro para el procesador
                            
    except serial.SerialException as e:
        print(f"\nError de comunicación Serial: No se pudo abrir el puerto {config.SERIAL_PORT}.")
        print("Asegúrate de que el monitor serial de PlatformIO esté cerrado y el cable bien conectado.")
    except Exception as e:
        print(f"Error inesperated en el lector serial: {e}")