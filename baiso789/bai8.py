a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
c = int(input("Nhap so thu ba: "))

ket_qua = a * b * c

print(f"Tich cua ba so la: {ket_qua}")

chuoi_so = str(ket_qua)

tong_chu_so = 0

for _ in chuoi_so:
    tong_chu_so += 1

chu_so_max = 0

for ky_tu in chuoi_so:
    if int(ky_tu) > chu_so_max:
        chu_so_max = int(ky_tu)

print("So chu so trong tich:", tong_chu_so)
print("Chu so lon nhat cua tich:", chu_so_max)