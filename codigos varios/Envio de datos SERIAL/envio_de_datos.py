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