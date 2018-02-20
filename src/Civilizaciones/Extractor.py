# coding: utf-8
'''
Created on 19 feb. 2018

@author: javier
'''

G=globals()
for i in range(10):
  G["grupo%d"%i]=0

print( G[2])