from datetime import datetime

class KhachHang:
    def __init__(self, ma, ten, phong, nhan, tra, dv):
        self.ma = f"KH{ma:02d}"
        self.ten = ten.strip()
        self.phong = phong.strip()
        self.nhan = datetime.strptime(nhan.strip(), "%d/%m/%Y")
        self.tra = datetime.strptime(tra.strip(), "%d/%m/%Y")
        self.dv = int(dv)
        self.so_ngay = (self.tra - self.nhan).days + 1
        self.tien = self.tinh_tien()

    def tinh_tien(self):
        tang = int(self.phong[0])
        if tang == 1:
            don_gia = 25
        elif tang == 2:
            don_gia = 34
        elif tang == 3:
            don_gia = 50
        else:
            don_gia = 80
        return self.so_ngay * don_gia + self.dv

    def __str__(self):
        return f"{self.ma} {self.ten} {self.phong} {self.so_ngay} {self.tien}"

n = int(input())
ds = []
for i in range(1, n + 1):
    ten = input().strip()
    phong = input().strip()
    nhan = input().strip()
    tra = input().strip()
    dv = input().strip()
    ds.append(KhachHang(i, ten, phong, nhan, tra, dv))

ds.sort(key=lambda x: x.tien,reverse=True)

for kh in ds:
    print(kh)
