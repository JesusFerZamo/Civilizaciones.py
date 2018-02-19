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

diccionario = {"cadena": "abc", "numero": 42, "lista": [True, 42]}  # Diccionario que tiene diferentes valores por cada clave, incluso una lista
print(diccionario["cadena"])  # Usando una clave, se accede a su valor
print(diccionario["lista"][0])  # Acceder a un elemento de una lista dentro de un valor (del valor de la clave "lista", mostrar el primer elemento)
diccionario["cadena"] = "xyz"  # Re-asignar el valor de una clave
print(diccionario["cadena"])
diccionario["decimal"] = 3.1415927  # Insertar un nuevo elemento clave:valor
print(diccionario["decimal"])
diccionario_mixto = {"tupla": (True, 3.1415), "diccionario": diccionario}  # También es posible que un valor sea un diccionario
print(diccionario_mixto["diccionario"]["lista"][1])  # Acceder a un elemento dentro de una lista, que se encuentra dentro de un diccionario
diccionario = {("abc",): 42}  # Sí es posible que una clave sea una tupla, pues es inmutable
diccionario = {["abc"]: 42}  # No es posible que una clave sea una lista, pues es mutable, lo que provocará una excepción

civi = {
    "Maya":0, "Azteca":0, "Incas":0, "Romana":0, "Egipcia":0
    }

for x, y in civi.items():
    print(x, y)
    
fich.write(str(civi))
fich.close()