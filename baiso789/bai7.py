def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor <= int(num ** 0.5):
        if num % divisor == 0:
            return False
        divisor += 1

    return True


amount = int(input("Nhap vao so luong phan tu: "))

prime_sum = 0

for position in range(1, amount + 1):
    value = int(input(f"Nhap gia tri thu {position}: "))

    if is_prime(value):
        prime_sum += value


print("Tong cac so nguyen to:", prime_sum)

if prime_sum > 50:
    if prime_sum % 2 == 1:
        print("Tong vua la so le vua lon hon 50")
    else:
        print("Tong lon hon 50 nhung khong phai so le")
else:
    print("Tong khong thoa dieu kien")