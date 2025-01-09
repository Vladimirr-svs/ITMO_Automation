class Math:
    def __init__(self, a, b):

        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
        else:
            print("Деление на ноль невозможно")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")


math_action = Math(10, 2)

math_action.addition()        # Сложение
math_action.multiplication()  # Умножение
math_action.division()        # Деление
math_action.subtraction()     # Вычитание