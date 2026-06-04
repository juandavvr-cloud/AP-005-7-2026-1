import threading
import time
import config
import data_store
import serial_reader
import analyzer
import plotter
import socket_server
import thingspeak_client  # <-- NOMBRE OFICIAL DE LA GUÍA
import web_app            # <-- NOMBRE OFICIAL DE LA GUÍA

def main():
    print("==================================================")
    print("   SISTEMA INTEGRAL DE MONITOREO ANALÓGICO - ESP32")
    print("==================================================")

    # 1. Inicializar la base de datos física local (CSV)
    data_store.initialize_csv()

    # 2. HILO 1: Lector Serial UART (ESP32 -> Python)
    serial_thread = threading.Thread(target=serial_reader.start_serial_reading, daemon=True)
    print("Arrancando Hilo 1: Lector Serial UART...")
    serial_thread.start()

    # 3. HILO 2: Servidor Sockets TCP (Puerto 9000)
    socket_thread = threading.Thread(target=socket_server.start_socket_server, daemon=True)
    print("Arrancando Hilo 2: Servidor Sockets TCP...")
    socket_thread.start()

    # 4. HILO 3: Analizador Estadístico y Generador de Gráficas (Pandas + Matplotlib)
    def loop_graficador():
        contador = 0
        while True:
            analyzer.update_statistics()
            if contador % 3 == 0:
                plotter.generate_plots()
            contador += 1
            time.sleep(1.0)

    plot_thread = threading.Thread(target=loop_graficador, daemon=True)
    print("Arrancando Hilo 3: Analizador Estadístico y Gráfico...")
    plot_thread.start()

    # 5. HILO 4: Sincronización con la nube (ThingSpeak API IoT)
    cloud_thread = threading.Thread(target=thingspeak_client.start_cloud_upload, daemon=True)
    print("Arrancando Hilo 4: Cliente IoT ThingSpeak...")
    cloud_thread.start()

    print("\n Lanzando Servidor Web Flask en http://127.0.0.1:5000")
    print("Presiona Ctrl + C en esta terminal para apagar el sistema de forma segura.\n")
    
    # 6. Ejecutar el Servidor Web Flask sobre el hilo principal de Python
    web_app.start_web_server()

if __name__ == "__main__":
    main()