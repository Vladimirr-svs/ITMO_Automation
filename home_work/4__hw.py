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

print(f'Rectangle 1: width={rectangle1.width}, height={rectangle1.height}')
print(f'Area : {rectangle1.area()}, Perimeter: {rectangle1.perimeter()}')

print(f'Rectangle 2: width={rectangle2.width}, height={rectangle2.height}')
print(f'Area: {rectangle2.area()}, Perimeter: {rectangle2.perimeter()}')

print(f'Rectangle 3: width={rectangle3.width}, height={rectangle3.height}')
print(f'Area: {rectangle3.area()}, Perimeter: {rectangle3.perimeter()}')