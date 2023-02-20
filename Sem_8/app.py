# Основные функции

def add_user(lis):
    user_mane = input("Добавьте пользователя: ")
    lis.append('\n' + user_mane)
    print(f"Контакт {user_mane} успешно добавлен")
    return lis


def search_data(my_list):
    seatch = input("Что ищем? ")
    flag = 0
    print()
    for el in my_list:
        if seatch in el:
            print(el.strip())
            flag += 1
    if flag == 0:
        print("Нет совпадений")


def del_data(my_list):
    flag_run = True
    flag = 0
    seatch = input("Кого будем удалять?: ")
    print()
    while flag_run:
        for el in my_list:
            if seatch in el:
                print(el.strip(),'\n')
                del_user = el
                flag += 1
        if flag > 1:
            seatch = input("Уточните кого именно вы хотите удалить?: ")
            flag = 0
            continue
        if flag == 0:
            print("Нет совпадений")
            return
        if flag == 1:
            confirm = input(f"Удалить контакт {del_user.strip()} ?\n1)Удалить\n2)Вернуться в меню\n")
            match confirm:
                case "1":
                    my_list.remove(del_user)
                    print(f"Контакт {del_user} успешно удален")
                    return
                case _:
                    return
