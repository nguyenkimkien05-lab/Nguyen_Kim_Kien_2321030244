# Dinh nghia lop Circle trong Python

class Circle:
    pi = 3.141592

    # Ham khoi tao
    def __init__(self, radius=1):
        self.radius = radius

    # Tinh dien tich hinh tron
    def area(self):
        return self.radius * self.radius * Circle.pi

# Tao doi tuong voi ban kinh = 5
c = Circle(5)

print("Dien tich hinh tron la:", c.area())
