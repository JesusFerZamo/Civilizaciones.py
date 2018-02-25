# coding: utf-8
'''
Created on 19 feb. 2018
Objetivo: media, moda, máximo, mínimo y varianza

@author: javier
'''
from whoosh.externalsort import sort

'''
FUNCIONES
'''
# Cálculo de la media
def media(l):
    suma = 0
    total = len(l)
    
    for i in range(total):
        suma += int(l[i])
    resultado = suma / total
    return resultado

def moda(l):
    M = 0
    cont = 0
    ll=sort(l)
    for i in range(0,len(l)-1):
        if (ll[i] == ll[i+1]):
            cont = cont + 1
            if cont >= M:
                M = cont
                moda = ll[i]
        else:
            cont=0
 
    return moda

'''
CÓDIGO
'''
#n = input("Nombre del fichero (sin extensión): ")
n = "ImperioRomano"
f = open(n + ".txt", "r")

l = [] # Lista primigenia
n = [] # Lista de nombres de caracteristicas
matrix = [] # Matriz de elementos numéricos

entrada = f.read()

l = entrada.split("\n")

for i in range(len(l)):
    n.append(l[i].split(":")[0]) # Almacena los nombres de variables
    matrix.append([])
    matrix[i] = l[i].split(":")[1].split(",")  # Almacena elementos en matrix

print(entrada)
print(l[1].split(":")[1].split(","))
print(media(l[1].split(":")[1].split(",")))
print(moda(l[1].split(":")[1].split(",")))

f.close

