# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:59:09 2020

@author: Varun Bhaaskar
"""
import math

N = list(map(int,input().split()))
r = N[0]
strt = list(map(int,input().split()))

vel = list(map(int,input().split()))

dirc =list(map(int,input().split()))
dirc = [1 if x==1 else -1 for x in dirc]

time = input()
time = int(time)
total = 0

centres = [r, r+N[1], r+N[2], r+N[3]]

deg = [vel[i]*dirc[i]*time for i in range(4)]

final_deg = [strt[i]+deg[i] for i in range(4)]
final_deg = [math.radians(x) for x in final_deg]

coor = []

for i in range(4):
    p=[r*math.cos(final_deg[i]), r*math.sin(final_deg[i])]
    p = [round(x,2) for x in p]
    p[0] += centres[i]
    coor.append(p)
    
def dist(a,b):
    x = b[0]-a[0]
    x= math.pow(x,2)
    y = b[1]- a[1]
    y = math.pow(y,2)
    r = x+y
    r = math.sqrt(r)
    return r

for i in range(3):
    res = dist(coor[i],coor[i+1])
    total += res
    
print(round(total))
