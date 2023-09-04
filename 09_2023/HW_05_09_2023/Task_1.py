# Задание №1
# 1. Получите словарную форму для первых 20 слов
# 2. Получите словарную форму для последних 10 слов
# 3. Получите словарную форму для слов: бойцовский клуб, игры, сваты, физика
# 4. Получите нормальную форму слова для 20 первых слов

import pymorphy3

morph = pymorphy3.MorphAnalyzer()

with open('text.txt', 'r', encoding='utf-8') as f:
    res = ''.join(f.readlines()).replace('\n', ' ').replace(',', '').replace('.', '').split(' ')
    result = [morph.parse(res[i])[0].methods_stack[0] for i in range(len(res)) if i < 20]
    print(*result, sep='\n') # Словарный анализатор для первых 20 слов
    print()

    res1 = res[::-1]
    result = [morph.parse(res1[i])[0].methods_stack[0] for i in range(len(res1)) if i < 10]
    print(*result, sep='\n')  # Словарный анализатор для последних 10 слов
    print()

    res2 = ['бойцовский', 'клуб', 'игры', 'сваты', 'физика']
    result = [morph.parse(res2[i])[0].methods_stack[0] for i in range(len(res2))]
    print(*result, sep='\n')  # Словарный анализатор для указаных слов
    print()

    result = [morph.parse(res[i])[0].normal_form for i in range(len(res)) if i < 20]
    print(*result, sep='\n')  # Словарный анализатор для первых 20 слов
    print()
