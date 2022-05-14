from random import randint

arz = 10
tool = 10 
board = []
for y in range(tool) :
    new_row = []
    for x in range(arz) :
       new_row.append(dict(value = 0 , is_show = False))
    board.append(new_row)

tool_cell = 3
tool_saghf = (tool_cell + 1) * arz + 1 
bombs = 7
around_bomb = [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1,+1)]

def print_board():
    def str_center(item) :
        cell = str(item.get("value")) if item.get("is_show") else "X"
        return cell.center(tool_cell)
    saghf = "-" * tool_saghf
    print(saghf)

    for row in board:
        row_cell = "|" + "|".join(map(str_center , row)) + "|"
        print(row_cell)
        print(saghf)


def select_bombs() :
    global board
    def update_bomb_boarder(x , y) :
        for diff_x , diff_y in around_bomb :
            new_x = x + diff_x
            new_y = y + diff_y

            if (0 <= new_x < arz) and (0 <= new_y < tool) and board[new_y][new_x] != 2 :
                board[new_y][new_x].update(value = 1)

    for _ in range(bombs):
        x = randint(0, arz - 1)
        y = randint(0, tool - 1)

        board[y][x].update(value = 2)
        update_bomb_boarder(x , y)

select_bombs()
rounds = 0
while True:
    print_board()
    rounds += 1

    if rounds == (arz * tool) - bombs :
        print("MashaLLaaaa")
        break
    x , y = list(map(int, input().split()))
    if (0 <= x < arz) and (0 <= y < tool) :
        if board[y][x].get("value") == 2 :
            print("ishaLLa yerooz dige")
            break
        else:
            board[y][x].update(is_show = True)
    else:
        print("Invalid input")