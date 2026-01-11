class xe:
    def __init__(self,bienso,xe,cho,loidi,ns):
        self.bienso=bienso
        self.xe=xe
        self.cho=cho
        self.loidi=loidi
        self.ns=ns
    def check(self):
        if self.loidi!="IN":
            return 0
        if self.xe=="Xe_con" and self.cho=='5':
            return 10000
        elif self.xe=="Xe_con" and self.cho=='7':
           return 15000
        elif self.xe=="Xe_tai" and self.cho=='2':
           return 20000
        elif self.xe=="Xe_khach" and self.cho=='29':
            return 50000
        else:
            return 70000

if __name__=='__main__':
    t=int(input())
    ds=[]
    a={}
    for i in range(t):
        bienso,loaixe,cho,loidi,ns=list(input().strip().split())
        ds.append(xe(bienso,loaixe,cho,loidi,ns))
    for d in ds:
        if d.ns not in a:
            a[d.ns]=d.check()
        else:
            a[d.ns]=a[d.ns]+d.check()
    for j in sorted(a.keys()):
        print(f"{j}: {a.get(j)}")






