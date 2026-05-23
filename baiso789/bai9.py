num1 = int(input("So thu nhat: "))
num2 = int(input("So thu hai: "))
num3 = int(input("So thu ba: "))

result = num1 + num2 + num3

print(f"Tong cua ba so = {result}")

count_even = 0

number_string = str(result)

for digit in number_string:
    value = int(digit)

    if value % 2 == 0:
        count_even += 1

print("Co", count_even, "chu so chan trong tong")