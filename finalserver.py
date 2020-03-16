import socket
import os

print("inserte la cantidad de clientes a recibir")
cantidad = int(input())
actual = 0
print("inserte la direccion ip del HOST")
HOST = input()
print("inserte el puerto al cual se conectara")
PORT = int(input())
print("inserte el nombre del archivo a enviar sin incluir la extension")
file = input()
print("inserte la extension del archivo a enviar ej: .mp4")
ext = input()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with s:
    # Crea un socket con la tupla host, puerto
    s.bind((HOST, PORT))
    # Hace que el servidor escuche peticiones en el puerto PORT
    s.listen()
    connections = []
    # Mientras sigan llegando clientes y mensajes de los mismos
    while True:
        # asigna un objeto socket a conn y la dirección del cliente aceptado en addt
        conn, addr = s.accept()
        connections.append(conn)
        # el with crea un contexto en el que se asegura el cierre del socket aun cuando ocurre un error o se
        # genera una excepción
        print("connected by", addr)
        # Almacena el mensaje en data
        data = conn.recv(1024)
        # print(threading.enumerate())
        print("recibido por el servidor: ", repr(data))
        # si no recibe un mensaje, cancele la conexión
        if not data:
            break
        # responde al mensaje, haciendo referencia a la espera de los demas clientes
        texto = ext+"/"+"recibido, esperando a los demas clientes " + str(actual + 1) + "/" + str(cantidad)
        conn.send(bytes(texto, encoding='utf8'))
        actual += 1
        if cantidad == actual:
            print(conn)
            enviados = 1
            envio = 1
            for i in connections:
                print("envio a cliente: " + str(enviados))
                f = open(file+ext, 'rb')
                f.seek(0, os.SEEK_END)
                texto = str(f.tell())
                f.close()
                i.send(bytes(texto, encoding='utf8'))
                f = open(file+ext, 'rb')
                enviable = f.read(1024000)
                envio = 0
                while enviable:
                    i.send(enviable)
                    enviable = f.read(1024000)
                    envio += 1
                f.close()
                succes = i.recv(1024)
                print(succes)
                while succes == b'error':
                    print("reintentando")
                    f = open(file+ext, 'rb')
                    enviable = f.read(1024000)
                    envio = 0
                    while enviable:
                        i.send(enviable)
                        enviable = f.read(1024000)
                        envio += 1
                    f.close()
                    succes = i.recv(1024)
                enviados += 1
                i.close()
