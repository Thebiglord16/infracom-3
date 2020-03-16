from threading import Thread
import os
import socket

print("inserte la direccion ip del HOST")
host = input()
print("inserte el puerto al cual se conectara")
port = int(input())
id = -1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.send(b"Listo para recibir!")
    data = s.recv(1024)
    print("recibido por el cliente con id: " + str(id), repr(data))
    ext = (((repr(data).replace("b", "")).replace("'", "")).split("/"))[0]
    print(ext)
    s.send(b"reciviendo")
    size = s.recv(1024)
    data = s.recv(1024000)
    f = open('nuevo' + str(id) + ext, 'wb')
    while data:
        f.write(data)
        try:
            data = s.recv(1024000)
        except Exception:
            break
    f.close()
    f = open('nuevo' + str(id) + ext, 'rb')
    f.seek(0, os.SEEK_END)
    sizer = str(f.tell())
    f.close()
    while bytes(sizer, encoding='utf8') != size:
        s.send(b"error")
        data = s.recv(1024000)
        f = open('nuevo' + str(id) + ext, 'wb')
        while data:
            f.write(data)
            try:
                data = s.recv(1024000)
            except Exception:
                break
        f.close()
        f = open('nuevo' + str(id) + ext, 'rb')
        f.seek(0, os.SEEK_END)
        sizer = str(f.tell())
        f.close()
    s.send(b"succes")

    print("Done Sending")
