import eDP as DivisorPropio

cont=2
bandera=0
temp1=0
temp2=0

print(''' ---------------------------------------------------------------------
BIENVENIDOS AL PROGRAMA QUE DETERMINA LOS PRIMEROS N NUMEROS AMIGOS
Programado por: Sergio Augusto León Urrutia
Carnet:201700722
---------------------------------------------------------------------''')
try:                        #Manejo de errores para la entrade de datos
    numero= int(input("Ingrese un numero entero: "))
except ValueError:          #Error cuando el usuario no ingresa un numero entero
    print("Este es un valor incorrecto, recuerde que debe ser un numero entero")
else:       

    while bandera<numero:
        amigo1=DivisorPropio.divisores(cont)        #Calcula el DP de un numero,
        amigo2=DivisorPropio.divisores(amigo1)      #Calcula el DP del numero encontrado anterior mente
        
        if amigo1==amigo2:                          #Si los amigos son iguales son numeros perfectos
            cont=cont+1                             #Por eso nos saltamos este numero

        if (temp2==amigo1 and temp1==amigo2):       #Evita que se repitan las parejas de numeros
            cont=cont+1                             #Sino mostraria: "la pareja 1 es: 220 y 284
                                                    #y la pareja 2: 284 y 220 "(MISMA PAREJA INVERITDA)
        
        if cont==amigo2:                            #Aqui si verifica que sean amigos
            bandera=bandera+1
            print("Los numeros "+str(amigo1)+" y "+str(amigo2)+" son la pareja de amigos No. "+str(bandera))
            temp1=amigo1
            temp2=amigo2  
        cont=cont+1