def cmp(x):
    a = x[0].split()
    dem = ""
    for i in range(1,len(a) - 1): dem += a[i]
    return (a[-1], a[0], dem)
with open("DIENTHOAI.txt", "w", encoding = "utf-8") as out:
    with open("SOTAY.txt", "r", encoding = "utf-8") as f:
        ngay = ""
        a = []
        for line in f:
            line = line.strip()
            if line.startswith("Ngay"):
                a = sorted(a, key = cmp)
                for ten, sdt in a:
                    out.write(ten + ": " + sdt + " " + ngay.split()[1] + "\n")
                a = []
                ngay = line
            else:
                ten, sdt = "", ""
                if line[1].isdigit():
                    sdt = line
                    a[-1] = (a[-1][0], sdt)
                else:
                    ten = line
                    a.append((ten, ""))
        if a:
            for ten, sdt in a:
                out.write(ten + ": " + sdt + " " + ngay.split()[1] + "\n")