first_number = int(input("Nhap gia tri m: "))
second_number = int(input("Nhap gia tri n: "))

total_value = first_number + second_number

print(f"Tong cua hai so la: {total_value}")

largest_digit = 0

for character in str(total_value):
    digit = int(character)

    if digit > largest_digit:
        largest_digit = digit

print("Chu so lon nhat trong tong:", largest_digit)