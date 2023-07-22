# Задание №_2 Подсчитать в текстовом файле количество слов.

count = 0 # Переменная отвечающая за количество пробелов и '\n'

text_1 = 'In order to get the value from the dictionary,\n'
text_2 = 'the hash of the elem variable is needed.\n'
text_3 = 'The hash value is needed twice: to get the previous value and to set the new one.\n'
text_4 = 'Obviously, calculating two hashes is doing double work.'

try:
    with open('Task_2.txt', 'r') as f: # В случае если файл есть, считаем в нем количество пробелов и '\n'
        ax = f.read()
        for i in ax:
            if i == ' ' or i == '\n':
                count += 1

except:
    with open('Task_2.txt', 'w') as f: # Если файла нет, создаем его и записываем в него текст
        f.write(text_1)
        f.write(text_2)
        f.write(text_3)
        f.write(text_4)

    with open('Task_2.txt', 'r') as f: # Считаем количество пробелов и '\n'
        ax = f.read()
        for i in ax:
            if i == ' ' or i == '\n':
                count += 1

result = count + 1 # Количество слов будет больше суммарного количества пробелов и '\n' на 1

print(result)