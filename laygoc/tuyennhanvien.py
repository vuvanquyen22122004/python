class nhanvien:
    def __init__(self,id,name,diem1,diem2):
        self.id=f"TS{id:02d}"
        self.name = name
        if diem1<=10:
            self.diem1=diem1
        else:
            self.diem1=diem1/10
        if diem2<=10:
            self.diem2=diem2
        else:
            self.diem2=diem2/10
        self.dtb=(self.diem1+self.diem2)/2
        if self.dtb<5:
            self.ketqua="TRUOT"
        elif self.dtb>=5 and self.dtb<8:
            self.ketqua="CAN NHAC"
        elif self.dtb>=8 and self.dtb<=9.5:
            self.ketqua="DAT"
        else:
            self.ketqua="XUAT SAC"
    def __str__(self):
        return f"{self.id} {self.name} {round(self.dtb,2):.2f} {self.ketqua}"
if __name__=="__main__":
    t=int(input())
    ds=[]
    for i in range(t):
        name=input()
        diem1=float(input())
        diem2=float(input())
        ds.append(nhanvien(i+1,name,diem1,diem2))
    ds.sort(key=lambda x : x.dtb , reverse=True)
    for j in ds:
        print(j)