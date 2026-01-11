class tinhluong:
    def __init__(self,mnv,tennv,ngaycong,luongcb):
        self.mnv=mnv
        self.tennv=tennv
        self.ngaycong=ngaycong
        self.luongcb=luongcb
        self.tenpb=""
    def check(self):
        if self.mnv[0:1]=="A":
            if int(self.mnv[1:3])<=3:
                return 10
            elif int(self.mnv[1:3])<=8:
                return 12
            elif int(self.mnv[1:3])<=15:
                return 14
            else:
                return 20
        elif self.mnv[0:1]=="B":
            if int(self.mnv[1:3])<=3:
                return 10
            elif int(self.mnv[1:3])<=8:
                return 11
            elif int(self.mnv[1:3])<=15:
                return 13
            else:
                return 16
        elif self.mnv[0:1]=="C":
            if int(self.mnv[1:3])<=3:
                return 9
            elif int(self.mnv[1:3])<=8:
                return 10
            elif int(self.mnv[1:3])<=15:
                return 12
            else:
                return 14
        elif self.mnv[0:1]=="D":
            if int(self.mnv[1:3])<=3:
                return 8
            elif int(self.mnv[1:3])<=8:
                return 9
            elif int(self.mnv[1:3])<=15:
                return 11
            else:
                return 13
    def tinhtien(self):
        return self.check()*self.ngaycong*self.luongcb
    def __str__(self):
        return f"{self.mnv} {self.tennv} {self.tenpb} {self.tinhtien()}000"
if __name__=='__main__':
    t= int(input())
    a={}
    ds=[]
    for i in range(t):
        f=list(input().split())
        xau=""
        xau=" ".join(f[1:])
        a[f[0]]=xau
    for j in range(int(input())):
        manv=input()
        tennv=input()
        luongcb=int(input())
        ngaycong=int(input())
        obj = tinhluong(manv,tennv,ngaycong,luongcb)
        obj.tenpb=a[manv[3:5]]
        ds.append(obj)
    for d in ds:
        print(d)





