# Nhap va tinh trung binh cac so thoa man dieu kien

n = int(input("Nhap so phan tu n: "))

while n <= 0 or n >= 100:
    n = int(input("Nhap lai n (0 < n < 100): "))

total = 0
count = 0

# Nhap cac so thuc
for i in range(n):
    value = float(input(f"Nhap x[{i+1}]: "))

    # Loc cac so am trong khoang (-1000, -10)
    if -1000 < value < -10:
        total += value
        count += 1

# Tinh trung binh cong
if count > 0:
    average = total / count
    print("Trung binh cong cac so thoa man:", average)
else:
    print("Khong co so nao thoa man dieu kien.")
