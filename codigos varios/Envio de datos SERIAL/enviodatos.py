import cv2
import time
import serial
import numpy as np

port = '/dev/ttyUSB0'
baudrate=9600
tiempo_espera=0.5

def enviarDatos(dato):
    Ascii_dato = chr(dato)
    print(dato)
    binario=bytes(Ascii_dato,'latin_1')

    UART = serial.Serial(port,baudrate, bytesize=8,parity='N', stopbits=1) 
    UART.write(binario)
    time.sleep(tiempo_espera)
    UART.close()
    

def Mapeo_de_colores(valor,Min_anterior,Max_anterior, Min, Max):
    Rango_anterior=(Max_anterior-Min_anterior)
    Rango =(Max-Min)
    Resultado = (((valor-Min_anterior)*Rango)/Rango_anterior)+Min
    return int(round(Resultado))

def conversion(matriz_datos_imagen):
    pixeles=[]
    for i in matriz_datos_imagen:
        for j in i:
            binary_repr_v= np.vectorize(np.binary_repr)
            bin_B = binary_repr_v(j[0],2)#3=11
            bin_G = binary_repr_v(j[1],3)#7=111
            bin_R = binary_repr_v(j[2],3)#7=111
            data = str((str(bin_B)+str(bin_G)+ str(bin_R)))
            #11 111 111
            decimal =int(data,base=2)
            pixeles.append(decimal)
            enviarDatos(decimal)

    print("Tamaño de la matriz a enviar "+ str(len(pixeles)))
    return pixeles


def procesamiento(nombre='imagen.jpg',filas=64,columnas=64):
    imagen = cv2.imread(nombre)
    imagen = cv2.resize(imagen,(filas,columnas))

    cv2.imshow('imgagen redimensionada: ',imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    B, G, R = cv2.split(imagen)

    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j]=Mapeo_de_colores(j,0,255,3,0)
    
    for i in range(len(G)):
        for j in range(len(G[0])):
            G[i][j]=Mapeo_de_colores(j,0,255,7,0)

    for i in range(len(R)):
        for j in range(len(R[0])):
            R[i][j]=Mapeo_de_colores(j,0,255,7,0)

    imagen= cv2.merge((B,G,R))
    print(conversion(imagen))
    cv2.imshow('imagen',imagen)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

procesamiento()