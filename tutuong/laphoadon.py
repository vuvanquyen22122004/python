class HoaDon:
    def __init__(self,id,ten,cu,moi):
        self.id=f"KH{id:02d}"
        self.ten=ten
        self.cu=cu
        self.moi=moi
        self.sokhoi=0
        self.tong=0
    def tinhkhoi(self):
        self.sokhoi=self.moi-self.cu
    def thanhtien(self):
        if self.sokhoi <= 50:
            total = self.sokhoi * 100
            phu_phi = 0.02
        elif self.sokhoi <= 100:
            total = 50 * 100 + (self.sokhoi - 50) * 150
            phu_phi = 0.03
        else:
            total = 50 * 100 + 50 * 150 + (self.sokhoi - 100) * 200
            phu_phi = 0.05

        self.tong = total + total * phu_phi
    def __str__(self):
        return f"{self.id} {self.ten} {round(self.tong)}"
if __name__=="__main__":
    t=int(input())
    ds=[]
    for i in range(t):
        ten=input()
        cu=int(input())
        moi=int(input())
        hd=HoaDon(i+1,ten,cu,moi)
        hd.tinhkhoi()
        hd.thanhtien()
        ds.append(hd)
    ds.sort(key=lambda x:x.tong,reverse=True)
    for hd in ds:
        print(hd)
