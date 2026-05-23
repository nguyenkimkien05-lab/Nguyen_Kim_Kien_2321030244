# Tao va ghi noi dung vao file
file = open("foo.txt", "w")
file.write("python la mot ngon ngu lap trinh tuyet voi\n")
file.write("Minh cung nghi nhu the!\n")
file.close()

# Mo lai file de kiem tra thuoc tinh (phai dung che do 'r' de khong bi xoa du lieu)
file = open("foo.txt", "r")

print("Ten file la:", file.name)
print("Che do mo file:", file.mode)
print("File da dong chua?", file.closed)

file.close()

print("Sau khi dong, file da dong chua?", file.closed)
