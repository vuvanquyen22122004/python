import math
def nt(n):
    if n==0 or n==1:
        return False
    else:
        for j in range(2,int(math.sqrt(n))+1):
            if n%j==0:
                return False
    return True
n,m=map(int,input().split())
a=[]
re=[]
maxi=2
b={}
check=True
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if nt(a[i][j])==True:
            if a[i][j]>maxi:
                check=False
                maxi=a[i][j]
                re=[(i,j)]
            elif a[i][j]==maxi:
                re.append((i,j))
if check==True:
    print("NOT FOUND")
else:
    print(maxi)
    for h in re:
        print(f"Vi tri [{h[0]}][{h[1]}]")



