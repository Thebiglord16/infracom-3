from ftplib import FTP
import time
import socket

# Dirección ip del servidor
HOST = 'localhost'

# Se realiza conexion con el HOST, usando el puerto predeterminado (puerto 21)
ftp = FTP(HOST)

# Se realiza el login con los parametros por default (usuario: "anonymous"; password: anonymous@)
ftp.login()

# La funcion cwd permite cambiar el directorio sobre el cual esta llevando a cabo la conexion ftp, en este caso para
# redirigirlo hacia la ubiacacion donde se encuentra el archivo a descargar
ftp.cwd("/migmu/Desktop/New folder (2)/infracom-3-master/compartiblesftp")

# muestra los directorios y archivos en la ubicacion actual, en este caso los 2 archivos a descargar
ftp.retrlines('LIST')

# Se abre primero el archivo multimedia, en modo write and binary para que de esta manera pueda ser copiada como
# archivo binario
with open('multimedia.mp4', 'wb') as archivo:
    # La funcion retrbinary se encarga de recuperar un archivo en formato binario, usando el comando RETR,
    # este luego es escrito en la ubicacion actual con el comando write
    ftp.retrbinary('RETR multimedia.mp4', archivo.write)
