import random
from typing import List


BOARD_LENGTH = 7
NUMBER_OF_BOMBS = [0]

BOMB_EMOJI = "💣"
CLOSED_SQUARE_EMOJI = "⬜"
FLAG_EMOJI = "🚩"
EMPTY_SQUARE_STR = "  "
NUMBERS = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣"
}


# NOTE: Lists are always passed in by a mutable reference

# fills up arr with a valid minesweeper board 
def create_playing_field(arr: List[str]):
    num = 1
    
    for i in range(BOARD_LENGTH):
        new_arr = []
        for j in range(BOARD_LENGTH):  
            new_arr.append(CLOSED_SQUARE_EMOJI)
            num += 1
        arr.append(new_arr)

def spawn_mines(arr: List[List[str]], mine_num: int):
    if mine_num > BOARD_LENGTH * BOARD_LENGTH :
        raise ValueError("Can not spawn more mines:", mine_num, "than squares on the board")
    
    if mine_num < 0:
        raise ValueError("Can not spawn less than 0 mines on the board")

    NUMBER_OF_BOMBS[0] = mine_num

    mines_created = 0

    while mines_created != mine_num:
        row = random.randint(1, BOARD_LENGTH)
        column = random.randint(1, BOARD_LENGTH)

        if arr[row - 1][column - 1] != BOMB_EMOJI:
            arr[row - 1][column - 1] = BOMB_EMOJI
            mines_created += 1
    
#========================================================

def print_board(arr: List[List[str]]):
    print_devider(BOARD_LENGTH)
    num = 1

    for i in arr:
        for j in i:
            print("|", j, "", end ="")
        print("|", num, end ="")
        print()
        print_devider(BOARD_LENGTH)
        num += 1

    num = 1
    print(" ", num, end ="")
    num += 1

    for i in range(BOARD_LENGTH - 1):
        print("   ", num, end ="")
        num += 1

    print()


def print_devider(colums: int):
    print("+----+", end ="")
    for i in range(colums - 1):
        print("----+", end ="")
    print()

#========================================================

# TODO: stop returning bool when dead
def reveal_square(play_arr: List[List[str]], show_arr: List[List[str]], row: int, column: int) -> bool:
    if play_arr[row][column] == BOMB_EMOJI:
        show_arr[row][column] = BOMB_EMOJI
        return False
    elif play_arr[row][column] == EMPTY_SQUARE_STR:
        open_empty_squares_rec(play_arr, show_arr, row, column)
        return True
    else: # if number
        show_arr[row][column] = play_arr[row][column]
        return True

#========================================================

def is_postion_within_bounds(row: int, column: int) -> bool:
    if row < 0 or row > BOARD_LENGTH - 1:
        return False

    if column < 0 or column > BOARD_LENGTH - 1:
        return False
    
    return True
    
def fill_up_board_around_bombs(play_arr: List[str]):
    for row in range(BOARD_LENGTH):
        for column in range(BOARD_LENGTH):
            mine_num = 0

            if is_postion_within_bounds(row - 1, column) and play_arr[row - 1][column] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row - 1, column + 1) and play_arr[row - 1][column + 1] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row, column + 1) and play_arr[row][column + 1] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row + 1, column + 1) and play_arr[row + 1][column + 1] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row + 1, column) and play_arr[row + 1][column] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row + 1, column - 1) and play_arr[row + 1][column - 1] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row, column - 1) and play_arr[row][column - 1] == BOMB_EMOJI:
                mine_num += 1

            if is_postion_within_bounds(row - 1, column - 1) and play_arr[row - 1][column - 1] == BOMB_EMOJI:
                mine_num += 1
            
            if play_arr[row][column] != BOMB_EMOJI:
                match mine_num:
                    case 0: play_arr[row][column] = EMPTY_SQUARE_STR 
                    case 1: play_arr[row][column] = NUMBERS[1] + " "
                    case 2: play_arr[row][column] = NUMBERS[2] + " "
                    case 3: play_arr[row][column] = NUMBERS[3] + " "
                    case 4: play_arr[row][column] = NUMBERS[4] + " "
                    case 5: play_arr[row][column] = NUMBERS[5] + " "
                    case 6: play_arr[row][column] = NUMBERS[6] + " "
                    case 7: play_arr[row][column] = NUMBERS[7] + " "
                    case 8: play_arr[row][column] = NUMBERS[8] + " "

#========================================================

def place_down_flag(arr: List[List[str]], row: int, column: int):
    arr[row][column] = FLAG_EMOJI

#========================================================

def open_empty_squares_rec(play_arr: List[List[str]], show_arr: List[List[str]], row: int, column: int):
    if show_arr[row][column] == FLAG_EMOJI:
        return

    if show_arr[row][column] != CLOSED_SQUARE_EMOJI:
        return
    
    if play_arr[row][column] == BOMB_EMOJI:
        return

    if play_arr[row][column] != EMPTY_SQUARE_STR:
        show_arr[row][column] = play_arr[row][column]
        return 

    if play_arr[row][column] == EMPTY_SQUARE_STR:
        show_arr[row][column] = play_arr[row][column]

        if is_postion_within_bounds(row, column - 1):
            open_empty_squares_rec(play_arr, show_arr, row, column - 1)

        if is_postion_within_bounds(row + 1, column):
            open_empty_squares_rec(play_arr, show_arr, row + 1, column)

        if is_postion_within_bounds(row, column + 1):
            open_empty_squares_rec(play_arr, show_arr, row, column + 1)

        if is_postion_within_bounds(row - 1, column):
            open_empty_squares_rec(play_arr, show_arr, row - 1, column)
             
def is_game_won(show_arr: List[List[str]]) -> bool:
    count = 0
    for row in range(BOARD_LENGTH):
        for column in range(BOARD_LENGTH):
            if show_arr[row][column] != CLOSED_SQUARE_EMOJI and show_arr[row][column] != FLAG_EMOJI:
                count += 1
    if count == BOARD_LENGTH * BOARD_LENGTH - NUMBER_OF_BOMBS[0]:
        return True
    return False