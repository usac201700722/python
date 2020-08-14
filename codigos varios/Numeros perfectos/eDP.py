def divisores(N):               #Funcion que devuelve la suma de los divisores propios de un numero
    lista=list(range(1,N))      #Lista que va desde 1 hasta N
    suma=0
    for i in lista:
        modulo=N%i              #Determina el modulo del numero ingresado con cada numero desde
        if modulo ==0:          #0-N y si es 0, entonces es divisor propio.
            suma=suma+i
    return suma                 #Devuelve la suma de los divisores propios del numero.