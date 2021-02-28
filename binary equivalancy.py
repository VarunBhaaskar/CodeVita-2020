# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 07:13:06 2020

@author: Varun Bhaaskar
"""

from itertools import combinations


N = int(input())
a = list(map(int,input().split()))
a.sort()
largest = len(bin(a[-1])) - 2
result = 0

def binaryEq(b):
    global result
    bi = []
    n1 = 0
    n0 = 0
    for x in b:
        z = bin(x).replace("0b", "")
        #z = str(z)
        m = len(z)
        if (m != largest):
            dif = largest - m
            for q in range(dif):
                z = '0'+z
        
        bi.append(z)
    for p in bi:
        for l in p:
            if l=='0':
                n0 +=1
            else:
                n1 +=1
    print(b,bi,n0,n1)
    if (n1==n0):
        result += 1

for i in range(1,N+1):
    T = combinations(a, i)
    T = list(T)
    for y in T:
        y = list(y)
        binaryEq(y)

result = bin(result).replace("0b","")
m = len(result)
if (m != largest):
            dif = largest - m
            for q in range(dif):
                result = '0'+ result

print(result)


        