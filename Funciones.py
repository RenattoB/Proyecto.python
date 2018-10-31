
# Excepcion

import sys

# Variables
villano="default"
nombreA="default"
nombreB="default"
cantidad="default"
categoria_elegida="Default"
eleccion="Default"
Respuesta="Default"
ContadorErrores=0
ContadorA=0
ContadorB=0

categorias =["a) Cultura general","b) Marvel","c) Musica","d) Historia", "e) Ciencia","f) Dibujos Animados","g) Tecnologia""\n"]

# ARREGLO DE CLAVES - CULTURA GENERALt:
opcionesCultura = [["a. Mario Vargas Llosa","B. Homero","C. Pablo Neruda"]
,["a. Odometro","b. Interferometro","c. Termometro"]
,["a. 1914","b. 1915","c. 1913"]
,["a. Oro","b. Diamante","c. Rodio"]
,["a. ReinoUnido","b. España","c. Francia"]
,["a. Biblia","b. Coran","c. Dhammapada"]]

# ARREGLOS DE CLAVES - MARVEL:
opcionesMarvel = [["a. Normamu ","b. Voldemort" , "c. The Ancient"]
,["a. Red Skull and Gamora","b. Red Skull and minerva" , "c. Gamora and Red Skull"]
,["a. New York","b. El Pentagono (Nave SHIELD)" , "c. Asgard"]
,["a. Aether","b. Chitauri Scepter" , "c. Orb"]
,["a. Modifica las leyes de la realidad y Moldea las leyes de la física","b. Super velocidad y Viajar en el espacio-tiempo" , "c. Traspasar cosas solidad e inmunidad a las balas"]
,["a. Iron man ","b. Thor" , "c. Wanda"]]

# ARREGLO DE CLAVES - MUSICA:
opcionesMusica = [["a. Des O'Connor","B. Roy Orbison","C. Ozzy Osbourne"]
,["a. Lead Piping ","b. Candlestick","c. Revolver"]
,["a. Black Sabbath","b. Manfred Mann","c. Led Zeppelin"]
,["a. 1983","b. 1978","c. 1988"]
,["a. Linkin Park","b. Fort Minor","c. X-Ecutioners"]
,["a. The White Rabbit","b. 8 mile","c. Stand"]]

# ARREGLO DE CLAVES -  HISTORIA:
opcionesHistoria = [["a. australiana - asiatico - oceanico","b. asiatico - australiano - africana","c. asiatica - oceanico - australiano"]
,["a. Magicos y Didacticos","b. Filosoficos y Economicos","c. Religiosos y Politicos"]
,["a. El monopolio del Comercio de Azucar","b. El impuesto al consumo de alcohol","c. La separacion de los funcionarios criollos"]
,["a. La mineria y la agricultura","b. La plata y el tributo indigena","c. La mita obrajera y la plata"]
,["a. Francia y Belgica","b. Estados unidos y Alemania","c. Inglaterra y Holanda"]
,["a. El desplazamiento de la Hegemonia inglesa por la norteamericana","b. El surgimiento de una alianza entre la clase media y la burguesia limeña","c. La instauracion de un modelo de desarrollo bajo la hegemonia de la mineria"]]

# ARREGLO DE CLAVES - CIENCIA:
opcionesCiencia = [["a. 1ra Ley de Newton","b. 2da Ley de Newton","c. 3ra Ley de Newton"]
,["a. 17","b. 14","c. 12"]
,["a. La temperatura","b. EL numero de atomos","c. El volumen "]
,["a. Ne","b. Kr","c. N"]
,["a. Cuando no existe la gravedad","b. Cuando no actuan fuerzas externas sobre el cuerpo ","c. Si el cuerpo posee una masa despreciable"]
,["a. C - Grupo 15","b. Zn - Grupo 12","c. Ni - Grupo 14"]]

# ARREGLO DE CLAVES - TECNOLOGIA:
opcionesTecnologia = [["a. Una tableta robusta","b. Sitios de internet dedicados a la farmacéutica","c. Un dispositivo mezcla entre celular y tableta"]
,["a. Un delincuente informático","b. Un virus muy peligroso","c. Una persona estudiosa y experta en tecnología"]
,["a. Un código de ‘software’ con objetivo malicioso","b. Un virus de celular","c. Un trino de un político en campaña"]
,["a. La cosa que forma el corazón de internet","b. La posibilidad de que cualquier cosa se conecte a internet","c. El internet que se usa en cualquier cosa"]
,["a. Las comunicaciones 4G LTE celulares","b. Servicios informáticos que operan desde internet","c. Los datos que viajan sin cables por el cielo"]
,["a. Gran cúmulo de información que se produce y existe en internet ","b. Es un supercomputador japonés","c. La gran cantidad de datos que hay en un computador"]]

# ARREGLO DE CLAVES - DIBUJOS ANIMADOS:
opcionesDibujos = [["a. Es su hermano","b. Es su primo","c. Es un amigo"]
,["a. Mark Lenders","b. Philip Ross","c. Andy Johnson"]
,["a. Sheen y Carl","b. Sheen y Carman","c. Carl y Shen"]
,["a. Tutty","b. Trixie","c. Wanda"]
,["a. Neptunoman","b. Chico Perseve","c. Sirenoman"]
,["a. Tierra","b. Agua","c. Fuego"]]

Respuesta="Default"

# FUNCIONES

def inicio():
    global ContadorErrores
    global nombreA
    global nombreB
    global villano
    global cantidad
    
# MODO DE JUEGO

## Excepcion:

    while True:
        ContadorErrores+=1
        if ContadorErrores==5:
            print("Numero de veces equivocado excedido""\n""Programa finalizado")
            sys.exit()
        try:
            cantidad=int(input("\n""¿Cuantos jugadores jugaran? 1 o 2: "))
            if cantidad==1 or cantidad==2:
                break
            print("Cantidad invalida""\n""Por favor introduzca una cantidad valida")
        except:
            print("Entrada incorrecta, por favor ingrese un numero entero")

# NOMBRE PLAYER1 Y PLAYER2 (O ENEMIGO)  
    
    if cantidad==1:
        nombreA=input("Nombre del Jugador: ")
        villano=input("Nombre del Enemigo: " )
            
        print("****************************************************************************************************************************************************")
        print ("Hola ",nombreA, "bienvenido a la alpha del juego, usted se enfrentara contra ",villano, " por la gloria. ¿Estas listo para jugar?")
    
    elif cantidad==2:
        nombreA=input("Nombre del Jugador1: ")
        nombreB=input("Nombre del Jugador2: ")
        print("****************************************************************************************************************************************************")
        print ("Hola  ",nombreA," y ",nombreB, " bienvenidos a la alpha del juego, ustedes se enfrentaran por la gloria. ¿Estais listo para jugar?")
    
# USUARIO SELECCIONA LA CATEGORIA DE PREGUNTAS

def elegir_categoria():
    global categoria_elegida
        
    print("\n""Las categorias disponibles son: ""\n")

    for i in categorias:
        print (" ",i," ")

    while True:
        eleccion = input("Digite la letra correspondiente a la categoria:  ")
        if eleccion.lower()=="a" or eleccion.lower()=="b" or eleccion.lower()=="c" or eleccion.lower()=="d" or eleccion.lower()=="e" or eleccion.lower()=="f" or eleccion.lower()=="g":
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
            elif eleccion == "f" or eleccion == "F":
                categoria_elegida= "Dibujos Animados"
            else:
                categoria_elegida= "Tecnologia"
            return categoria_elegida
            break
        print("Digite una categoria valida por favor""\n")
    

# FUNCIONA PARA LLEVAR LA CUENTA DEL JUGADOR O JUGADORES, Y SABER QUIEN HA GANADO
def contadores():
    

    if cantidad == 2:
        print ("El participante ",nombreA," obtubo ",ContadorA," puntos")
        print ("El participante ",nombreB," obtubo ",ContadorB," puntos")

        if ContadorA > ContadorB:
            print("El ganador es ",nombreA)
        elif ContadorA < ContadorB:
            print("EL ganador es ",nombreB)
        else:
            print("La victoria se decidira con una pregunta RANDOM!!")
            print("\n""De un avion salta un negro y un judio quien cae mas rapido?")
            respuestaA = input(nombreA," dice: La respuesta es: ")
            if respuestaA.lower() == "a" :
                print("Usted ha ganado")
            else:
                print("Ha perdido")
                    
            respuestaB = input(nombreB," dice: La respuesta es: ")
            if respuestaB == "a" or respuestaB == "A":
                print("Jugador ",nombreB," usted ha ganado!!!")
            else:
                print("Ha perdido")
                    
            print ("Gracias por juegar")
    else:
        print ("El participante ",nombreA," tiene ",ContadorA," puntos")
        
        if ContadorA == 5:
            print ("Felicidades has derrotado a",villano,"!!")
        else:
            print (villano,"te ha vencido, intentalo en otra vida")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE CULTURA GENERAL
  
def preguntasCulturaGeneral():

    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("¿Quien escribio la Odisea?")

    for i in opcionesCultura[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Con que instrumento se mide la temperatura?")

    for i in opcionesCultura[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("¿En que año inicio la segunda guerra mundial?")
    for i in opcionesCultura[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("¿Cual es el metal mas caro del mundo?")
    for i in opcionesCultura[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("¿En que pais se encuentra La Universidad de Cambridge?")
    for i in opcionesCultura[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("¿Cual es el libro sagrado del Islam?")
    for i in opcionesCultura[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE MARVEL

def preguntasMarvel():
 
    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("¿Quién es el maestro que le enseña las artes místicas a Dr.Strange?")

    for i in opcionesMarvel[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta=="C" or Respuesta=="c":
        ContadorA = ContadorA + 1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Quién cuida la gema? Y ¿A quien sacrifica Thanos para obtenerla?")

    for i in opcionesMarvel[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("¿En que lugar fue guardado la gema del espacio , tras los sucesos en el film Captain America?")
    for i in opcionesMarvel[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("¿Dónde era guardada la gema del poder, en Guardians of the Galaxy?")
    for i in opcionesMarvel[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("¿Qué habilidades te otorga la gema de la realidad?")
    for i in opcionesMarvel[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("¿Quién le da la gema de la mente a visión (en los comics)?")
    for i in opcionesMarvel[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE MUSICA

def preguntasMusica():

    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("¿ Que cantante era conocido como 'The big O' " )

    for i in opcionesCultura[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Cual de estos es el nombre de un álbum de los Beatles?")

    for i in opcionesCultura[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("¿Que banda de rock fundó Jimmy Page en 1968?")
    for i in opcionesCultura[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("¿En que año Culture Club obtuvo un numero 1 con Karma Chameleon?")
    for i in opcionesCultura[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("¿A cual de los siguientes grupos no pertenece Mike Shinoda?")
    for i in opcionesCultura[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("¿Cual fue el nombre de la pelicula de Eminem?")
    for i in opcionesCultura[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE HISTORIA

def preguntasHistoria():

    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("Las teorías inmigracionistas que explican el poblamiento de América son la de la procedencia... (Alex Hdrlicka), la de origen... (Paul Rivet) y la de procedencia... (Mendes Correia)." )

    for i in opcionesHistoria[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("Las pinturas rupestres con escenas de caza, halladas en las paredes de las cuevas de Lascaux y Altamira, fueron realizadas con propósitos.")

    for i in opcionesHistoria[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("Debido a los elevados gastos militares realizados por Inglaterra en la Guerra de los Siete Años contra Francia (1756-1763), el fisco quedó en ruina, motivo por el cual tuvo que adoptar medidas para generar ingresos. Una de estas fue...")
    for i in opcionesHistoria[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("Luego de canceladas la mayoría de las encomiendas por la aplicación de las denominadas Nuevas Leyes (1542), la economía colonial estuvo basada en las rentas que proporcionaban ...")
    for i in opcionesHistoria[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("La segunda Revolución Industrial, caracterizada por el uso de nuevas fuentes de energía y la especialización de los procesos de trabajo se desarrolló a finales del siglo XIX en países como...")
    for i in opcionesHistoria[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("La ruptura de Augusto B. Leguía con el Partido Civil, hacia 1919, significó la culminación de un proceso económico iniciado a comienzos del siglo XX en el Perú. ¿Cuál fue su característica central?")
    for i in opcionesHistoria[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE CIENCIA:

def preguntasCiencia():
    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("Cual de las 3 Leyes de Newton hace referencia la siguiente frase: El cambio de movimient es directamente proporcional a la fuerza motriz impresa y ocurre según la línea recta a lo largo de la cual aquella fuerza se imprime")

    for i in opcionesCiencia[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="b":
        ContadorA = ContadorA + 1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Cual es el número atomico del Carbono?")

    for i in opcionesCiencia[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("En un Proceso Isocóro se mantiene contante ........")
    for i in opcionesCiencia[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("¿Cual de los siguientes elementos no pertenece al grupo de los Gases Nobles?")
    for i in opcionesCiencia[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("¿Cuando se considera un evento de Conservacion de Energia?")
    for i in opcionesCiencia[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("¿Cual es la relacion incorrecta entre elemento - grupo en la tabla periodica ?")
    for i in opcionesCiencia[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE DIBUJOS ANIMADOS:

def preguntasDibujos():
    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("¿Que tipo de relacion tiene Diego con Dora la exploradora?")

    for i in opcionesDibujos[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="b":
        ContadorA = ContadorA + 1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Como se llama el futbolista que sufria del corazon en Los super campeones?")

    for i in opcionesDibujos[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("¿Como se llamaban los mejores amigos de Jimmmy Neutron?")
    for i in opcionesDibujos[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("¿Como se llamaba la chica de la cual Timmy Turner estaba enamorado?")
    for i in opcionesDibujos[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("¿Cual era el nombre del heroe que admiraba Bob Esponja?")
    for i in opcionesDibujos[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("¿En la serie Avatar cual fue el ultimo elemento que aprendio Aang?")
    for i in opcionesDibujos[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n")

'''//////////////////////////////////////////////////////////////////////////////////////////////////////////'''

# PREGUNTAS DE TECNOLOGIA:

def preguntasTecnologia():
    global ContadorA
    global Respuesta

    # PREGUNTA 1
    print("Una 'phablet' es: ")

    for i in opcionesDibujos[0]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA = ContadorA + 1
        print("Respuesta correcta tienes ",ContadorA," puntos") 
    else:   
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 2   
    print("¿Qué es un 'hacker'?")

    for i in opcionesDibujos[1]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="c":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 3
    print("¿Qué es un 'malware'?")
    for i in opcionesDibujos[2]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")

    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 4
    print("El 'internet de las cosas es': ")
    for i in opcionesDibujos[3]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 5 
    print("La 'computación en la nube' se le dice a: ")
    for i in opcionesDibujos[4]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="b":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else: 
        print("Respuesta incorrecta")
    print("\n")

    # PREGUNTA 6
    print("'Big data' se conoce como: ")
    for i in opcionesDibujos[5]:
        print (i)
    Respuesta=input("Ingrese la letra de su respuesta: ")
    
    if Respuesta.lower()=="a":
        ContadorA=ContadorA+1
        print("Respuesta correcta tienes ",ContadorA," puntos")
    else:
        print("Repuesta incorrecta")
    print("\n") 
