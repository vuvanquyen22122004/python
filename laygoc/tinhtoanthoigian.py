from datetime import datetime
class gamethu:
    def __init__(self,id,name,vao,ra):
        self.id=id
        self.name=name
        self.vao=datetime.strptime(vao,"%H:%M")
        self.ra=datetime.strptime(ra,"%H:%M")

        self.delta=self.ra-self.vao
        self.gio=self.delta.seconds //3600
        self.phut=(self.delta.seconds %3600)//60
    def __str__(self):
        return f"{self.id} {self.name} {self.gio} gio {self.phut} phut"
if __name__=='__main__':
    t = int(input())
    ds=[]
    for i in range(t):
        id=input()
        name=input()
        vao=input()
        ra=input()
        ds.append(gamethu(id,name,vao,ra))
    ds.sort(key=lambda x: (x.gio,x.phut), reverse=True)
    for d in ds:
        print(d)



