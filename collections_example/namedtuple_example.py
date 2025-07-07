from collections import namedtuple

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# Створення екземпляра Point
p = Point(11, y=22)

# Доступ до елементів за іменем
print(p.x)  # 11
print(p.y)  # 22


person = ('Mick', 'Nitch', 35, 'Boston', '01146')
# кортежу для особи,  який зберігає ім'я, прізвище, вік, місто народження та поштовий індекс

#Після створення person там, де ви його використовуєте, вам потрібно пам'ятати, що ім'я на першому місці, 
# а вік — на третьому. Щоб не плутатися, доведеться постійно повертатися до коду, 
# де створюється person та перевіряти себе. Це незручно і спеціально для таких випадків додали іменовані кортежі.


# Створення іменованого кортежу Person
Person = namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)       
print(person.post_index) 
print(person.age)        
print(person[3])         


Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')
print(f'This is a cat {cat.nickname}, a {cat.age}-yers-old. His owner is {cat.owner}')
