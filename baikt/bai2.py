amount = int(input("Nhap so phan tu: "))

even_total = 0

for index in range(1, amount + 1):
    number = int(input(f"Phan tu thu {index}: "))

    if number % 2 == 0:
        even_total += number

print(f"Tong cac so chan = {even_total}")

condition = even_total < 200 and even_total % 7 == 0

if condition:
    print("Tong hop le theo yeu cau")
else:
    print("Tong khong dat dieu kien")