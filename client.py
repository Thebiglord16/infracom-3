import socket

print("Por favor ingrese la direccion ip del servidor")
# Dirección ip del servidor
HOST = input()
# Puerto en el que se esperan conecciones
PORT = 65432

# se abre un socket para la comunicación, el with crea un contexto en el que se asegura el cierre del socket aun cuando
# hay ocurre un error o se genera una excepción, el primer parametro representa la familia de direcciones con al que se
# creara el socket, en este caso IPV4, el segundo es el protoclo de comunicación en este caso TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Crea un socket con la tupla host, puerto
    s.connect((HOST, PORT))
    # manda un mensaje "hello world" a todos los servidores escuchando en el purto e ip de destino
    s.sendall(b'hello, world')
    # guarda en la variable data el mensaje recivido
    data = s.recv(1024)

# imprime el mensaje que recivió luego de reconstruirlo
print('Received', repr(data))
