# Tinh giai thua trong Python

def factorial(num):
    result = 1

    # Nhan cac so tu 1 den num
    for i in range(1, num + 1):
        result *= i

    return result

# --- Chuong trinh chinh ---

n = int(input("Nhap n: "))

ket_qua = factorial(n)

print("Giai thua cua", n, "la:", ket_qua)
