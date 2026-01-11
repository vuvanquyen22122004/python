s1=input().split()
s2=input().split()
x1,x2=set(),set()
for i in s1:
    x1.add(i.lower())
    for j in s2:
        if i.lower()==j.lower():
            x2.add(j.lower())
for j in s2:
    x1.add(j.lower())
for i in sorted(x1):
    print(i,end=" ")
print()
for j in sorted(x2):
    print(j,end=" ")