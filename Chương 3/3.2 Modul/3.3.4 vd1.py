# Doc file va tinh tong cac so trong Python

file = open("dulieu.txt", "r")

# Doc toan bo noi dung file
content = file.read()

# Xu ly chuoi
content = content.strip()
numbers_str = content.split()

total = 0

print("Day so doc duoc:", numbers_str)

# Tinh tong cac so
for item in numbers_str:
    if item != "":
        total += int(item)

print("Tong cua day so la:", total)

file.close()
