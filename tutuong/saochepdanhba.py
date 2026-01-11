class Dien:
    def __init__(self,id,ten,cu,moi):
        self.ma=f"KH{id:02d}"
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.khoi=moi-cu
        if self.khoi<51:
            self.gia=self.khoi*100
            self.phu=self.gia*0.02
            self.tong=self.gia+self.phu
        elif self.khoi<101:
            self.gia=50*100+(self.khoi-50)*150
            self.phu=self.gia*0.03
            self.tong=self.gia+self.phu
        else:
            self.gia=50*100+50*150+(self.khoi-100)*200
            self.phu=self.gia*0.05
            self.tong=self.gia+self.phu
    def __str__(self):
        return f"{self.ma} {self.ten} {round(self.tong)}"
if __name__=='__main__':
    n=int(input())
    ds=[]
    for i in range(n):
        ten=input()
        cu=int(input())
        moi=int(input())
        ds.append(Dien(i+1,ten,cu,moi))
    ds.sort(key=lambda x:x.tong,reverse=True)
    for d in ds:
        print(d)