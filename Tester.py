from server3 import ServerThread
from cliente3 import ClientThread
import threading

numeroClientes = 2
HOST = 'localhost'
hiloserver = ServerThread()
hiloserver.start()
listaClientes = []

while numeroClientes > 0:
    nuevoCliente = ClientThread()
    nuevoCliente.id = numeroClientes
    listaClientes.append(nuevoCliente)
    numeroClientes -= 1
for cliente in listaClientes:
    cliente.start()

