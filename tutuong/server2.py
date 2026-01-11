from datetime import datetime

# Class GameThu
class GameThu:
    def __init__(self, id, name, vao, ra):
        self.id = f"TS{id:02d}"
        self.name = name
        self.vao = datetime.strptime(vao, "%H%M")
        self.ra = datetime.strptime(ra, "%H%M")
        # Tính khoảng thời gian chơi
        self.delta = self.ra - self.vao
        self.gio = self.delta.seconds // 3600
        self.phut = (self.delta.seconds % 3600) // 60

    def __str__(self):
        return f"{self.id} {self.name} {self.gio} gio {self.phut} phut"


# Phần main
if __name__ == '__main__':
    t = int(input("Nhập số game thủ: "))
    ds = []

    for i in range(t):
        print(f"Nhập thông tin game thủ thứ {i+1}:")
        name = input("Tên: ")
        vao = input("Giờ vào (HHMM): ")
        ra = input("Giờ ra (HHMM): ")
        ds.append(GameThu(i+1, name, vao, ra))

    # Sắp xếp theo thời gian chơi giảm dần
    ds.sort(key=lambda x: x.delta.total_seconds(), reverse=True)

    # In ra màn hình
    print("\nDanh sách sắp xếp theo thời gian chơi:")
    for g in ds:
        print(g)

    # Ghi vào file ketqua.txt
    with open("ketqua.txt", "w") as f:
        for g in ds:
            f.write(str(g) + "\n")

    print("\nĐã ghi kết quả vào file ketqua.txt")
