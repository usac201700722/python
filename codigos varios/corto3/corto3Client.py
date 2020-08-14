import socket   #SALU libreria para implementar sockets
import binascii #SALU libreria para enviar hex
import os       #SALU libreria para trabajar con comandos de OS

SERVER_IP   = ''    #SALU  '' es igual a localhost
SERVER_PORT = 9800  #SALU  puerto 9800
BUFFER_SIZE = 64 * 1024 #SALU tamaño de buffer de 64kb

#SALU  Se crea socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SALU  Se conecta al puerto donde el servidor se encuentra a la escucha
server_address = (SERVER_IP, SERVER_PORT)
print('Conectando a {} en el puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    print('''INSTRUCCIONES:
    PARA GRABAR AUDIO PRESIONE:  1
    PARA RECIBIR EL ULTIMO AUDIO GRABADO PRESIONE: 2
    PARA FINALIZAR LA CONEXION PRESIONES: 0

    *Si presiona otra tecla la conexion finalizará.
    ''')

    message = int(input("ingrese una instruccion: ")) #SALU instruccion que ingresa el usuario

    print('\n\nEnviando el siguiente texto:  {!s}'.format(message)) #SALU imprime message
    if message == 1:
        sock.sendall(binascii.unhexlify("01")) #SALU enviamos el comando como Hex
        while True:
            respuesta = sock.recv(BUFFER_SIZE)
            if respuesta==binascii.unhexlify("CC"):
                print("se recibio respuesta")
                duracion= input("Ingrese la duracion del audio en segundos: ")
                duracion = duracion.encode
                sock.sendall(duracion)
    
    if message == 2:
        sock.sendall(binascii.unhexlify("02"))
        buff = sock.recv(BUFFER_SIZE)
        archivo = open('202012345_client.wav', 'wb') #SALU Aca se guarda el archivo entrante
        while buff:
            buff = sock.recv(BUFFER_SIZE) #SALU Los bloques se van agregando al archivo
            archivo.write(buff)
        os.system('aplay 202012345_client.wav') #SALU reproduce el audio que entro
        archivo.close() #Se cierra el archivo
        print("Reproduccion de audio finalizada")

    if message == 0:
        sock.sendall(binascii.unhexlify("00"))  #SALU envia el comando para finalizar conexion

finally:
    print('\n\nConexion finalizada con el servidor')    #SALU finaliza la coneccion
    sock.close()