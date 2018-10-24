nombreA="default"
nombreB="default"
cantidad="default"
categoria_elegida="Default"
eleccion="D"
categorias_array=["a) Cultura general","b) Marvel","c) Musica","d) Historia", "e) Ciencia","f) Tecnologia"]

def inicio():
    global nombreA
    global nombreB
    global cantidad
    cantidad=int(input("¿Cuantos jugadores jugaran? 1 o 2: "))
    if cantidad==1:
        nombreA=input("Ingrese su nombre: ")
        nombreB=input("Ingrese el nombre del villano que quiere enfrentar: ")
        print ("Hola ",nombreA, "bienvenido a la alpha del juego, usted se enfrentara contra ",nombreB, " por la gloria.¿Estas listo para jugar?")
    else:
        nombreA=input("Ingrese el nombre del primer jugador: ")
        nombreB=input("Ingrese el nombre del segundo jugador: ")
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
    print (categoria_elegida)


    
    

