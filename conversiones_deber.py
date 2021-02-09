# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:43:10 2021

@author: USER
"""
kilo=334 #iniciamos una constante
horasa_ac=float(input("ingrese el tiempo en horas de conduccion actual"))#pedimos el ingreso de ddatos"""
desplazamiento=int(input("Ingrese la velocidad de desplazamiento"))#pedimos el ingreso de datos"""

total_dist= horasa_ac*desplazamiento #esa variable tendra como resultado la distancia recorrida"""
print(" la distancia recorrida al momento es:" ,total_dist) #mandamos a imprimir el resultado """

dist_faltante= kilo-total_dist# esta variable tendra como resultado la distancia faltante"""
print("La distancia faltante por recorrer es:",dist_faltante) #mandamos a imprimir el resultado"""
destino= dist_faltante/desplazamiento #usamos la formula de (mru) para sacar el timpo de llegada"""
print("usted lleorasa_acgara a su destino en:",destino,"horas")#imprimimos el resultado de la variable anterior"""
