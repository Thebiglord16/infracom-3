from threading import Thread
import time
import socket
import threading


class ClientThread(Thread):
    host = '127.0.0.1'  # Get local machine name
    port = 65432  # Reserve a port for your service.
    listo = False
    continuar = threading.Event()
    id = -1

    def run(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.send(b"Listo para recibir!")
            data = s.recv(1024)
            print("recibido por el cliente con id: "+str(self.id), repr(data))
            self.listo = True
            s.send(b"reciviendo")
            data = s.recv(1024000)
            f = open('nuevo' + str(self.id) + '.mp4', 'wb')
            while data:
                f.write(data)
                try:
                    data = s.recv(1024000)
                except Exception:
                    break
            f.close()
            print("Done Sending")
