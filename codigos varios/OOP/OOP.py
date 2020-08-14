#************* CLASE PARA REALIZAR OPERACIONES CON MATRICES *****************************
class matriz(object):
    
    #Constructor de la clase
    #Todos los metodos (funciones) dentro de un 
    #objeto, llevan como parametro inicial "self"
    def __init__(self, data=[]):
        self.data = list(data)

    #La "longitud" del objeto, es en realidad representado
    #por la cantidad de datos de su lista principal
    def __len__(self):
        return len(self.data)

#****** MÉTODO QUE DEVUELVE LAS FILAS DE LA MATRIZ *************************************
    #Devuelve el valor de las filas de la matriz
    def filasMatriz(self):
        f = len(self)
        return f
#****** MÉTODO QUE DEVUELVE LAS COLUMNAS DE LA MATRIZ **********************************
    #Devuelve el valor de las columnas de la matriz
    def columnasMatriz(self):
        c = len(list(self.data[0]))
        return c
#****** MÉTODO QUE DEVUELVE LA MATRIZ DE FORMA AMIGABLE AL USUARIO PARA __STR__ ********
    #Funcion que devuelve la matriz en orden, para que el usuario pueda ver de forma adecuada
    #la estructura de la instancia matriz que creo
    def mostrarMatriz(self): 
        for i in range(0,self.filasMatriz()):
            for j in range(0,self.columnasMatriz()):
                print(self.data[i][j],end=' ')
            print()

#******FUNCION QUE DETERMINA SI LAS DIMENSIONES DE UNA MATRIZ SON CORRECTAS PARA SUM/RES****
    #Si las filas y columnas de ambas matrices son iguales entonces devuelve True
    def equalLenghts(self, nextObject):
        #Compara si las filas y las columnas del primer objeto son iguales a las del siguiente
        dimension=False
        if len(self.data)== len(nextObject) and len(self.data[0])==len(nextObject.data[0]):
            dimension= True
        return dimension 

#******************* SUMA ********************************************
    #Sobrecarga de suma, aplicado para una matriz
    def __add__(self, sumando):
        if self.equalLenghts(sumando):
            #Lleno matriz con ceros
            x = []
            for i in range(self.filasMatriz()):
                x.append([])
                for j in range(self.columnasMatriz()):
                    x[i].append(self.data[i][j] + sumando.data[i][j])   #Asigna al vector la suma de ambos
            return matriz(x)    #devuelve el vector de tipo matriz para poder usarlo en cadena a+b+c+...         
        else:
            raise ErrorDimensional(len(self.data), len(self.data[0]), len(sumando.data), len(sumando.data[0]))
#****************** RESTA **********************************************
    #Sobrecarga de resta, aplicado para una matriz
    def __sub__(self, sustraendo):
        if self.equalLenghts(sustraendo):
            #Lleno matriz con ceros
            x = []
            for i in range(self.filasMatriz()):
                x.append([])
                for j in range(self.columnasMatriz()):
                    x[i].append(self.data[i][j] - sustraendo.data[i][j])    #Asigna la resta de las matrices
            return matriz(x)        
        else:
            #Levantamos una excepcion creada a la medida
            raise ErrorDimensional(len(self.data), len(self.data[0]), len(sustraendo.data), len(sustraendo.data[0]))
#***************** MULTIPLICACION ***************************************
    #Debe hacerse en el siguiente orden: matriz*escalar
    #de lo contrario, el objeto int y float deberian ser modificados
    #Tambien sirve para matriz*matriz
    def __mul__(self, escalar):
        if type(escalar) == int or type(escalar) == float:  #Si el siguiente numero es un escalar opero Matriz*Escalar
            x = []
            for i in range(self.filasMatriz()):
                x.append([])
                for j in range(self.columnasMatriz()):
                    x[i].append(self.data[i][j]*escalar)
            return matriz(x)
        elif type(escalar) == matriz:                       #Si el siguiente parametro es un vector opero matriz*matriz
            if len(self.data[0])==len(escalar.data):
                #Lleno la matriz con ceros
                x=[]
                for i in range(len(self.data)):
                    x.append([])
                    for j in range(len(escalar.data[0])):
                        x[i].append(0)
                #Algoritmo para la multiplicacion
                for i in range(len(self.data)):             
                    for j in range(len(escalar.data[0])):
                        for k in range(len(self.data[0])):
                            x[i][j]+= self.data[i][k]*escalar.data[k][j]
                return matriz(x)
            else:
                raise ErrorDim(len(self.data[0]),len(escalar.data))            
        else:
            #La excepcion ya existe, solo se va a reutilizar
            raise TypeError("Solo pueden realizarse producto con un escalar o por una matriz")

#******************* Determinante ******************************************
    #Esta funcion se deberia hacer con recursividad para que no importe el tamaño de la
    #matriz cuadrada, sin embargo intente hacerla y no me funciono, asi que lo hice colocando
    #uno por uno los cofactores que darian como resultado el determinte, sin embargo no es nada optimo
    def determinante(self):
        if len(self)==len(self.data[0]):    #Es matriz cuadrada
            det=0
            if len(self)==1:            #Matriz 1X1
                det=self.data[0][0]
            elif len(self)==2:          #Matriz 2X2
                det=self.data[0][0]*self.data[1][1]-self.data[0][1]*self.data[1][0]
            elif len(self)==3:          #Matriz 3X3
                det=(self.data[0][0]*self.data[1][1]*self.data[2][2]+self.data[0][1]*self.data[1][2]*self.data[2][0]+\
                    self.data[0][2]*self.data[1][0]*self.data[2][1])-(self.data[2][0]*self.data[1][1]*self.data[0][2]+\
                        self.data[2][1]*self.data[1][2]*self.data[0][0]+self.data[2][2]*self.data[1][0]*self.data[0][1])
            else:
                raise ErrorDimMatrix(len(self.data))    #Si es mayor a 3X3 salta una excepcion
            return det
        else:
            #print("no se puede")
            raise ErrorSquareMatrix(len(self.data),len(self.data[0]))   #Si no es cuadrada salta una excepcion
#******************** INVERSA *************************************************
    #Al igual que el determinante no pude hacer un algoritmo, intente hacer el inv=adj(a**transpuesta)/Det
    #pero no pude sacar el determinante y la adjunta tambien necesitaba el metodo de cofactores, 
    #asi que tampoco la pude hacer.
    def inversa(self):
        if len(self.data)==len(self.data[0]):
            raise ErrorInvMatrix(len(self.data))
        else:
            raise ErrorSquareMatrix(len(self.data),len(self.data[0]))

#******************* SOBRECARCA __STR__ ***************************************
    #Sobrecarga de string: devuelve la lista de datos del vector
    def __str__(self):
        return str(self.mostrarMatriz())
#******************* SOBRECARGA __REPR__ **************************************
    #Representacion cuando se invoca el objeto sin casting a STRING.
    def __repr__(self):
        return self.__str__()

 #*********** CLASE TIPO EXCEPCION PARA INDICAR QUE DOS MATRICES NO SON DEL MISMO TAMAÑO *********   
#Excepcion hecha a la medida, para reportar un error que no es estandar
#Se levanta esta excepcion cuando la longitud de dos matrices a sumar/restar
#no son iguales. Se reciben como parametros las longitudes de ambas matrices
class ErrorDimensional(Exception):
    def __init__(self, lf1, lc1, lf2, lc2):
        self.lf1 = lf1
        self.lc1 = lc1
        self.lf2 = lf2
        self.lc2 = lc2
    
    def respuesta(self):
        if self.lf1 !=self.lf2 and self.lc1 != self.lc2:
            respuesta= "Las longitudes de las filas y columnas no coinciden"
        elif self.lf1 != self.lf2:
            respuesta= "Las longitudes de las filas no coinciden"+str(self.lf1) + "~=" + str(self.lf2)
        elif self.lc1 != self.lc2:
            respuesta= "Las longitudes de las columnas no coinciden"+str(self.lc1) + "~=" + str(self.lc2)
        return str(respuesta)
    def __str__(self):
        return self.respuesta()

#************ CLASE TIPO EXCEPCION PARA INDICAR QUE DOS MATRICES NO SE PUEDEN MULTIPLICAR ***************
#Excepcion que dice cuando dos matrices no se pueden multiplicar porque las columnas de la
#matriz1 no son iguales a las filas de la matriz2
class ErrorDim(Exception):
    def __init__(self,lc1, lf2):
        self.lc1 = lc1
        self.lf2 = lf2

    def __str__(self):
        return str("Las columnas de la primer matriz no corresponden con las filas de la segunda "+str(self.lc1)+" ~= "+str(self.lf2))


    def __repr__(self):
        return self.__str__()

#************** CLASE TIPO EXCEPCION PARA INDICAR QUE UNA MATRIZ ES MUY GRANDE PARA SACAR EL DETERMINANTE
# Esta excepcion es para decir que la matriz es muy grande para sacar un determinante
class ErrorDimMatrix(Exception):
    def __init__(self,lf1):
        self.lf1 = lf1 

    def __str__(self):
        return str("El tamaño de la matriz es muy grande, "+str(self.lf1)+" no es menor a 4 ")

    def __repr__(self):
        return self.__str__()

#************ CLASE TIPO EXCEPCION PARA INDICAR QUE UNA MATRIZ NO ES CUADRADA *******************
#Excepcion que salta cuando se le quiere sacar el determinante o la inversa a una matriz
#que no es cuadrada
class ErrorSquareMatrix(Exception):
    def __init__(self,lf1, lc1):
        self.lf1 = lf1
        self.lc1 = lc1

    def __str__(self):
        return str("Debe ser una matriz cuadrada "+str(self.lf1)+" ~= "+str(self.lc1))

    def __repr__(self):
        return self.__str__()

#************ CLASE TIPO EXCEPCION PARA INDICAR QUE UNA MATRIZ NO ES CUADRADA *******************
#Excepcion que puse para mostrar que no pude hacer la inversa de una matriz
class ErrorInvMatrix(Exception):
    def __init__(self,lf1):
        self.lf1=lf1

    def __str__(self):
        return str("Lo siento, no pude hacer la inversa de la matriz :( ")

    def __repr__(self):
        return self.__str__()

#****************** CLASE TIPO EXCEPCION PARA VER SI UN VECTOR ESTA VACIO ***************
#Excepción que se levanta cuando se trata de generar el inverso del vector,
#pero el vector está vacío
class VectorVacio(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return str("No hay elementos en la lista de datos")

    def __repr__(self):
        return self.__str__()