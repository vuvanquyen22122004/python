import math
def check(n):
    for j in range(len(n)):
        if int(n[j])%2!=0:
            return 0
    return 1
a = []
def sinh():
    for h in range(2,889):
        if check(str(h))==1:
            a.append(str(h))
sinh()
for i in range(int(input())):
    n = input()
    for i in range(len(a)):
        if (int(a[i]+a[i][::-1]))<int(n):
            print(f"{a[i]}{a[i][::-1]}",end=" ")

    print()
