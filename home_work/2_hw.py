

def task_1():
    a: int = 10
    b: float = 52.7
    c: str = "Home Work"
    d: list = [1, 2, 3, 4, 5]
    e: bool = False
    return type(a), type(b), type(c), type(d), type(e)

result = task_1()
print(result)


def task_2():
    a = [1, 2, 3, 5, 8, 13, 21] #Последовательность Фибоначчи
    print("a[0:3] = ", a[0:3])
(task_2())


def task_3(number: int):
    return number ** 2
print(task_3(25))
