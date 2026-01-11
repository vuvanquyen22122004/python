class NhanVien:
    def __init__(self,ma,ten,diem1,diem2):
        self.ma=f"TS0{str(i+1)}"
        self.ten=ten
        if diem1<=10: self.diem1=diem1
        else: self.diem1=diem1/10
        if diem2<=10: self.diem2=diem2
        else: self.diem2=diem2/10
        self.diemtb=0
        self.xepLoai=""
    def tinhDiemtb(self):
        self.diemtb=(self.diem1+self.diem2)/2
    def ketQua(self):
        if self.diemtb>=9.5: self.xepLoai="XUAT SAC"
        elif self.diemtb>=8: self.xepLoai="DAT"
        elif self.diemtb>=5: self.xepLoai="CAN NHAC"
        else: self.xepLoai="TRUOT"
    def __str__(self):
        return self.ma+" "+self.ten+" "+f"{round(self.diemtb,2):.2f}"+" "+self.xepLoai
if __name__=="__main__":
    t=int(input())
    ds=[]
    for i in range(t):
        ten=input()
        diem1=float(input())
        diem2=float(input())
        nv=NhanVien(i,ten,diem1,diem2)
        nv.tinhDiemtb()
        nv.ketQua()
        ds.append(nv)
    ds.sort(key=lambda x: x.diemtb, reverse=True)
    for d in ds:
        print(d)