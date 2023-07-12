f = open('text.txt')
print(f)
print(list(f))

f = open('text.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

f = open('text.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()