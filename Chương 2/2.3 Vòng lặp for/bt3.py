# Nhap va xuat ma tran trong Python

rows = int(input("Nhap so hang m: "))
cols = int(input("Nhap so cot n: "))

matrix = []

# Nhap du lieu cho ma tran
for row in range(rows):
    current_row = []

    for col in range(cols):
        value = float(input(f"Nhap phan tu a[{row+1}][{col+1}]: "))
        current_row.append(value)

    matrix.append(current_row)

print("Ma tran vua nhap la:")

# In ma tran ra man hinh
for row in matrix:
    for value in row:
        print(f"{value:8.2f}", end=" ")
    print()
