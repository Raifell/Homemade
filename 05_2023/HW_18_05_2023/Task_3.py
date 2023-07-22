#Задание №_3 - Дополнить имеющийся код игры, обновленный после выполнения Задания №_1 и Задания №_2,
#добавить отображение общего количества побед и поражений, по завершении выполнения внутреннего цикла.


import random

while True:
    try:
        count = int(input("Сколько раз вы хотите сыграть?: "))
    except ValueError:
        print("Введите число!")
    else:
        count_start = 1
        win = 0
        lose = 0
        while count_start <= count:
            print("Раунд", count_start)
            user_action_1 = input("\nСделайте выбор — камень, ящерица, спок, ножницы или бумага:\n")
            user_action = user_action_1.lower()
            possible_actions = ["камень", "бумага", "ножницы", "ящерица", "спок"]
            computer_action = random.choice(possible_actions)
            print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")

            if user_action == computer_action:
                count_start += 1
                print(f"Оба пользователя выбрали {user_action}. Ничья!!")

            elif user_action == "камень":
                count_start += 1
                if computer_action == "ножницы":
                    print("Камень бьет ножницы! Вы победили!")
                    win += 1
                elif computer_action == "ящерица":
                    print("Камень бьет ящерицу! Вы победили!")
                    win += 1
                elif computer_action == "спок":
                    print("Спок разрушает камень! Вы проиграли!")
                    lose += 1
                else:
                    print("Бумага оборачивает камень! Вы проиграли.")
                    lose += 1

            elif user_action == "бумага":
                count_start += 1
                if computer_action == "камень":
                    print("Бумага оборачивает камень! Вы победили!")
                    win += 1
                elif computer_action == "спок":
                    print("Бумага закрывает спок! Вы победили")
                    win += 1
                elif computer_action == "ящерица":
                    print("Ящерица жует бумагу! Вы проиграли!")
                    lose += 1
                else:
                    print("Ножницы режут бумагу! Вы проиграли.")
                    lose += 1

            elif user_action == "ножницы":
                count_start += 1
                if computer_action == "бумага":
                    print("Ножницы режут бумагу! Вы победили!")
                    win += 1
                elif computer_action == "ящерица":
                    print("Ножницы режут ящерицу! Вы победили!")
                    win += 1
                elif computer_action == "спок":
                    print("Спок хватает ножницы! Вы проиграли!")
                    lose += 1
                else:
                    print("Камень бьет ножницы! Вы проиграли.")
                    lose += 1

            elif user_action == "ящерица":
                count_start += 1
                if computer_action == "бумага":
                    print("Ящерица жует бумагу! Вы победили!")
                    win += 1
                elif computer_action == "спок":
                    print("Ящерица кусает спок! Вы победили!")
                    win += 1
                elif computer_action == "камень":
                    print("Камень бьет ящерицу! Вы проиграли!")
                    lose += 1
                else:
                    print("Ножницы режут ящерицу! Вы проиграли.")
                    lose += 1

            elif user_action == "спок":
                count_start += 1
                if computer_action == "камень":
                    print("Спок разрушает камень! Вы победили!")
                    win += 1
                elif computer_action == "ножницы":
                    print("Спок хватает ножницы! Вы победили!")
                    win += 1
                elif computer_action == "ящерица":
                    print("Ящерица кусает спок! Вы проиграли!")
                    lose += 1
                else:
                    print("Бумага закрывает спок! Вы проиграли.")
                    lose += 1

            else:
                print("Выбранное значение не соответствует игровому жесту!\n")

        print("Счет -", "Игрок:", win, "Компьютер:", lose)
        over = input("\nХотите сыграть еще раз? Д/Н:\n")
        over = over.lower()
        if over == "н":
            break


#За основу был взят код из файла "Новый текстовый документ.txt", из архива с домашним заданием.
#Код был дополнен согласно условиям задачи №_3
#
#Были добавлены переменные отвечающие за количество побед и поражений, так же добавлено отображение
#данных этих переменных в числовом значении, после завершения выполнения внутреннего цикла.
