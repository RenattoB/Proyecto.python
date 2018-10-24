#Varibles
nombreA="default"
nombreB="default"
cantidad="default"

categoria_elegida="Default"
eleccion="Default"

categorias_array=["a) Cultura general","b) Marvel","c) Musica","d) Historia", "e) Ciencia","f) Tecnologia"]

opcionesHistoria=[["a. 1976","b. 1876" , "c. 1567"],[],[],[]]

opcionesCultura=[["a. Mario Vargas Llosa","B. Homero","C. Pablo Neruda"],["a. Odometro","b. Interferometro","c. Termometro"]
,["a. 1914","b. 1915","c. 1913"],["a. Oro","b. Diamante","c. Rodio"],["a. ReinoUnido","b. España","c. Francia"],["a. Biblia","b. Coran","c. Dhammapada"]]

Respuesta="Default"

ContadorA=0
ContadorB=0

#Funciones
def inicio():
    
    global nombreA
    global nombreB
    global villano
    global cantidad
    
# Usuario selecciona el modo de juego que desea:

    cantidad=int(input("¿Cuantos jugadores jugaran? 1 o 2: "))

# Digitacion de nombre para el Player1 y Player2 (o enemigo):   
    if cantidad==1:
        nombreA=input("Nombre del Jugador1: ")
        nombreB=input("Nombre del enemigo: " )
        print("******************************************************************************************")
        print ("Hola ",nombreA, "bienvenido a la alpha del juego, usted se enfrentara contra ",nombreB, " por la gloria.¿Estas listo para jugar?")
    else:
        nombreA=input("Nombre del Jugador1: ")
        nombreB=input("Nombre del Jugador2: ")
        print("*******************************************************************************************")
        print ("Hola  ",nombreA," y ",nombreB, " bienvenidos a la alpha del juego, ustedes se enfrentaran por la gloria. ¿Estais listo para jugar?")
    
# Usuario selecciona el tipo de preguntas que desea resolver:
def categorias():
    global categoria_elegida
        
    print("Las categorias disponibles son: ")
    
    for i in categorias_array:
        print (" ",i," ")

    eleccion = input("Digite la letra correspondiente a la categoria:  ")

    if eleccion == "a" or eleccion == "A":
        categoria_elegida= "Cultura general"
    elif eleccion == "b" or eleccion == "B":
        categoria_elegida= "Marvel"
    elif eleccion == "c" or eleccion == "C":
        categoria_elegida= "Musica"
    elif eleccion == "d" or eleccion == "D":
        categoria_elegida= "Historia"
    elif eleccion == "e" or eleccion == "E":
        categoria_elegida= "Ciencia"
    else:
        categoria_elegida= "Tecnologia"

return categoria_elegida
 
def preguntasHistoria():

    global ContadorA

    print("¿En que año nacio Napoleon?")
    for i in opcionesHistoria[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="B" or "b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")

# FUNCIONA PARA LLEVAR LA CUENTA DEL JUGADOR O JUGADORES, Y SABER QUIEN HA GANADO
def contadores():
    
    if cantidad == 2:
        print ("El participante ",nombreA," tiene ",ContadorA," puntos")
        print ("El participante ",nombreB," tiene ",ContadorB," puntos")

        if ContadorA > ContadorB:
            print("El ganador es ",nombreA)
        elif Contador A < Contador B:
            print("EL ganador es ",nombreB)
        else:
            print("La victoria se decidira con una pregunta extra!!")
    else:
        print ("El participante ",nombreA," tiene ",ContadorA," puntos")
        
        if ContadorA == 5:
            print ("Felicidades has derrotado a",villano,"!!")
        else:
            print (villano,"te ha vencido, intentalo en otra vida")
    
def preguntasCulturaGeneral():
    global ContadorA
    global Respuesta
    print("¿Quien escribio la Odisea?")
    for i in opcionesCultura[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="B" or Respuesta=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else: 
        print("Respuesta incorrecta")
    print("\n")
        
    print("¿Con que instrumento se mide la temperatura")
    for i in opcionesCultura[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="C" or Respuesta=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    print("¿Cuando empezo la segunda guerra mundial?")
    for i in opcionesCultura[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="A" or Respuesta=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    print("¿Cual es el metal mas caro del mundo?")
    for i in opcionesCultura[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="C" or Respuesta=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    print("¿En que pais se encuentra la universidad de Cambridge?")
    for i in opcionesCultura[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="A" or Respuesta=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    print("¿Cual es el libro sagrado del Islam?")
    for i in opcionesCultura[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    if Respuesta=="B" or Respuesta=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")
    
        

def preguntasMarvel():
    print ("Hola Marvel")

def preguntasMusica():
    print("Hola Musica")

def preguntasCiencia():
    print("Hola Ciencia")

def preguntasTecnologia():
    print("Hola Tecnologia")



    
    

