
import sqlite3
import pandas as pd

# =============================================================================
# BƯỚC 1: TẠO DATABASE VÀ 2 BẢNG
# =============================================================================
print("BƯỚC 1: Tạo database và 2 bảng từ CSV...")

conn = sqlite3.connect("diem_lop.db")

# Đọc CSV
df_bangdiem = pd.read_csv("bangdiem.csv", encoding="latin-1")
df_thangdiem = pd.read_csv("thangdiem.csv", encoding="latin-1")

# Chuẩn hóa tên cột bangdiem
df_bangdiem.columns = df_bangdiem.columns.str.strip()
column_map = {}
for col in df_bangdiem.columns:
    col_lower = col.lower()
    if 'code' in col_lower:
        column_map[col] = 'MaSV'
    elif 'name' in col_lower:
        column_map[col] = 'HoTen'
    elif 'thuy' in col_lower or 'tr\x8d' in col or 'trinh' in col_lower:
        column_map[col] = 'DiemThuyetTrinh_Raw'
    elif 't?p' in col_lower or 'tap' in col_lower or 'l?n' in col_lower or 'lon' in col_lower:
        column_map[col] = 'DiemBaiTapLon_Raw'

df_bangdiem = df_bangdiem.rename(columns=column_map)

# Chuẩn hóa tên cột thangdiem
df_thangdiem.columns = ['Alphabet', 'DiemSo']

# Lưu vào database
df_bangdiem.to_sql("bangdiem", conn, if_exists="replace", index=False)
df_thangdiem.to_sql("thangdiem", conn, if_exists="replace", index=False)

print(f"✓ Bảng 1 (bangdiem): {len(df_bangdiem)} sinh viên")
print(f"✓ Bảng 2 (thangdiem): {len(df_thangdiem)} mức điểm\n")

# =============================================================================
# BƯỚC 2: TẠO BẢNG 3 - ĐIỂM TRUNG BÌNH
# =============================================================================
print("BƯỚC 2: Tạo bảng 3 - Điểm trung bình...")

# Tạo dict ánh xạ điểm
grade_map = dict(zip(df_thangdiem['Alphabet'], df_thangdiem['DiemSo']))

# Hàm chuyển đổi sang thang 10
def convert_to_10(val):
    if pd.isna(val):
        return None
    val_str = str(val).strip()
    try:
        num = float(val_str)
        return round(num / 10, 1) if num > 10 else round(num, 1)
    except:
        return grade_map.get(val_str, None)

# Ánh xạ điểm
df_bangdiem['DiemThuyetTrinh'] = df_bangdiem['DiemThuyetTrinh_Raw'].apply(convert_to_10)
df_bangdiem['DiemBaiTapLon'] = df_bangdiem['DiemBaiTapLon_Raw'].apply(convert_to_10)

# Tính điểm TB (20% thuyết trình + 80% bài tập lớn)
df_bangdiem['DiemTB'] = (
    df_bangdiem['DiemThuyetTrinh'] * 0.2 +
    df_bangdiem['DiemBaiTapLon'] * 0.8
).round(1)

# Tạo bảng 3
df_diemtrungbinh = df_bangdiem[['MaSV', 'HoTen', 'DiemThuyetTrinh', 'DiemBaiTapLon', 'DiemTB']].copy()
df_diemtrungbinh.to_sql("diemtrungbinh", conn, if_exists="replace", index=False)

print(f"✓ Bảng 3 (diemtrungbinh): {len(df_diemtrungbinh)} sinh viên\n")

# =============================================================================
# BƯỚC 3: NỐI BẢNG 1 VÀ BẢNG 3 - GIỮ NGUYÊN ĐIỂM CHỮ
# =============================================================================
print("BƯỚC 3: Nối bảng 1 và bảng 3...\n")

df_joined = pd.read_sql("""
    SELECT 
        b.MaSV,
        b.HoTen,
        b.DiemThuyetTrinh_Raw AS DiemThuyetTrinh_Chu,
        b.DiemBaiTapLon_Raw AS DiemBaiTapLon_Chu,
        d.DiemThuyetTrinh AS DiemThuyetTrinh_So,
        d.DiemBaiTapLon AS DiemBaiTapLon_So,
        d.DiemTB
    FROM bangdiem b
    LEFT JOIN diemtrungbinh d ON b.MaSV = d.MaSV
    ORDER BY d.DiemTB DESC
""", conn)

print("="*110)
print("KẾT QUẢ NỐI BẢNG 1 (bangdiem) VÀ BẢNG 3 (diemtrungbinh)")
print("="*110)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
print(df_joined.to_string(index=False))
print("="*110)

# =============================================================================
# BƯỚC 4: XUẤT FILE XẾP HẠNG THEO ĐIỂM
# =============================================================================
print("\nBƯỚC 4: Xuất danh sách xếp hạng theo điểm...")
df_joined.to_csv("danh_sach_xep_hang_theo_diem.csv", index=False, encoding="utf-8-sig")
print("✓ File: danh_sach_xep_hang_theo_diem.csv\n")

# =============================================================================
# BƯỚC 5: PHÂN LOẠI THEO HẠNG
# =============================================================================
print("BƯỚC 5: Phân loại và thống kê theo hạng...\n")

def classify_rank(tb):
    if pd.isna(tb):
        return "Chưa có điểm"
    elif tb >= 8:
        return "Giỏi"
    elif tb >= 6.5:
        return "Khá"
    elif tb >= 5.0:
        return "Trung bình"
    else:
        return "Trượt"

df_joined['XepHang'] = df_joined['DiemTB'].apply(classify_rank)

# Sắp xếp theo hạng
rank_order = ['Giỏi', 'Khá', 'Trung bình', 'Trượt', 'Chưa có điểm']
df_joined['RankOrder'] = df_joined['XepHang'].apply(lambda x: rank_order.index(x) if x in rank_order else 999)
df_sorted = df_joined.sort_values(['RankOrder', 'DiemTB'], ascending=[True, False]).drop('RankOrder', axis=1)

# In theo từng hạng
print("="*110)
print("DANH SÁCH SINH VIÊN THEO HẠNG")
print("="*110)
for rank in rank_order:
    df_rank = df_sorted[df_sorted['XepHang'] == rank]
    if len(df_rank) > 0:
        print(f"\n>>> {rank.upper()} ({len(df_rank)} sinh viên)")
        print("-"*110)
        print(df_rank[['MaSV', 'HoTen', 'DiemThuyetTrinh_Chu', 'DiemBaiTapLon_Chu',
                       'DiemThuyetTrinh_So', 'DiemBaiTapLon_So', 'DiemTB']].to_string(index=False))

print("\n" + "="*110)

# Xuất file
df_sorted.to_csv("danh_sach_theo_hang.csv", index=False, encoding="utf-8-sig")
print("\n✓ File: danh_sach_theo_hang.csv")

# Thống kê
print("\n" + "="*90)
print("THỐNG KÊ SỐ SINH VIÊN MỖI HẠNG")
print("="*90)
stats = df_joined['XepHang'].value_counts()
total = len(df_joined)
print(f"\n{'Hạng':<20} {'Số lượng':>10} {'Tỷ lệ':>10}")
print("-"*42)
for rank in rank_order:
    if rank in stats:
        count = stats[rank]
        percent = (count / total) * 100
        print(f"{rank:<20} {count:>10} {percent:>9.1f}%")
print("-"*42)
print(f"{'TỔNG':<20} {total:>10} {100:>9.1f}%")

# Thống kê điểm
df_co_diem = df_joined.dropna(subset=['DiemTB'])
if len(df_co_diem) > 0:
    print("\n" + "="*90)
    print("THỐNG KÊ ĐIỂM SỐ")
    print("="*90)
    print(f"Điểm cao nhất      : {df_co_diem['DiemTB'].max():.1f}")
    print(f"Điểm thấp nhất     : {df_co_diem['DiemTB'].min():.1f}")
    print(f"Điểm trung bình    : {df_co_diem['DiemTB'].mean():.1f}")
    print(f"Số SV có điểm      : {len(df_co_diem)}/{total}")

conn.close()
print("\n" + "="*90)
print("HOÀN TẤT!")
print("="*90)
