class danhsachphim:
    def __init__(self, id, ns, ten, tap, matl):
        self.id = f"P{id:03d}"
        self.ns = ns
        self.ten = ten
        self.matl = matl
        self.tap = tap
        self.tl = ""
        self.ngay, self.thang, self.nam = map(int, self.ns.split("/"))

    def __str__(self):
        return f"{self.id} {self.tl} {self.ns} {self.ten} {self.tap}"

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = {}
    ds = []

    for i in range(n):
        a[f"TL{i + 1:03d}"] = input()

    for i in range(m):
        matl = input()
        ns = input()
        ten = input()
        tap = int(input())

        ds.append(danhsachphim(i + 1, ns, ten, tap, matl))
        ds[i].tl = a[matl]

    ds.sort(key=lambda x: (x.nam, x.thang, x.ngay, x.ten, -x.tap))

    for d in ds:
        print(d)
