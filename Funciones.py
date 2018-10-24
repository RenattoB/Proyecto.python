#Varibles
nombreA="default"
nombreB="default"
cantidad="default"
categoria_elegida="Default"
eleccion="D"
categorias_array=["a) Cultura general","b) Marvel","c) Musica","d) Historia", "e) Ciencia","f) Tecnologia"]
opcionesHistoria=[["a. 1976","b. 1876" , "c. 1567"],[],[],[]]
Respuesta="Default"
ContadorA=0
ContadorB=0
#Funciones
def inicio():
    global nombreA
    global nombreB
    global cantidad
    cantidad=int(input("¿Cuantos jugadores jugaran? 1 o 2: "))
    if cantidad==1:
        nombreA=input("Ingrese su nombre: ")
        nombreB=input("Ingrese el nombre del villano que quiere enfrentar: " )
        print("********************************************************************")
        print ("Hola ",nombreA, "bienvenido a la alpha del juego, usted se enfrentara contra ",nombreB, " por la gloria.¿Estas listo para jugar?")
    else:
        nombreA=input("Ingrese el nombre del primer jugador: ")
        nombreB=input("Ingrese el nombre del segundo jugador: ")
        print("********************************************************************")
        print ("Hola  ",nombreA," y ",nombreB, " bienvenidos a la alpha del juego, ustedes se enfrentaran por la gloria.¿Estais listo para jugar?")
    
def categorias():
    global categoria_elegida
        
    print("Las categorias disponibles son: ")
    for i in categorias_array:
        print (" ",i," ")
    eleccion=input("Seleccione la letra de su categoria: ")
    if eleccion == "a" or eleccion == "A":
        categoria_elegida= "Cultura general"
    elif eleccion == "b" or eleccion == "B":
        categoria_elegida= "Marvel"
    elif eleccion == "c" or eleccion == "C":
        categoria_elegida= "Musica"
    elif eleccion == "d" or eleccion == "D":
        categoria_elegida= "Historia"
    elif eleccion == "e" or eleccion == "E" :
        categoria_elegida= "Ciencia"
    else:
        categoria_elegida= "Tecnologia"
    
    return categoria_elegida

def preguntasHistoria():
    global ContadorA
    print("¿Cuando nacio napoleon?")
    for i in opcionesHistoria[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="B" or "b":
        print("Respuesta correcta tienes un punto mas")
        ContadorA=ContadorA+1
        return ContadorA
    

def preguntasCulturaGeneral():
    print("Hola Cultura general")

def preguntasMarvel():
    print ("Hola Marvel")

def preguntasMusica():
    print("Hola Musica")

def preguntasCiencia():
    print("Hola Ciencia")

def preguntasTecnologia():
    print("Hola Tecnologia")



    
    

