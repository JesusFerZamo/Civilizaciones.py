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
matrix = [] # Matriz de elementos numéricos

entrada = f.read()

l = entrada.split("\n")

for i in range(len(l)):
    n.append(l[i].split(":")[0]) # Almacena los nombres de variables
    m.append(l[i].split(":")[1]) # Almacena listas de elementos
    matrix.append([])
    matrix[i] = m[i].split(",")  # Almacena elementos de la lista de elementos en matrix
 
print(entrada)
print(matrix[2][0])

f.close