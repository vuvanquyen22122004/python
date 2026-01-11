from math import gcd
a,b,c,d=list(map(int,input().split()))
f=(b*d)//gcd(b,d)
a=(f//b)*a
b=(f//d)*c
print(f"{(a+b)//gcd(a+b,f)}/{f//gcd(a+b,f)}")
