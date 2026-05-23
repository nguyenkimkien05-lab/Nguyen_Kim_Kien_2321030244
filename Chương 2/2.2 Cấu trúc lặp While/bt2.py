# Tinh tong cac so chan nhap tu ban phim

total = 0

while True:
    value = int(input("Nhap so: "))

    # Thoat vong lap neu nhap 0
    if value == 0:
        break

    # Cong neu la so chan
    if value % 2 == 0:
        total += value

print("Tong cac so chan la:", total)
