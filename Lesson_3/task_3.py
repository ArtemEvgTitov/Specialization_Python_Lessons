# Метод append. Для добавления нового элемента в конец списка используется метод append. Метод
# принимает один аргумент — объект который будет добавлен в конец динамически
# увеличенного списка.

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)
my_list.append(my_list)
print(my_list)
# Вывод: [None, 42, 'Hello world!', [1, 3, 5, 7], [...]]

# Метод extend ведёт себя аналогично append, то есть добавляет элементы в конец
# списка. В качестве аргумента extend принимает последовательность, итерируется
# по ней слева направо и каждый элемент добавляет в новую ячейку списка.

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)

# Метод pop позволяет удалить элемент списка. Удаляемый элемент возвращается
# как результат работы метода

my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10) # IndexError: pop index out of range

# Метод count подсчитывает вхождение элемента в список

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.count(2)
print(spam)
eggs = my_list.count(3)
print(eggs)

# Метод index возвращает индекс переданного объекта внутри списка.

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90)
print(eggs)
err = my_list.index(3) # ValueError: 3 is not in list

# Метод insert принимает на вход два аргумента — индекс для вставки и объект
# вставки. Метод добавляет элемент после индекса.

my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73) # my_list.append(73)
print(my_list)

# Метод remove принимает на вход объект, производит его поиск в списке и удаляет в
# случае нахождения.

my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6)
print(my_list)
my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)
