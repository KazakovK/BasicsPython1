a = 'Строковое'
b = 102
c = 10.9
d = [9, 'Строка', -12.6]
e = (21, 98, -9, 11.1)
f = {
    a: 12,
    c: (12, 9, 6),
    'Строка': 'Строка'
}
print(f'Вывод переменных:\n строка - {a},\n число - {b} и {c},\n массив - {d} и {e},\n словарь - {f},'
      f'\n элемент словаря - {a}')

age = input('Введите ваш возраст: ')
age = 60 - int(age)
print(f'Вам осталось до пенсии: {age} лет')

name = input('Как вас зовут?')
position = input('Какая у вас должность?')

print('Здравствуйте,',name,'. Ваша должность ',position,' очень интересная!')
