import matplotlib.pyplot as plt
import numpy as np

# ==================== CAU HINH ====================
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ==================== DU LIEU ====================
workloads = ['Random', 'Sequential', 'Locality', 'Write-Heavy']

# WRITE-THROUGH
wt_hit_rate = [27.08, 0.00, 63.77, 52.63]
wt_miss_rate = [72.92, 100.00, 36.23, 47.37]
wt_hdd_write = [52, 37, 31, 81]
wt_total_time = [811.70, 1281.40, 520.60, 899.20]

# WRITE-BACK
wb_hit_rate = [27.08, 0.00, 63.77, 52.63]
wb_miss_rate = [72.92, 100.00, 36.23, 47.37]
wb_hdd_write = [44, 37, 23, 32]
wb_total_time = [731.70, 1281.40, 440.60, 409.20]

# Tinh toan
total_wt_hdd_write = sum(wt_hdd_write)
total_wb_hdd_write = sum(wb_hdd_write)
avg_wt_time = sum(wt_total_time)/len(wt_total_time)
avg_wb_time = sum(wb_total_time)/len(wb_total_time)

# ==================== VE BIEU DO ====================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KET QUA & SO SANH\nWRITE-THROUGH vs WRITE-BACK',
             fontsize=14, fontweight='bold')

# ========== 5.2a: HIT/MISS RATE ==========
ax1 = axes[0, 0]
x = np.arange(len(workloads))
width = 0.35

bars1 = ax1.bar(x - width/2, wt_hit_rate, width, label='Hit Rate', color='#27ae60')
bars2 = ax1.bar(x + width/2, wt_miss_rate, width, label='Miss Rate', color='#e74c3c')

ax1.set_ylabel('Ty le (%)')
ax1.set_title('5.2a. Cache Hit/Miss Rate')
ax1.set_xticks(x)
ax1.set_xticklabels(workloads)
ax1.legend()
ax1.set_ylim(0, 120)

for bar in bars1:
    h = bar.get_height()
    if h > 0:
        ax1.text(bar.get_x() + bar.get_width()/2, h + 2, f'{h:.1f}%', ha='center', fontsize=8)
for bar in bars2:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, h + 2, f'{h:.1f}%', ha='center', fontsize=8)

# ========== 5.2b: HDD WRITES ==========
ax2 = axes[0, 1]

bars3 = ax2.bar(x - width/2, wt_hdd_write, width, label='Write-through', color='#3498db')
bars4 = ax2.bar(x + width/2, wb_hdd_write, width, label='Write-back', color='#e74c3c')

ax2.set_ylabel('So lan ghi HDD')
ax2.set_title('5.2b. So sanh HDD Writes')
ax2.set_xticks(x)
ax2.set_xticklabels(workloads)
ax2.legend()
ax2.set_ylim(0, 100)

for bar in bars3:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h + 1, f'{h:.0f}', ha='center', fontsize=9, fontweight='bold')
for bar in bars4:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h + 1, f'{h:.0f}', ha='center', fontsize=9, fontweight='bold')

# ========== 5.2c: THOI GIAN (LINE CHART) ==========
ax3 = axes[1, 0]

ax3.plot(workloads, wt_total_time, marker='o', linewidth=2, markersize=8,
         label='Write-through', color='#3498db')
ax3.plot(workloads, wb_total_time, marker='s', linewidth=2, markersize=8,
         label='Write-back', color='#e74c3c')

ax3.set_ylabel('Thoi gian (ms)')
ax3.set_xlabel('Workload')
ax3.set_title('5.2c. So sanh Toc do xu ly')
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.fill_between(workloads, wt_total_time, wb_total_time, alpha=0.2, color='green')

# Chi hien thi gia tri cua Write-through (phia tren)
for i, wt in enumerate(wt_total_time):
    ax3.text(i, wt + 40, f'{wt:.0f}', ha='center', fontsize=8, color='#3498db')

# Chi hien thi gia tri cua Write-back (phia duoi)
for i, wb in enumerate(wb_total_time):
    ax3.text(i, wb - 60, f'{wb:.0f}', ha='center', fontsize=8, color='#e74c3c')

# ========== 5.1 & 5.3: BANG + NHAN XET ==========
ax4 = axes[1, 1]
ax4.axis('off')

# Tao bang
col_labels = ['Chi so', 'Write-through', 'Write-back', 'Giam']
table_vals = [
    ['Tong HDD Writes', '201', '136', '32.3%'],
    ['Thoi gian TB (ms)', '878.2', '715.7', '18.5%'],
]

table = ax4.table(
    cellText=table_vals,
    colLabels=col_labels,
    loc='upper center',
    cellLoc='center',
    colWidths=[0.3, 0.23, 0.23, 0.18]
)
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)

# To mau header
for i in range(4):
    table[(0, i)].set_facecolor('#34495e')
    table[(0, i)].set_text_props(color='white', fontweight='bold')

# Nhan xet
nhan_xet = """
5.3. NHAN XET:

* Write-back NHANH HON:
  - Giam 32.3% so lan ghi HDD
  - Giam 18.5% thoi gian xu ly
  - Write-Heavy cai thien 54.5%

* Write-through AN TOAN HON:
  - Du lieu dong bo ngay voi HDD
  - Khong mat du lieu khi mat dien

* KET LUAN:
  - Can toc do -> Write-back
  - Can an toan -> Write-through
"""

ax4.text(0.05, 0.55, nhan_xet, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(facecolor='#ecf0f1', edgecolor='gray', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.savefig('ketqua_sosanh.png', dpi=150, bbox_inches='tight')
plt.show()

print("Da luu: nguoi5_ketqua_sosanh.png")