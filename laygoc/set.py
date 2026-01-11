import math
for i in range(int(input())):
    n = int(input())
    for  j in range(2,int(math.sqrt(n))+1):
        cnt=0
        if n%i==0:
            while(n%i==0):
                cnt+=1
                n/=i
        print(f'* {i} ^ {cnt}',end='')
    if(n>1):
        print(f'* {n}^ 1',end=" ")




