for q in range(int(input())):
    c,d=list(map(int,input().split()))
    a = [0, 1]
    for i in range(2, 93):
        a.append(a[i - 2] + a[i - 1])
    for j in range(c,d+1):
        print(a[j],end=" ")
    print()

