# Функция iter имеет формат iter(object[, sentinel]). object является обязательным
# аргументом. Если объект не реализует интерфейс итерации через методы __iter__
# или __getitem__, получим ошибку TypeError.

a = 42
iter(a) # TypeError: 'int' object is not iterable

# Получим итератор списка

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

# Один из простейших способов получить элементы - распаковать итератор через
# звёздочку.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

# Второй параметр функции iter — sentinel передают для вызываемых
# объектов-итераторов. Параметр указывает в какой момент должна быть завершена
# итерация, при совпадении возвращаемого значения со значением sentinel.

data = [2, 4, 6, 8]
list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

# Один из вариантов работы функции iter с двумя параметрами — чтение бинарного
# файла блоками фиксированного размера до тех пор, пока не будет достигнут конец
# файла.

import functools
f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()

# Функция next имеет формат next(iterator[, default]). На вход функция принимает
# итератор, который вернула функция iter. Каждый вызов функции возвращает
# очередной элемент итератора.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter)) # StopIteration

# Второй параметр функции next нужен для возврата значения по умолчанию вместо
# выброса исключения StopIteration

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))