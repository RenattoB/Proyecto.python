#Entrada
from Funciones import *

#codigo
inicio()
a =categorias()
print(a)

if a== "Historia" :
    preguntasHistoria()
elif a=="Cultura general":
    preguntasCulturaGeneral()
elif a=="Marvel":
    preguntasMarvel()
elif a=="Musica":
    preguntasMusica()
elif a=="Ciencia":
    preguntasCiencia()
else:
    preguntasTecnologia()

