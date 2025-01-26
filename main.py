# ========================================================
# This game was made by 2 brothers age 15 and 21 yo
# It was implemented under my older brother's supervision
# 25 January 2025 🎃
# ========================================================


import minesweeper as mswp

#== Initialisation =======================
play_arr = []
show_arr = []

mswp.create_playing_field(play_arr)
mswp.create_playing_field(show_arr)
mswp.spawn_mines(play_arr, 5)
mswp.fill_up_board_around_bombs(play_arr)

#== Game Loop ===================================

did_user_win = False

while True:
    print("\n\n\n=======================================================\n\n\n")

    place_flag_var = False
    
    mswp.print_board(show_arr)
    print()

    #== Combinations ===============================================

    row = 0
    try:
        row = int(input("Enter row: "))
    except:
        print("Invalid row number", end="\n\n")
        continue

    if row < 1 or row > mswp.BOARD_LENGTH:
            print("Invalid row number", end="\n\n")
            continue
    

    column = 0
    try:
        column = int(input("Enter column: "))
    except:
        print("Invalid column number", end="\n\n")
        continue

    if column < 1 or column > mswp.BOARD_LENGTH:
        print("Invalid column number", end="\n\n")
        continue

    #== Open square ================================================

    row -= 1
    column -= 1

    place_flag_var = 0
    try:
        place_flag_var = int(input("Place down a flag: 0 -> false, other_digits -> true: "))
    except:
        print("Invalid flag operation", end="\n\n")
        continue

    if place_flag_var != 0:
        if show_arr[row][column] == mswp.CLOSED_SQUARE_EMOJI:
            mswp.place_down_flag(show_arr, row, column)
        else:
            print("\nSquare at {row}, {column} is alredy open\n".format(row = row, column = column))
    else:
        if show_arr[row][column] == mswp.FLAG_EMOJI:
            show_arr[row][column] = mswp.CLOSED_SQUARE_EMOJI
        elif show_arr[row][column] != mswp.CLOSED_SQUARE_EMOJI:
            print("\nSquare at {row}, {column} is already Opened ! ! !\n".format(row = row, column = column))
        elif show_arr[row][column] == mswp.CLOSED_SQUARE_EMOJI:
            game_continues = mswp.reveal_square(play_arr, show_arr, row, column)
            if not game_continues:
                break
            elif mswp.is_game_won(show_arr):
                did_user_win = True
                break
        
LOSING_EMOJI_LINES = "🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄"
WINNING_EMOJI_LINES = "🎃🎃🎃🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🎃🎃🎃"
line_to_print = WINNING_EMOJI_LINES if did_user_win else LOSING_EMOJI_LINES

print("\nGAME OVER")
print("\n" + line_to_print)

if not did_user_win:
    print("\nYour board:")
    mswp.print_board(show_arr)
else:
    print("\n🎉🎉 YOU SUCCESSFULLY DEFEATED Mr. Pumpkin 🎉🎉")

print("\nActual board:")
mswp.print_board(play_arr)

print("\n" + line_to_print + "\n")
