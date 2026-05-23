import math

# Tinh dien tich hinh tron
def circle_area(radius):
    return math.pi * radius * radius

# Tinh dien tich hinh chu nhat
def rectangle_area(length, width):
    return length * width

# Tinh dien tich hinh vuong
def square_area(side):
    return side ** 2

# Tinh chu vi hinh chu nhat
def rectangle_perimeter(length, width):
    return (length + width) * 2
