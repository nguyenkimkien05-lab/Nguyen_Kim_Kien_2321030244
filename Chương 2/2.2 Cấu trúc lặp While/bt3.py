# Tim cac uoc so nguyen to cua n

n = int(input("Nhap so n: "))

print("Cac uoc so nguyen to cua n la:")

for i in range(2, n + 1):
    if n % i == 0:
        # kiem tra i co phai so nguyen to khong
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)
