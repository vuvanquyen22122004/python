class hoadon:
    def __init__(self,id,name,cu,moi):
        self.id=f"KH{id:02d}"
        self.name=name
        self.cu=cu
        self.moi=moi
        self.khoi=self.moi-self.cu
        if self.khoi<=50:
           self.gia=self.khoi*100
           self.phu=self.gia*0.02
           self.tong=self.gia+self.phu
        elif self.khoi>50 and self.khoi<=100:
            self.gia = 50*100+(self.khoi-50)*150
            self.phu = self.gia * 0.03
            self.tong = self.gia + self.phu
        else:
            self.gia = 50*100+50*150+(self.khoi-100)*200
            self.phu = self.gia * 0.05
            self.tong = self.gia + self.phu
    def __str__(self):
        return f"{self.id} {self.name} {round(self.tong)}"
if __name__=="__main__":
    t = int(input())
    ds=[]
    for i in range(t):
        ten=input()
        cu=int(input())
        moi=int(input())
        ds.append(hoadon(i+1,ten,cu,moi))
    ds.sort(key=lambda x: -x.tong)
    for d in ds:
        print(d)

