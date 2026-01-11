from collections import defaultdict
t =int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mp = defaultdict(int)
    for i in range(n):
        mp[a[i]]+=1
    res=0
    for i in range(n):
        if mp[a[i]]>res:
            res=mp[a[i]]
    a.sort()
    ok=True
    for i in range(n):
        if mp[a[i]]==res and mp[a[i]]>n/2:
            print(a[i])
            ok=False
            break
    if ok==True:
        print("NO")