# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
seznam = [random.randint(1,50) for a in range(20)]
k1 = ("sudých čísel je:")
x=0
for a in seznam:
    if a % 2 == 0:
        x=x+1

print(seznam)
print()
print(k1, x) 



print()
print()
print()



seznam = [random.randint(1,50) for b in range(20)] 
k2=("Čísla větší než 11 a menší než 19 jsou: ")

print(seznam)
print()
print(k2)

for b in seznam:
    if b>11 and b<19:
        print(b)



print()
print()
print()



seznam = [random.randint(1,50) for c in range(20)]
k3=("čísla která jsou dělitelná 3 a 4 zároveň: ")

print(seznam)
print()
print(k3)

for c in seznam:
    if c % 3 == 0:
        if c % 4 ==0:
            print(c)
            

f = int(input("počet čísel v Fibonacciho posloupnosti: "))
m = 0
n = 1
while f > 0:
    print (n)
    m = n + m
    n = m - n
    f += -1
print()



