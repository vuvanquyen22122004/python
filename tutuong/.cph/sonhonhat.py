from datetime import datetime;
class thoigian:
    def __init__(self, bdau, kthuc, mua):
        time1 = datetime.strptime(bdau, "%H:%M")
        time2 = datetime.strptime(kthuc, "%H:%M")
        self.luongmua = (time2 - time1).seconds / 60
        self.mua = mua
class Tram:
    def __init__(self, ten):
        self.ten = ten
        self.ds = []
    def add(self, tg):
        self.ds.append(tg)
    def muatb(self):
        s = 0
        ss = 0
        for x in self.ds:
            s += x.luongmua
            ss += x.mua
        print(f"{ss / s * 60:.2f}")
t = int(input())
tram = {}
a = []
for _ in range(t):
    ten = input().strip()
    bdau = input().strip()
    kthuc = input().strip()
    mua = input().strip()
    if ten not in tram:
        tram[ten] = Tram(ten)
        a.append(ten)
    tgian = thoigian(bdau, kthuc, int(mua))
    tram[ten].add(tgian)
for i, x in enumerate(a):
    print(f"T{i + 1:02d} {x}", end = ' ')
    tram[x].muatb()