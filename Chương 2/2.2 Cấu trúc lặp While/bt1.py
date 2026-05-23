# Nhap diem va xep loai hoc sinh trong Python

toan = float(input("Nhap diem Toan: "))
ly = float(input("Nhap diem Ly: "))
hoa = float(input("Nhap diem Hoa: "))

# Tinh diem trung binh
average_score = (toan + ly + hoa) / 3

print("Diem trung binh:", average_score)

# Xep loai hoc luc
if average_score < 5:
    print("Xep loai: Yeu")
elif average_score < 7:
    print("Xep loai: Trung binh")
elif average_score < 9:
    print("Xep loai: Kha")
else:
    print("Xep loai: Gioi")
