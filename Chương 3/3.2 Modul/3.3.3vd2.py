# Nhap va ghi ma tran vao file trong Python

rows = int(input("Nhap so hang: "))
cols = int(input("Nhap so cot: "))

matrix = []

# Nhap du lieu ma tran
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Nhap a[{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

# Ghi ma tran ra file
file = open("matran.txt", "w")

for row in matrix:
    for value in row:
        file.write(str(value) + " ")
    file.write("\n")

file.close()

print("Da luu ma tran vao file matran.txt")
