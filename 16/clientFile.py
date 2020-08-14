import socket
import os

SERVER_ADDR = ''
SERVER_PORT = 9800

BUFFER_SIZE = 64 * 1024

sock = socket.socket()
sock.connect((SERVER_ADDR, SERVER_PORT))


try:
    buff = sock.recv(BUFFER_SIZE)
    archivo = open('recibido.wav', 'wb') #Aca se guarda el archivo entrante
    while buff:
        archivo.write(buff)
        buff = sock.recv(BUFFER_SIZE) #Los bloques se van agregando al archivo
    archivo.close() #Se cierra el archivo
    print("Recepcion de archivo finalizada")

finally:
    print('Conexion al servidor finalizada')
    sock.close() #Se cierra el socket
    os.system('aplay recibido.wav')
