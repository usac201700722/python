import eDP as DivisorPropio         #Importe funcion que calcula los divisores propios

cont=2
bandera=0
print(''' ---------------------------------------------------------------------
BIENVENIDOS AL PROGRAMA QUE DETERMINA LOS PRIMEROS N NUMEROS PERFECTOS
Programado por: Sergio Augusto León Urrutia
Carnet:201700722
---------------------------------------------------------------------''')
try:                                    #Manejo de errores al ingresar un valor equivocado 
    numero= int(input("Ingrese un numero entero: "))
except ValueError:
    print("Ingreso un valor incorrecto, recuerde que debe ser un numero entero")
else:
    if numero>0 and numero<5:           #Verfica que el rango del numero sea correcto
        while bandera<numero:
            amigo1=DivisorPropio.divisores(cont)    #Calcula el DP de un numero
            
            if cont==amigo1:                        #Si el DP del numero es igual al numero es perfecto
                bandera=bandera+1
                print("El numero: "+str(amigo1) +" es el perfecto No. "+str(bandera)) #Imprime los No. perfectos 
            cont=cont+1
    elif numero>=5:                 #Mensaje de error cuando el numero es muy grande    
        print('''**Este programa puede calcular numeros perfectos mayores a 4, sin embargo,
        el procesamiento es MUY ELEVADO y puede tardar muchos minutos o hasta varios dias
        en calcularlo, por eso esta limitado a calores entre 1 y 4**''')
    elif numero<0:                 #Mensaje de error cuando el numero no es mayor a 0
        print("Este numero es incorrecto, debe ingresar valores MAYORES a 0")
