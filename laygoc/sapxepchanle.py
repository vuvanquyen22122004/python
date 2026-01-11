class tiendien:
    def __init__(self,id,ten,loai,dau,cuoi):
        self.id=id
        self.ten=ten
        self.dau=dau
        self.loai=loai
        self.cuoi=cuoi
    def sodm(self):
        if self.loai=='A':
            return 100
        elif self.loai=='B':
            return 500
        else:
            return 200
    def check(self):
        if self.cuoi-self.dau < self.sodm():
            return (self.cuoi-self.dau)*450
        return self.sodm()*450
    def tienvuotdm(self):
        if self.cuoi-self.dau > self.sodm():
            return ((self.cuoi-self.dau)-self.sodm())*1000
        return 0
    def thue(self):
        return self.tienvuotdm()//20
    def tien(self):
        return self.thue() + self.check() + self.tienvuotdm()
    def __str__(self):

        return f"{self.id} {self.ten} {self.check()} {self.tienvuotdm()} {self.thue()} {self.check()+self.tienvuotdm()+self.thue()}"
if __name__=="__main__":
    t = int(input())
    ds=[]
    for i in range(t):
        id = f"KH{i+1:02d}"
        ten=" ".join([x.title() for x in input().strip().split()])
        loai,dau,cuoi=list(input().strip().split())
        ds.append(tiendien(id,ten,loai,int(dau),int(cuoi)))
    ds.sort(key=lambda x:-x.tien())
    for d in ds:
        print(d)