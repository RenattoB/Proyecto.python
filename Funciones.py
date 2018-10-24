nombreA="default"
nombreB="default"
cantidad="default"

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
    