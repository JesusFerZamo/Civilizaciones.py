# coding: utf-8
'''
Created on 6 feb. 2018
@author: Jesus
'''
fichero = input("Nombre del fichero")
fich = open(fichero+".txt", "w")

print("Introduzca las 5 características con sus rangos por favor")
c1 = input("Característica 1: ")
r1 = input("Rango de " + c1)
c2 = input("Característica 2: ")
r2 = input("Rango de " + c2)
c3 = input("Característica 3: ")
r3 = input("Rango de " + c3)
c4 = input("Característica 4: ")
r4 = input("Rango de " + c4)
c5 = input("Característica 5: ")
r5 = input("Rango de " + c5)
print("De acuerdo: ")

civi = {
    "Maya":0, "Azteca":0, "Incas":0, "Romana":0, "Egipcia":0
    }

for x, y in civi.items():
    print(x, y)
    
fich.write(str(civi))
fich.close()