import os
import pandas as pd
import matplotlib
# Configuración para que Matplotlib guarde archivos en segundo plano sin abrir ventanas gráficas
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import config

def generate_plots():
    """Lee el archivo CSV histórico y genera de forma automática las 3 gráficas requeridas en PNG"""
    try:
        # 1. Validar la existencia física del archivo de datos
        if not os.path.exists(config.CSV_FILE_PATH):
            return
        
        try:
            df = pd.read_csv(config.CSV_FILE_PATH)
        except Exception:
            return

        # Si el CSV está vacío o tiene muy poquitas muestras, esperamos a que recolecte más
        if df.empty or len(df) < 5:
            return

        # Definimos la ruta de guardado dentro de tu estructura de proyecto
        output_dir = 'static/plots'
        os.makedirs(output_dir, exist_ok=True)

        # Tomamos las últimas 100 muestras para que las gráficas no se saturen visualmente
        df_recent = df.tail(100).copy()

        # ----------------------------------------------------
        # GRÁFICA 1: Señal de Voltaje en Función del Tiempo
        # ----------------------------------------------------
        plt.figure(figsize=(6, 4))
        plt.plot(df_recent['tiempo_ms'] / 1000.0, df_recent['voltaje'], color='blue', label='Voltaje Real')
        plt.title('Señal del Sensor en el Tiempo')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Voltaje (V)')
        plt.ylim(-0.1, 3.4)
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'sensor_tiempo.png'), dpi=100)
        plt.close()

        # ----------------------------------------------------
        # GRÁFICA 2: Histograma de las Mediciones de Voltaje
        # ----------------------------------------------------
        plt.figure(figsize=(6, 4))
        plt.hist(df['voltaje'], bins=15, color='purple', edgecolor='black', alpha=0.7)
        plt.title('Histograma de Mediciones')
        plt.xlabel('Voltaje (V)')
        plt.ylabel('Frecuencia de Muestras')
        plt.xlim(-0.1, 3.4)
        plt.grid(True, linestyle='--')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'histograma.png'), dpi=100)
        plt.close()

        # ----------------------------------------------------
        # GRÁFICA 3: Gráfica del Promedio Móvil
        # ----------------------------------------------------
        plt.figure(figsize=(6, 4))
        df_recent['promedio_movil'] = df_recent['voltaje'].rolling(window=10, min_periods=1).mean()
        
        plt.plot(df_recent['tiempo_ms'] / 1000.0, df_recent['voltaje'], color='lightgray', alpha=0.6, label='Voltaje Real')
        plt.plot(df_recent['tiempo_ms'] / 1000.0, df_recent['promedio_movil'], color='red', linewidth=2, label='Promedio Móvil')
        plt.title('Gráfica de Promedio Móvil')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Voltaje (V)')
        plt.ylim(-0.1, 3.4)
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'promedio_movil.png'), dpi=100)
        plt.close()

    except Exception as e:
        print(f"Error al generar gráficos: {e}")