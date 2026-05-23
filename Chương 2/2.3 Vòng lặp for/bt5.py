# Kiem tra so hoan hao trong Python

number = int(input("Nhap n: "))
total = 0

# Tim tong cac uoc thuc su cua n
for i in range(1, number):
    if number % i == 0:
        total += i

# Kiem tra dieu kien so hoan hao
if total == number:
    print(number, "la so hoan hao")
else:
    print(number, "khong phai so hoan hao")
