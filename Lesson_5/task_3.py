# С одним из генераторов мы уже знакомы. Это объект, возвращаемый функцией
# range. При создании генератора мы указываем диапазон перебираемых целых
# чисел, но не сохраняем их в памяти. Каждое из значений генерируется на
# очередном витке цикла.

a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# Генераторные выражения Python позволяют создать собственный генератор,
# перебирающий значения.

my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)

# В общем виде генератор можно записать как:

# gen = (expression for expr in sequense1 if condition1
#     for expr in sequense2 if condition2
#     for expr in sequense3 if condition3
#     ...
#     for expr in sequenseN if conditionN)

# Если расписать выражение в обычном коде, получим следующий код:
# for expr in sequense1:
#   if not condition1:
#       continue
#   for expr in sequense2:
#       if not condition2:
#           continue
#           ...
#       for expr in sequenseN:
#           if not conditionN:
#               continue

# При работе с генераторами стоит помнить, что для каждого витка внешнего цикла
# внутренний перебирает все элементы от начала до конца. Например:

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

