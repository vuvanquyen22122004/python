cnt = 1
class Student:
    def __init__(self, ten, a):
        global cnt
        self.__ten = ten
        s = sum(x for x in a)
        s += a[0] + a[1]
        self.__diem = s/ 10/ 1.2
        self.__ma = f"HS{cnt:02d}"
        cnt += 1
        if self.__diem >= 9: self.__xephang = "XUAT SAC"
        elif self.__diem >= 8: self.__xephang = "GIOI"
        elif self.__diem >= 7: self.__xephang = "KHA"
        elif self.__diem >= 5: self.__xephang = "TB"
        else: self.__xephang = "YEU"
    def getdiem(self): return self.__diem
    def getma(self): return self.__ma
    def show(self):
        print(f"{self.__ma} {self.__ten} {self.__diem:.1f} {self.__xephang}")

n = int(input())
a = []
for _ in range(n):
    ten = input()
    diem = list(map(float, input().split()))
    st = Student(ten, diem)
    a.append(st)
a = sorted(a, key = lambda x : (-x.getdiem(), x.getma()))
for x in a:
    x.show()