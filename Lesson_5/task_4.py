# Генератор
# списков полностью формирует список с элементами до его присваивания
# переменной слева от знака равно

my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)

# Как и генераторные выражения списковые включения поддерживаю несколько
# циклов и логические проверки для каждого из циклов. Можно воспринимать их как
# синтаксический сахар, более короткую запись. Например выбираем все чётные
# числа из исходного списка и складываем их в результирующий.
# Длинный код:

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')

# Аналогичное решение, но с использованием синтаксического сахара listcomp:

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

# Если на выходе нужен
# готовый список, оптимальным будет следующий код:

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

# А если нам не нужны все элементы разом. Например мы в дальнейшем хотим
# перебирать значения по одному в цикле. В этом случае подойдет генераторное
# выражение без преобразования в список.

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')

# Кроме синтаксического сахара для генерации списков можно создавать множества
# в одну строку. Синтаксис аналогичен примерам выше. Изменяются лишь скобки.
# Для множеств используются фигурные.

my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

# Ещё один вариант синтаксического сахара — генерация словаря.

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')