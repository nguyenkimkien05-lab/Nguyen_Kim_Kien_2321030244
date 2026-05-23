# Chuyen chuoi so thanh danh sach so nguyen

data = "5 10 15 20 25"

# Tach chuoi thanh cac phan tu rieng biet
items = data.split()

# Chuyen tung phan tu sang kieu int
numbers = [int(value) for value in items]

# Hien thi ket qua
print("Danh sach sau khi chuyen doi:", numbers)
