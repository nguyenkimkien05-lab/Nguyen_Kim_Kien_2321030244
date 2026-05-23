# Nhap du lieu vao danh sach va ghi ra file trong Python

numbers = []

n = int(input("Nhap so phan tu: "))

# Nhap du lieu vao list
for i in range(n):
    value = int(input(f"Nhap phan tu thu {i+1}: "))
    numbers.append(value)

# Mo file de ghi du lieu
file = open("dulieu.txt", "w")

# Ghi tung phan tu vao file
for item in numbers:
    file.write(str(item) + " ")

# Dong file
file.close()
