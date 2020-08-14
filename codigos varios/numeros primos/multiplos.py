numero=int(input("Ingrese un numero: "))
lista=list(range(numero))
print(lista)
res=[]
suma=0
for i in lista:
    modulo3=i%3
    modulo5=i%5

    if modulo3==0 or modulo5==0:
        res.append(i)
        suma =suma+ i
print(res)
print (suma)