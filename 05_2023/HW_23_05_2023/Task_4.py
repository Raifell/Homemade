# Задание №_4 Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось количество учащихся,
# б) в школе появился новый класс, с) в школе был расформирован (удален) другой класс. Вычислите общее
# количество учащихся в школе.

import random

classes = ['1a', '1b', '2a', '2b', '3a', '3b', '4a', '4b']
students = 0
school = dict.fromkeys(classes, students)
school_copy_1 = school

for i in school:
    ax = dict({i: random.randint(10, 20)})
    school.update(ax)

print('\nСтартовый вариант словаря:', school_copy_1)

even = random.choice(classes)
new_count_students = dict({even: random.randint(20, 30)})
school.update(new_count_students)
school_copy_2 = school

print(f'\nПосле изменения количества учащихся в классе {even}:', school_copy_2)

new_classes = random.choice(['5a', '5b'])
new_class = dict({new_classes: random.randint(9, 29)})
school.update(new_class)
school_copy_3 = school

print(f"\nПосле добавления нового класса {new_classes}:", school_copy_3)

even_1 = random.choice(classes)
school.pop(even_1)
school_copy_4 = school

print(f'\nПосле удаления класса {even_1}:', school_copy_4)

students_survived = 0
for i in school.values():
    students_survived += i

print('\nСтудентов всего:', students_survived)


# При построении логики заполнения данных, полагался на модуль random, для удобства сделал отдельные print(),
# после каждого выполненного задания
