class Math:
    def __init__(self, a, b):

        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f'Addition: {self.a} + {self.b} = {result}')

    def multiplication(self):
        result = self.a * self.b
        print(f'Multiplication: {self.a} * {self.b} = {result}')

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f'Division: {self.a} / {self.b} = {result}')
        else:
            print('Division by zero is not possible')

    def subtraction(self):
        result = self.a - self.b
        print(f'Subtraction: {self.a} - {self.b} = {result}')


math_action = Math(10, 2)

math_action.addition()
math_action.multiplication()
math_action.division()
math_action.subtraction()