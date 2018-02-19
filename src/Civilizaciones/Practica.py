# coding: utf-8
'''
Created on 6 feb. 2018
@author: Jesus
'''
fichero = input("Nombre del fichero")
fich = open(fichero+".txt", "w")

print("Introduzca las 5 características")
c1 = input("Característica 1: ")
c2 = input("Característica 2: ")
c3 = input("Característica 3: ")
c4 = input("Característica 4: ")
c5 = input("Característica 5: ")
print("De acuerdo: ")

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)

civi = {
    "Maya":0, "Azteca":0, "Incas":0, "Romana":0, "Egipcia":0
    }

for x, y in civi.items():
    print(x, y)
    
fich.write(str(civi))
fich.close()