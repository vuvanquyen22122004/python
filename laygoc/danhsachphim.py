class Phim:
    def __init__(self,id,matl,ns,ten,tap):
        self.ma=f"P{id:03d}"
        self.matl=matl
        self.tl=""
        self.ns=ns
        self.ten=ten
        self.tap=tap
        d,m,y=self.ns.split("/")
        self.ngay=int(d)
        self.thang=int(m)
        self.nam=int(y)
    def __str__(self):
        return f"{self.ma} {self.tl} {self.ns} {self.ten} {self.tap}"
if __name__=='__main__':
    n,m=map(int,input().split())
    ar={}
    for i in range(n):
        ar[f"TL{i+1:03d}"]=input()
    ds=[]
    for i in range(m):
        ma=input()
        ns=input()
        ten=input()
        tap=int(input())
        ds.append(Phim(i+1,ma,ns,ten,tap))
        ds[i].tl=ar[ma]
    ds.sort(key=lambda x:(x.nam,x.thang,x.ngay,x.ten,-x.tap))
    for d in ds:
        print(d)