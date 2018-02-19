# coding: utf-8
'''
Created on 6 feb. 2018
@author: Jesus
'''
fichero = input("Nombre del fichero")
fich = open(fichero+".txt", "w") 

civi = {
    "Maya":0, "Azteca":0, "Incas":0, "Romana":0, "Egipcia":0
    }

for x, y in civi.items():
    print(x, y)
    
fich.write(str(civi))
fich.close()