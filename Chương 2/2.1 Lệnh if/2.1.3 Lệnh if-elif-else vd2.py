# Giai va bien luan phuong trinh bac nhat ax + b = 0

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

if a == 0:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b / a
    print("Nghiem duy nhat x =", x)
