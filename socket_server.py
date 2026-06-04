import socket
import json
import config

def start_socket_server():
    """Inicializa el servidor TCP en su propio hilo para responder consultas de red."""
    # Configuración del socket de red IPv4 y protocolo TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permite reutilizar el puerto de inmediato si reinicias el script
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Enlazar el socket a la IP y puerto definidos en config.py
        server_socket.bind((config.SOCKET_HOST, config.SOCKET_PORT))
        server_socket.listen(5)
        print(f" Servidor Socket TCP corriendo en http://{config.SOCKET_HOST}:{config.SOCKET_PORT}")
        
        while True:
            # Se queda esperando conexiones entrantes
            client_socket, client_address = server_socket.accept()
            
            try:
                # Leer la memoria global compartida protegiéndola con el Lock
                with config.data_lock:
                    payload = dict(config.latest_data)
                
                # Convertir los datos de ingeniería a formato JSON estructurado
                json_response = json.dumps(payload, indent=2)
                
                # Enviar respuesta y codificar el texto en bytes (UTF-8)
                client_socket.sendall(json_response.encode('utf-8'))
                
            except Exception as e:
                print(f"Error procesando petición en el socket cliente: {e}")
            finally:
                # Cerramos la conexión con este cliente para liberar el canal
                client_socket.close()
                
    except Exception as e:
        print(f"Error crítico en el Servidor Sockets TCP: {e}")
    finally:
        server_socket.close()