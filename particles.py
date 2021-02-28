import timeit
t1 = timeit.timeit()
import math
H = input()
H = int(H)
ini = list(map(int,input().split()))
vel = list(map(int,input().split()))
dirc = list(input().split())
dirc = [1 if x=="U" else -1 for x in dirc]
thr = [H if x== 1 else 0 for x in dirc]
mov = [dirc[i]*vel[i] for i in range(4)]
A = [[0,ini[0],H],[H,ini[1],H],[H,ini[2],0],[0,ini[3],0]]
brek = 0

def dist(a,b):
    x = b[0]-a[0]
    x= math.pow(x,2)
    y = b[1]- a[1]
    y = math.pow(y,2)
    z = b[2] - a[2]
    z = math.pow(z,2)
    r = x+y+z
    r = math.sqrt(r)
    return r

def comp(a):
    AB = dist(a[0],a[1])
    BC = dist(a[1],a[2])
    CD = dist(a[2],a[3])
    DA = dist(a[3],a[0])
    AC = dist(a[0],a[2])
    s1 = (float (AB +BC +AC))/2
    a1 = s1*(s1-AB)*(s1-BC)*(s1-AC)
    a1 = math.sqrt(a1)
    s2 = (float(AC+CD+DA)) /2
    a2 = s2*(s2-AC)*(s2-CD)*(s2-DA)
    a2 = math.sqrt(a2)
    a = a1+a2
    a = math.pow(a,2)
    return a

maxx = comp(A)
minn = comp(A)
#print("initial area = " minn)
#counter = 0
while(1):
    #counter += 1
    #print("counter = " , counter)
    if (A[0][1] != thr[0]):
        A[0][1] += mov[0]
    else:
        brek += 1
        
    if (A[1][1] != thr[1]):
        A[1][1] += mov[1]
    else:
        brek += 1
    
    if (A[2][1] != thr[2]):
        A[2][1] += mov[2]
    else:
        brek += 1
        
    if (A[3][1] != thr[3]):
        A[3][1] += mov[3]
    else:
        brek += 1
    
    inter = comp(A)
    if(inter> maxx):
        maxx = inter
    if(inter<minn):
        minn = inter
        
    if(brek==4):
        break

print(round(4*maxx) , round(4*minn))
t2 = timeit.timeit()
print(t2-t1)