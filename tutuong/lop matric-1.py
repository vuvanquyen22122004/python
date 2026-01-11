t = int(input())
for _ in range(t):
    a = []
    n, m = map(int, input().split())
    for _ in range(n):
        a.append(list(map(int, input().split())))
    b = [[0 for i in range(n)] for _ in range(m)]
    res = [[0 for i in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(m):
            b[i][j] = a[j][i]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n): print(res[i][j], end = ' ')
        print()