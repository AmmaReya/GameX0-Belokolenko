import random
# игровое поле
board_value = ['_', '_', '_',
               '_', '_', '_',
               '_', '_', '_']
# выигрышные линии
victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]


# визуализация игрового поля
def draw_board():
    print(board_value[0], board_value[1], board_value[2])
    print(board_value[3], board_value[4], board_value[5])
    print(board_value[6], board_value[7], board_value[8])


# ход игрока
def step_player():
    index = input_adds()
    if board_value[index] != '_':
        print('Позиция занята, повторите снова')
        return step_player()
    step_board(index)


# отображение хода на игровом поле
def step_board(index):
    board_value[index] = player


# проверка результата игры
def result():
    global game_over
    for i in victories:
        if board_value[i[0]] == 'X' and board_value[i[1]] == 'X' and board_value[i[2]] == 'X':
            print('КОНЕЦ ИГРЫ: ПОБЕДИЛИ Х')
            game_over = True
            draw_board()
        elif board_value[i[0]] == '0' and board_value[i[1]] == '0' and board_value[i[2]] == '0':
            print('КОНЕЦ ИГРЫ: ПОБЕДИЛИ 0')
            game_over = True
            draw_board()
    if '_' not in board_value:
        print('КОНЕЦ ИГРЫ: НИЧЬЯ')
        game_over = True
        draw_board()


# выбор символа игрока
def select_symbol():
    symbol = input().upper()
    if symbol == 'X' or symbol == 'Х':
        return 'X'
    if symbol == '0' or symbol == 'O':
        return symbol
    else:
        print('Недопустимый выбор, повторите снова: ')
        return select_symbol()


# преобразования адреса введеного игроком в индекс элемента
def get_index(adds):
    index = {'11': 0, '12': 1, '13': 2,
             '21': 3, '22': 4, '23': 5,
             '31': 6, '32': 7, '33': 8}
    return index[adds]


# выбор игроком позиции для хода
def input_adds():
    line = input('Введите номер строки: ')
    column = input('Введите номер столбца: ')
    if line.isdigit() and column.isdigit() and int(line) in range(1, 4) and int(column) in range(1, 4):
        return get_index(line+column)
    else:
        print('Неверный адрес, повторите попытку')
        return input_adds()


# ход компьютера
def step_computer():
    step = check_line(2, 0)
    if step == '':
        step = check_line(0, 2)
    if step == '':
        step = check_line(1, 0)
    if step == '':
        step = check_line(0, 1)
    if step == '':
        if board_value[4] == '_':
            board_value[4] = computer


# проверка комбинаций для хода компьютера
def check_line(count_c, count_p):
    step = ''
    for i in victories:
        count_computer = 0
        count_player = 0
        for j in range(0, 3):
            if board_value[i[j]] == computer:
                count_computer += 1
            if board_value[i[j]] == player:
                count_player += 1
        if count_computer == count_c and count_player == count_p:
            for j in range(0, 3):
                if board_value[i[j]] == '_':
                    board_value[i[j]] = computer
                    step = 1
                    break
            break
    return step


print('Добро пожаловать в игру КРЕСТИКИ-НОЛИКИ!\nВыберите, за кого будете играть: X или 0')
player = select_symbol()
game_over = False
while not game_over:
    random.shuffle(victories)
    if player == 'X':
        computer = '0'
        draw_board()
        step_player()
        result()
        if game_over:
            break
        step_computer()
        result()
    else:
        computer = 'X'
        step_computer()
        draw_board()
        result()
        if game_over:
            break
        step_player()
        result()
