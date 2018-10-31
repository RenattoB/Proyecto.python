#Entrada
from Funciones import *

#codigo
inicio()
a = elegir_categoria()

if a== "Historia" :
    print("\n""Usted selecciono la categoria de Historia: ""\n")
    preguntasHistoria()
elif a=="Cultura general":
    print("\n""Usted selecciono la categoria Cultura general: ""\n")1
    preguntasCulturaGeneral()
elif a=="Marvel":
    print("\n""Usted selecciono la categoria Marvel: ""\n")
    preguntasMarvel()   
elif a=="Musica":
    print("\n""Usted selecciono la categoria de Musica: ""\n")
    preguntasMusica()
elif a=="Ciencia":
    print("\n""Usted selecciono la categoria de Ciencia: ""\n")
    preguntasCiencia()
elif a=="Dibujos Animados":
    print("\n""Usted selecciono la categoria de Dibujos Animados: ""\n")
    preguntasDibujos()    
else:
    print("\n""Usted selecciono la categoria de Tecnologia: ""\n")
    preguntasTecnologia()

contadores()
