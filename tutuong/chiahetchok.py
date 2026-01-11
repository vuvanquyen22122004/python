

a,k,n=[int (j) for j in input().split()]



def nhohonn(a,k,n):
    ok=0
    for i in range(1,n+1):
        if a%k==0:
            if a+(a%k)<=n:
                print(a%k,end=" ")
                ok=1
    if(ok==0):
        print("-1")



nhohonn(a,k,n)