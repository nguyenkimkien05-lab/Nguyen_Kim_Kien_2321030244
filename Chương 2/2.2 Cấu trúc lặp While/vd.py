# Tinh tong tu 1 den n trong Python

n = int(input("Nhap n: "))

total = 0
i = 1

while i <= n:
    total += i   # cong don i vao tong
    i += 1       # tang bien dem

print("Tong tu 1 den n la:", total)
