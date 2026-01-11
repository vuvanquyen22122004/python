import math
def checkscs(n):
    if len(n) %2==0:
        return 1
    return 0
def checktn(n):
    b = n[::-1]
    a=0
    while a<len(n):
        if n[a]!=b[a] or int(n[a])%2!=0:
            return 0
        a+=1
    return 1

for i in range(int(input())):
    n = int(input())
    if n>22:
        for j in range(10,n):
            if checkscs(str(j))==1 and checktn(str(j))==1:
                print(j,end=" ")
    print()
