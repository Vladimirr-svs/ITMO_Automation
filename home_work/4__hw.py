class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(10, 2)

print(f'Прямоугольник 1: ширина={rectangle1.width}, высота={rectangle1.height}')
print(f'Площадь: {rectangle1.area()}, Периметр: {rectangle1.perimeter()}')

print(f'Прямоугольник 2: ширина={rectangle2.width}, высота={rectangle2.height}')
print(f'Площадь: {rectangle2.area()}, Периметр: {rectangle2.perimeter()}')

print(f'Прямоугольник 3: ширина={rectangle3.width}, высота={rectangle3.height}')
print(f'Площадь: {rectangle3.area()}, Периметр: {rectangle3.perimeter()}')