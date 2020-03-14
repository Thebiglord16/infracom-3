import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

print("Por favor ingrese la dirección ip del servidor")
# Dirección ip del servidor
HOST = input()
# Creacion de un autorizador, el cual manejara las autenticaciones y permitira es uso de usuarios anonimos
autorizaciones = DummyAuthorizer()
autorizaciones.add_anonymous("/users")
# El FTPHandler se encarga de implementar el protocolo FTP, en este caso especificando que el autorizador previamente
# creado sera el encargado de las autorizaciones del mismo
handler = FTPHandler
handler.authorizer = autorizaciones
# Se crea el servidor con el manejador indicado, en el puerto predeterminado y la ip escogida
server = FTPServer((HOST, 21), handler)
server.serve_forever()

