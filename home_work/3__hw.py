def  max_number(a, b): #Задание 2
    if a > b:
        print(a)
    else:
        print(b)

max_number(13, 15)


def value(a, b): # Задание 3
    if abs(a - b) == 135:
        print('Yes')
    else:
        print('No')

value(1, 136)


def season(month): # Задание 4
    if month in [12, 1, 2]:
        print('Зима')
    elif month in [3, 4, 5]:
        print('Весна')
    elif month in [6, 7, 8]:
        print('Лето')
    else:
        print('Осень')

season(8)


def more_than_10(a, b, c): # Задание 5
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

more_than_10(11, 15, 30)


def count_positive_numbers(numbers):  # Задание 6
    positive_count = 0
    for number in numbers:
        if number > 0:
            positive_count += 1
    return positive_count

numbers = [-5, 23, -18, 10, -25]
result = count_positive_numbers(numbers)
print(result)


def quantity_days(years, months):  # Задание 7
    days_in_year = 365
    days_in_month = 29
    total_days = years * days_in_year + months * days_in_month
    print(total_days)

quantity_days(5, 9)




