"""
============================================================
PROYECTO: Lectura serial del ESP32 y guardado en CSV
DESCRIPCION:
1. Abre el puerto serial donde esta conectado el ESP32.
2. Lee lineas en formato CSV.
3. Valida la estructura de cada linea.
4. Convierte los datos a tipos numericos.
5. Agrega timestamp del computador y guarda en un archivo CSV.
AUTOR: Material pedagogico para Programacion Aplicada
============================================================
"""

# ---------------------------------------------------------
# Importacion de modulos
# ---------------------------------------------------------
# csv permite escribir archivos separados por comas.
import csv
# os permite verificar si un archivo existe.
import os
# time se usa para pausas breves.
import time
# datetime permite crear una marca de tiempo legible.
from datetime import datetime
# serial proviene de pyserial y permite leer el puerto.
import serial

# ---------------------------------------------------------
# Configuracion editable por el estudiante
# ---------------------------------------------------------
# En Windows suele ser COM3, COM4, COM5...
# En Linux suele ser /dev/ttyUSB0 o /dev/ttyACM0.
PUERTO = "COM3"
# Debe coincidir con Serial.begin(115200) del ESP32.
BAUDIOS = 115200
# Nombre del archivo donde se guardaran las muestras.
ARCHIVO_CSV = "datos_potenciometro.csv"

# ---------------------------------------------------------
# Crear el CSV con cabecera si aun no existe
# ---------------------------------------------------------
def inicializar_csv(nombre_archivo):
    # Si el archivo no existe, se crea y se escribe la cabecera.
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([
                "timestamp_pc",
                "lectura_cruda",
                "voltaje",
                "porcentaje"
            ])

# ---------------------------------------------------------
# Funcion principal
# ---------------------------------------------------------
def main():
    # Variable de conexion. Se inicializa en None para poder
    # cerrarla con seguridad dentro del bloque finally.
    conexion = None
    
    # Se garantiza que el archivo CSV exista.
    inicializar_csv(ARCHIVO_CSV)
    print("Intentando abrir el puerto serial...")
    try:
        # Apertura del puerto serial.
        conexion = serial.Serial(PUERTO, BAUDIOS, timeout=1)
        # Pequena pausa para estabilizar la conexion.
        time.sleep(2)
        print(f"Conexion establecida con {PUERTO} a {BAUDIOS} baudios.")
        print("Presiona Ctrl + C para detener la captura.\n")
        # Bucle infinito de lectura.
        while True:
            # Lee una linea, la convierte de bytes a texto y quita
            # espacios o saltos de linea sobrantes.
            linea = conexion.readline().decode("utf-8", errors="ignore").strip()
            # Si no llego nada, se continua con la siguiente iteracion.
            if not linea:
                continue
            # Se ignora la linea de bienvenida enviada por setup().
            if "ESP32 listo" in linea:
                print(f"[INFO] {linea}")
                continue
            # Se imprime la linea para depuracion.
            print(f"[RECIBIDO] {linea}")
            # Se espera exactamente el formato:
            # lectura_cruda,voltaje,porcentaje
            partes = linea.split(",")
            # Si la linea no tiene exactamente 3 campos, se descarta.
            if len(partes) != 3:
                print("[ADVERTENCIA] Linea con formato inesperado. Se omite.")
                continue
            try:
                # Conversion de texto a tipos numericos.
                lectura_cruda = int(partes[0])
                voltaje = float(partes[1])
                porcentaje = float(partes[2])
            except ValueError as error:
                # Esta excepcion aparece cuando un campo no puede
                # convertirse a numero.
                print(f"[ADVERTENCIA] No se pudo convertir la linea: {error}")
                continue

            # Timestamp del computador al recibir la muestra.
            timestamp_pc = datetime.now().strftime(" %Y- %m- %d %H: %M: %S")
            
            try:
                # Se agrega la nueva fila al final del CSV.
                with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow([
                        timestamp_pc,
                        lectura_cruda,
                        voltaje,
                        porcentaje
                    ])
            except PermissionError as error:
                # Puede ocurrir si el CSV esta abierto en Excel
                # y el sistema no permite escribirlo.
                print(f"[ERROR] No se pudo escribir el CSV: {error}")
                time.sleep(1)
    
    except serial.SerialException as error:
        # Error al abrir el puerto o al usarlo durante la captura.
        print(f"[ERROR] Problema con el puerto serial: {error}")
    except KeyboardInterrupt:
        # Se activa cuando el usuario presiona Ctrl + C.
        print("\nCaptura finalizada por el usuario.")
    finally:
        # finally se ejecuta siempre, haya o no excepcion.
        # Aqui se intenta cerrar el puerto correctamente.
        if conexion is not None and conexion.is_open:
            conexion.close()
            print("Puerto serial cerrado correctamente.")


# ---------------------------------------------------------
# Punto de entrada del programa
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
