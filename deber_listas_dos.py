# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:38:35 2021

@author: USER
"""
N= int(input("ingrese tamaño de la lista 1"))
A=[]

while N<=4 or N>20 :
      print("error")
      print("el tamaño del vector debe ser mayor que 4 y menor que 20")
      N= int(input("ingrese tamaño de la lista 1"))

for x in range(N):
    valor=str(input("Ingrese nombres:"))
    A.append(valor)

 
N= int(input("ingrese tamaño de la lista numero 2"))
B=[]
while N<=4 or N>20 :
      print("error")
      print("el tamaño del vector debe ser mayor que 4 y menor que 20")
      N= int(input("ingrese tamaño de la lista numero 2"))


for x in range(N):
    valor=str(input("Ingrese apellidos:"))
    B.append(valor)
print("el resultado de la lista 1 es:")
print(A)

print("el resultado de la lista 2 es:")
print(B)    
   
   