# Dinh nghia lop Circle trong Python

class Circle:
    # Nhap ban kinh
    def input_radius(self):
        self.radius = float(input("Nhap ban kinh: "))

    # Tinh dien tich hinh tron
    def area(self):
        return self.radius * self.radius * 3.141592

# Tao doi tuong va thuc thi chuong trinh
c = Circle()
c.input_radius()

print("Dien tich hinh tron la:", c.area())
