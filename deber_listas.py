# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:30:23 2021

@author: USER
"""

N= int(input("ingrese el tamaño del vector"))
A=[]
while N<=4 or N>20 :
      print("error")
      print("el tamaño del vector debe ser mayor que 4 y menor que 20")
      N= int(input("ingrese el tamaño del vector"))

for x in range(N):
    valor=int(input("Ingrese un valor entero:"))
    A.append(valor)
print(A)    
   
   