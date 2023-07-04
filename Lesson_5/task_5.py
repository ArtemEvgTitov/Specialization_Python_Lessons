# Рассмотрим создание генератора не в одну строку, а как отдельную функцию.
# Например нам надо посчитать факториал чисел от одного до n.
# Прежде чем создавать генератор, создадим обычную функцию, которая вернёт
# список чисел.

def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result
for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Изменим функцию для получения факториала чисел, превратив её в генератор.

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number
for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Уже знакомые по сегодняшнему уроку функции iter и next могут работать с
# созданными генераторами. Например так:

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # StopIteration