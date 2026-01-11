n = input()
ok = True
hit =0
for i in range(len(n)):
    if n[i]!='6'and n[i]!='8':
        ok=False
        break
    if n[i]=='8': hit+=1
    elif n[i]!='8': hit = 0
    if hit ==3:
        ok = False
        break



if ok:
    print("YES")
else:
    print("NO")
