# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:58:45 2021

@author: USER
"""

s=" "
primernombre= input("ingrese su nombre: ")
segundonombre= input("ingrese apellido:")
ubi=input("ingrese su ubicaion: ")
edad= int (input("ingrese su edad"))

print ( "su nombre es:",primernombre,"su apellido es:",segundonombre,"su ubicacion es:",ubi,"la edad es:",edad)
if edad>=1 and edad<=12:
    print ("la edad es de niño")
elif edad>=13 and edad<=18:
    print(" la edad es de adolecnte")
elif edad>=19 and edad<=50:
    print(" la edad es de mayor")
elif edad>=51 and edad<=100:
|    print(" la edad es de adulto mayor")