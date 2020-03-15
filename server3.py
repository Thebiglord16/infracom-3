import socket
import threading


class ServerThread(threading.Thread):
    cantidad = 2
    continuar = threading.Event()
    actual = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        HOST = 'localhost'
        PORT = 65432
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with s:
            # Crea un socket con la tupla host, puerto
            s.bind((HOST, PORT))
            # Hace que el servidor escuche peticiones en el puerto PORT
            s.listen()

            # Mientras sigan llegando clientes y mensajes de los mismos
            while True:
                # asigna un objeto socket a conn y la dirección del cliente aceptado en addt
                conn, addr = s.accept()
                # el with crea un contexto en el que se asegura el cierre del socket aun cuando ocurre un error o se
                # genera una excepción
                with conn:
                    print("connected by", addr)
                    # Almacena el mensaje en data
                    data = conn.recv(1024)
                    # print(threading.enumerate())
                    print("recibido por el servidor: ", repr(data))
                    # si no recibe un mensaje, cancele la conexión
                    if not data:
                        break
                    # responde al mensaje, haciendo referencia a la espera de los demas clientes
                    texto = "recibido, esperando a los demas clientes " + str(self.actual) + "/" + str(self.cantidad)
                    conn.send(bytes(texto, encoding='utf8'))
                    self.actual += 1
                    if self.cantidad > self.actual:
                        enviados = 0
                        while enviados < self.cantidad:
                            self.continuar.wait()
                            f = open('multimedia.mp4', 'rb')
                            enviable = f.read(1024)
                            while enviable:
                                s.send(enviable)
                                enviable = f.read(1024)
                            f.close()
                            self.continuar.wait()
