for q in range(int(input())):
    n = input()
    if int(n[0])!=0:
        tich=int(n[0])
    else:
        tich = 1
    tong=0
    for j in range(1,len(n)):
        if j % 2==0 and int(n[j])!=0:
            tich*=int(n[j])
        elif j %2!=0 :
            tong+=int(n[j])
    if tong==0:
        print("INVALID")
    else:
        print(f"{tich/tong:.6f}")