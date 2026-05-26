from machine import Pin, ADC
import time

# Pin del potenciómetro (GPIO 34)
PIN_POT = 34

# Intervalo de muestreo en ms
INTERVALO_MS = 500

# Configuración ADC
adc = ADC(Pin(PIN_POT))
adc.atten(ADC.ATTN_11DB)      # Permite leer hasta ~3.3V
adc.width(ADC.WIDTH_12BIT)    # Resolución de 0 a 4095

ultimoEnvio = time.ticks_ms()

print("ESP32 listo. Enviando: lectura_cruda,voltaje,porcentaje")

while True:
    ahora = time.ticks_ms()
    
    if time.ticks_diff(ahora, ultimoEnvio) >= INTERVALO_MS:
        ultimoEnvio = ahora
        
        # Lectura cruda
        lecturaCruda = adc.read()  # 0 - 4095
        
        # Conversión a voltaje (aproximada)
        voltaje = (lecturaCruda / 4095) * 3.3
        
        # Conversión a porcentaje
        porcentaje = int((lecturaCruda / 4095) * 100)
        
        # Envío en formato CSV
        print("{},{:.3f},{}".format(lecturaCruda, voltaje, porcentaje))