def solve():
    s = input()


    tong_chu_so = 0
    for digit in s:
        tong_chu_so += int(digit)

    if tong_chu_so % 10 != 0:
        print("NO")
        return

    for i in range(len(s) - 1):

        if abs(int(s[i]) - int(s[i + 1])) != 2:
            print("NO")
            return


    print("YES")



t = int(input())
while t > 0:
    solve()
    t -= 1