# coding: utf-8
'''
Created on 19 feb. 2018

@author: javier
'''

#n = input("Nombre del fichero (sin extensión): ")
n = "ImperioRomano"
f = open(n + ".txt", "r")

entrada = f.read()

print(entrada)

f.close