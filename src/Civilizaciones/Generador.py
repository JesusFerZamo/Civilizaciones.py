# coding: utf-8
'''
Created on 6 feb. 2018
@author: Jesús
'''

from random import randrange

fichero = input("Nombre del fichero: ")
fich = open(fichero+".txt", "w")

# Creación de listas
c       = [] # Caracteristicas
rmin    = [] # Rango mínimo
rmax    = [] # Ranto máximo
lista0  = []
lista1  = []
lista2  = []
lista3  = []
lista4  = []

# Almacenamiento de características y rangos por parte del usuario
for x in range(5):
    c.append(input("Característica " + str(x) + ": "))
    rmin.append(int(input("Rango mínimo " + c[x] + ": ")))
    rmax.append(int(input("Rango máximo " + c[x] + ": ")))

# Bucle para rellenar las diferentes listas siguiendo el rango establecido por el usuario
for x in range(1000):
    lista0.append(randrange(rmin[0],rmax[0]))
    lista1.append(randrange(rmin[1],rmax[1]))
    lista2.append(randrange(rmin[2],rmax[2]))
    lista3.append(randrange(rmin[3],rmax[3]))
    lista4.append(randrange(rmin[4],rmax[4]))
    
# Declaración de variable de tipo cadena salida para la extracción de los datos
salida = c[0] + ":" + str(lista0).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[1] + ":" + str(lista1).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[2] + ":" + str(lista2).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[3] + ":" + str(lista3).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[4] + ":" + str(lista4).replace("[", "").replace("]", "").replace(" ", "")

print(salida) # Impresión por pantalla la salida
fich.write(salida) # Escritura la salida en el fichero establecido

fich.close()