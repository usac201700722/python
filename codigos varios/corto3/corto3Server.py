import socket   #SALU libreria para implementar sockets
import binascii #SALU libreria para enviar hex
import os       #SALU libreria para trabajar con comandos de OS

#SALU  Crea un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ADDR = '' #SALU  La IP donde desea levantarse el server '' es localhost
IP_ADDR_ALL = '' #SALU esucha en todas las interfaces de red
IP_PORT = 9800 #SALU Puerto al que deben conectarse los clientes

BUFFER_SIZE = 64 * 1024 #SALU buffer de 64 KB

#SALU  Bind the socket to the port
serverAddress = (IP_ADDR_ALL, IP_PORT) #SALU Escucha en todas las interfaces
print('Iniciando servidor en {}, puerto {}'.format(*serverAddress))
sock.bind(serverAddress) #SALU Levanta servidor con parametros especificados

#SALU  Habilita la escucha del servidor en las interfaces configuradas
sock.listen(10) #SALU El argumento indica la cantidad de conexiones en cola

while True:
    #SALU  Esperando conexion
    print('Esperando conexion remota')
    connection, clientAddress = sock.accept() #SALU acepta la conexion
    
    try:
        print('Conexion establecida desde', clientAddress)

        #SALU  Se envia informacion en bloques de BUFFER_SIZE bytes
        #SALU  y se espera respuesta de vuelta
        while True:
            data = connection.recv(BUFFER_SIZE) 
            #SALU almacena los datos recibidos en bloques de tamaño 64kb
            print('Recibido: {!r}'.format(data))
            if data==binascii.unhexlify("01"):  #SALU GRABA EL AUDIO
                connection.sendall(binascii.unhexlify("CC"))
                while True:
                    duracion = connection.recv(BUFFER_SIZE)
                    #duracion = duracion.encode()
                    #print(str(duracion))
                    os.system('arecord -d 10 -f U8 -r 8000 201700722_server.wav')  #SALU Graba con arecord

            if data==binascii.unhexlify("02"):
                with open('201700722_server.wav', 'rb') as f: #SALU Se abre el archivo a enviar en BINARIO
                    connection.sendfile(f, 0)   #SALU envia el archivo de audio
                    f.close()
                    print("\n\nArchivo enviado a: ", clientAddress)
            
            if data==binascii.unhexlify("00"): #SALU cierra la conexion 
                print('Transmision finalizada desde el cliente ', clientAddress)
                break

            else:
                print('Comando no definido ', clientAddress)
                break
    
    except KeyboardInterrupt:
        sock.close()

    finally:
        # Se baja el servidor para dejar libre el puerto para otras aplicaciones o instancias de la aplicacion
        connection.close()