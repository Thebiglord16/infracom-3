import socket
import threading
import os

class ServerThread(threading.Thread):
    cantidad = 25
    continuar = threading.Event()
    actual = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        HOST = '127.0.0.1'
        PORT = 65432
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
                texto = "recibido, esperando a los demas clientes " + str(self.actual+1) + "/" + str(self.cantidad)
                conn.send(bytes(texto, encoding='utf8'))
                self.actual += 1
                if self.cantidad == self.actual:
                    print(conn)
                    enviados = 1
                    envio = 1
                    for i in connections:
                        print("envio a cliente: " + str(enviados))
                        f = open('nvm.mp4', 'rb')
                        f.seek(0, os.SEEK_END)
                        texto = str(f.tell())
                        f.close()
                        i.send(bytes(texto, encoding='utf8'))
                        f = open('nvm.mp4', 'rb')
                        enviable = f.read(1024000)
                        envio = 0
                        while enviable:
                            print("envio " + str(envio))
                            i.send(enviable)
                            enviable = f.read(1024000)
                            envio += 1
                        f.close()
                        succes = i.recv(1024)
                        while succes == b'error':
                            print("reintentando")
                            f = open('nvm.mp4', 'rb')
                            enviable = f.read(1024000)
                            envio = 0
                            while enviable:
                                print("envio " + str(envio))
                                i.send(enviable)
                                enviable = f.read(1024000)
                                envio += 1
                            f.close()
                            succes = i.recv(1024)
                        enviados += 1
                        i.close()
