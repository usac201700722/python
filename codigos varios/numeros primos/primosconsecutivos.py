def primo(N):
    if N < 1:
        return False
    elif N == 2:
        return True
    else:
        for i in range(2, N):
            if N % i == 0:
                return False
        return True  

lista=[] 
num = int(input("Escriba un numero entero: "))
archivo= open('sumatoria.txt','w')
for i in range(2,num):
    esprimo = primo(i)
    #print(esprimo)
    if esprimo==True:
        lista.append(i)
archivo.write(str(lista))

suma=0
bandera=True
for i in lista:
    suma = suma+i
archivo.write(str(suma))
archivo.close()
    
    

