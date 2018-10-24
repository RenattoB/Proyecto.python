#Entrada
from Funciones import *

#codigo
inicio()
a =categorias()


if a== "Historia" :
    print("Usted selecciono la categoria de Historia")
    preguntasHistoria()
elif a=="Cultura general":
    print("Usted selecciono la categoria Cultura general")
    preguntasCulturaGeneral()
elif a=="Marvel":
    print("Usted selecciono la categoria Marvel")
    preguntasMarvel()
elif a=="Musica":
    print("Usted selecciono la categoria de Musica")
    preguntasMusica()
elif a=="Ciencia":
    print("Usted selecciono la categoria de Ciencia")
    preguntasCiencia()
else:
    print("Usted selecciono la categoria de Tecnologia")
    preguntasTecnologia()
contadores()
