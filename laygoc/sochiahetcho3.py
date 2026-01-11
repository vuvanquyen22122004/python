class Chuyen:
    def __init__(self,ma,ten,lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.cc=10
    def tinhDiem(self,s):
        for i in range(len(s)):
            if s[i]=='m': self.cc-=1
            elif s[i]=='v': self.cc-=2
            else : self.cc-=0
        if self.cc<0:
            self.cc=0
    def __str__(self):
        if self.cc==0:
            return f"{self.ma} {self.ten} {self.lop} {self.cc} KDDK"
        else:
            return f"{self.ma} {self.ten} {self.lop} {self.cc}"
def getMa(ds,ma):
    for i in ds:
        if i.ma==ma:
            return i
    return None
if __name__=='__main__':
    n=int(input())
    ds=[]
    for i in range(n):
        ma=input()
        ten=input()
        lop=input()
        ds.append(Chuyen(ma,ten,lop))
    for i in range(n):
        line=input().split()
        l=line[0]
        s=line[1]
        sv=getMa(ds,l)
        sv.tinhDiem(s)
    for i in ds:
        print(i)