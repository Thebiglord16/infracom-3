import socket

print("Por favor ingrese la dirección ip del servidor")
# Dirección ip del servidor
HOST = input()
# Puerto en el que se esperan conecciones
PORT = 65432

# se abre un socket para la comunicación, el with crea un contexto en el que se asegura el cierre del socket aun cuando
# ocurre un error o se genera una excepción, el primer parametro representa la familia de direcciones con al que se
# creara el socket, en este caso IPV4, el segundo es el protoclo de comunicación en este caso TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Crea un socket con la tupla host, puerto
    s.bind((HOST, PORT))
    # Hace que el servidor escuche peticiones en el puerto PORT
    s.listen()
    # asigna un objeto socket a conn y la dirección del cliente aceptado en addt
    conn, addr = s.accept()
    # el with crea un contexto en el que se asegura el cierre del socket aun cuando ocurre un error o se genera una
    # excepción
    with conn:
        print("connected by", addr)
        # Mientras la conexion reciva mensajes
        while True:
            # Almacena el mensaje en data
            data = conn.recv(1024)
            print("received", repr(data))
            # si no recibe un mensaje, cancele la conexión
            if not data:
                break
            # responde al mensaje, en este caso hace eco del mensaje recivido
            conn.sendall(data)
