n = input()
a= list(map(float,input().split()))
a.sort()
mini=a[0]
maxi=a[len(a)-1]
sumi=0
cnt=0
for i in a:
    if i!=mini and i!=maxi:
        sumi+=i
        cnt+=1
if cnt!=0:
    print(f"{round(sumi/float(cnt),2):.2f}")
