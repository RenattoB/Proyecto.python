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
    else:
        nombreA=input("Ingrese el nombre del primer jugador: ")
        nombreB=input("Ingrese el nombre del segundo jugador: ")

    print ("Hola jugad")