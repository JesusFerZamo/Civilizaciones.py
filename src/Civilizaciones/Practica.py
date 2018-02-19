# coding: utf-8
'''
Created on 6 feb. 2018
@author: Jesus
'''
from random import randrange
fichero = input("Nombre del fichero: ")
fich = open(fichero+".txt", "w")

print("Introduzca las 5 características con sus rangos por favor")
c1 = input("Característica 1: ")
r1a = int(input("Principio del rango " + c1 + ": "))
r1b = int(input("Final del rango " + c1+ ": "))
c2 = input("Característica 2: ")
r2a = int(input("Principio del rango " + c2 + ": "))
r2b = int(input("Final del rango " + c2 + ": "))
c3 = input("Característica 3: ")
r3a = int(input("Principio del rango " + c3 + ": "))
r3b = int(input("Final del rango " + c3 + ": "))
c4 = input("Característica 4: ")
r4a = int(input("Principio del rango " + c4 + ": "))
r4b = int(input("Final del rango " + c4 + ": "))
c5 = input("Característica 5: ")
r5a = int(input("Principio del rango " + c5 + ": "))
r5b = int(input("Final del rango " + c5 + ": "))
print("De acuerdo: ")

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

for x in range(1000):
    lista1.append(randrange(r1a,r1b))
    lista2.append(randrange(r2a,r2b))
    lista3.append(randrange(r3a,r3b))
    lista4.append(randrange(r4a,r4b))
    lista5.append(randrange(r5a,r5b))
    
d = {
    c1:lista1, c2:lista2, c3:lista3, c4:lista4, c5:lista5
    }

for x, y in d.items():
    print(x, y)
    
fich.write(str(d))
fich.close()