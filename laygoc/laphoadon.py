from datetime import datetime
class hoadon:
    def __init__(self,id,ten,phong,nhan,tra,dv):
        self.id = f"KH{id:02d}"
        self.ten = ten
        self.phong = phong
        self.nhan =datetime.strptime(nhan,"%d/%m/%Y")
        self.tra = datetime.strptime(tra,"%d/%m/%Y")
        self.dv = dv
        self.songayo=(self.tra-self.nhan).days+1
        if self.phong[0:1]=='1':
            self.tien=self.songayo*25+self.dv
        elif self.phong[0:1]=='2':
            self.tien=self.songayo*34+self.dv
        elif self.phong[0:1]=='3':
            self.tien=self.songayo*50+self.dv
        else:
            self.tien=self.songayo*80+self.dv

    def __str__(self):
        return f"{self.id} {self.ten} {self.phong} {self.songayo} {self.tien}"
if __name__=='__main__':
    t = int(input())
    ds=[]
    for i in range(t):
        ten=input().strip()
        phong=input().strip()
        nhan=input().strip()
        tra=input().strip()
        dv=int(input().strip())
        ds.append(hoadon(i+1,ten,phong,nhan,tra,dv))
    ds.sort(key=lambda x:x.tien,reverse=True)
    for d in ds:
        print(d)
