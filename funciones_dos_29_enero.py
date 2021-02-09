# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:32:51 2021

@author: USER
"""

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

print(is_prime(4))

for i in range(1, 1000):
    if is_prime(i + 1):
        print(i + 1, end=" ")
        