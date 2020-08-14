#Mi carnet es 201700722
Numero=722
archivo = open('/home/urrutia/Escritorio/201700722-Cortos980/corto1/collatz.txt', 'w')
for cont in range(2,Numero):
    dimension2=[]
    while cont!=1:
        modulo=cont%2                       #Determina el modulo para saber si es par
        if modulo==0:                       #Si es par cont = cont/2
            dimension2.append(cont)              #Escribe al final del archivo
            cont=cont//2
        else:                               #Si es impar cont = (3*cont)+1
            dimension2.append(cont)
            cont =(3*cont)+1                #Escribe al final del archivo
        if cont == 1:
            dimension2.append(1)
    archivo.write(str(dimension2)+'\n')
archivo.close()