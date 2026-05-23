so_phan_tu = int(input("Nhap vao n: "))

danh_sach = []

for vi_tri in range(1, so_phan_tu + 1):
    gia_tri = float(input(f"Gia tri thu {vi_tri}: "))
    danh_sach.append(gia_tri)

cac_so_hop_le = []

for item in danh_sach:
    if item > -1000 and item < -10:
        cac_so_hop_le.append(item)

if len(cac_so_hop_le) > 0:
    trung_binh = sum(cac_so_hop_le) / len(cac_so_hop_le)

    print("Gia tri trung binh:", trung_binh)
else:
    print("Khong tim thay phan tu phu hop")