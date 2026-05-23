# Nhap va tinh tong cac phan tu trong danh sach

numbers = []
total = 0

n = int(input("Nhap so luong phan tu: "))

# Nhap du lieu vao danh sach
for index in range(n):
    value = int(input(f"Nhap phan tu thu {index + 1}: "))
    numbers.append(value)

# Tinh tong cac phan tu
for item in numbers:
    total += item

print("Tong cua day so la:", total)
