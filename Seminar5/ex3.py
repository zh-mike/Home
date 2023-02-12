# 3. Игра крестики нолики

def print_table(): # Вывод в терминал игровое поле
    print()
    for i in range(len(table_game)):
        if i == 2 or i == 5 or i == 8: # Проверка для того что бы поставить переход на новую строку
            print(f"[{table_game[i]}]", end='\n')
        else:
            print(f"[{table_game[i]}]", end=' ')


def check_table(): # Победные комбинации
    match table_game:
        case [
            "X", "X", "X",
             _,   _,   _,  
             _,   _,   _] | ["O", "O", "O", 
                              _,   _,   _,
                              _,   _,   _]:
            return True
        case [
             _,   _,   _, 
            "X", "X", "X", 
             _,   _,   _] | [ _,   _,   _, 
                              "O", "O", "O", 
                              _,   _,   _]:
            return True
        case [
             _,   _,   _,  
             _,   _,   _, 
            "X", "X", "X"] | [ _,   _,   _,   
                               _,   _,   _, 
                              "O", "O", "O"]:
            return True
        case [
            "X", _, _,  
            "X", _, _, 
            "X", _, _] | ["O", _, _,  
                          "O", _, _, 
                          "O", _, _]:
            return True
        case [
            _, "X", _,
            _, "X", _,  
            _, "X", _] | [_, "O", _,  
                          _, "O", _,  
                          _, "O", _]:
            return True
        case [
            _, _, "X",  
            _, _, "X", 
            _, _, "X"] | [_, _, "O",
                          _, _, "O", 
                          _, _, "O"]:
            return True
        case [
            "X", _,  _,
             _, "X", _,
             _,  _, "X"] | [ "O", _,  _,
                              _, "O", _, 
                              _,  _, "O"]:
            return True
        case [
             _,  _, "X",
             _, "X", _,
            "X", _,  _] | [  _,  _, "O",
                             _, "O", _, 
                            "O", _,  _]:
            return True


def motion(): # Основная функция 
    x_or_o = "X"
    while True:
        num = int(input(f"Введите цифру, куда поставить {x_or_o}: "))
        while not num in table_game:
            num = int(
                input(f"Нет такой позиции.\nВведите цифру {x_or_o}: "))
        table_game[num-1] = x_or_o
        print_table()
        if check_table():
            return f"Победил {x_or_o}"
        if set(table_game) == {"X", "O"}: # Проверка на ничью
            return "Ничья"
        x_or_o = "O" if x_or_o == "X" else "X"

# Начальное игровое поле
table_game = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

print_table() 
print(motion())

