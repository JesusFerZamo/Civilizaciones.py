# coding: utf-8
'''
Created on 19 feb. 2018

@author: javier
'''

#n = input("Nombre del fichero (sin extensión): ")
n = "ImperioRomano"
f = open(n + ".txt", "r")

l = [] # Lista primigenia
n = [] # Lista de nombres de variables
m = [] # Lista de elementos de cada variable
k = []
n0 = []
n1 = []
n2 = []
n3 = []
n4 = []

entrada = f.read()

l = entrada.split("\n")

for i in range(len(l)):
    n.append(l[i].split(":")[0]) # Almacena los nombres de variables
    m.append(l[i].split(":")[1])
    k.append([])
    k[i] = m[i].split(",")
 
print(entrada)
print(k[2][0])

f.close