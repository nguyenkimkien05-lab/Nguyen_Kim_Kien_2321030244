number_a = int(input("Nhap so a: "))
number_b = int(input("Nhap so b: "))

smallest_digit = 9

for digit in str(number_b):
    value = int(digit)

    if value < smallest_digit:
        smallest_digit = value

print("Chu so nho nhat cua b la:", smallest_digit)

if smallest_digit == 0:
    print("Khong the kiem tra chia het cho 0")
elif number_a % smallest_digit == 0:
    print("a co chia het cho chu so nho nhat cua b")
else:
    print("a khong chia het cho chu so nho nhat cua b")