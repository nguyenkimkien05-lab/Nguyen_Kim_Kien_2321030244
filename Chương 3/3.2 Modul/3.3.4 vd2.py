# Doc ma tran tu file va tinh tong trong Python

file = open("matran.txt", "r")

# Doc tung dong va tach thanh cac so
matrix = [line.split() for line in file]

print("Ma tran doc duoc tu file:", matrix)

total = 0

# Duyet tung phan tu trong ma tran
for row in matrix:
    for value in row:
        total += float(value)

print("Tong cua ma tran la:", total)

file.close()
