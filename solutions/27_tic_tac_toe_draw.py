# p_1: Player 1
# p_2: Player 2


def draw_board(board):
    # Draw a general list of lists as a board
    size = len(board)
    if size == 0:
        return None

    #### n dimensions ####
    for i in range(size): # Loop through the rows
        print("\n ", end="")
        for j in range(size): # Loop through the columns
            print("--- ", end="")

        print("\n|", end="")
        for k in range(size):
            print(f" {board[i][k]} |", end="")

    # Print bottom line
    print("\n ", end="")
    for i in range(size):
        print("--- ", end="")
    print("\n")


def update_board(board, p_1, x, y):
    # Update board based on player coordinates
    if p_1:
        board[x - 1][y - 1] = "X"
    else:
        board[x - 1][y - 1] = "0"

    return board


def get_p_coordinates(p_input):
    # Convert the string input by each player into coordinates for update_board function
    # Assume player input is valid, but testing would be easy if it wasn't anyway
    p_coords = list(map(int, (p_input.strip()).split(",")))

    return p_coords


def check_repeat_position(x, y):
    if board[x - 1][y - 1] != " ":
        return True
    return False


def ask_p_1():
    while 1:
        p_1_choice = input("\nPlayer 1, where would you like to place your X? (Format: 'x,y')\n")
        p_1_coords = get_p_coordinates(p_1_choice)
        if check_repeat_position(p_1_coords[0], p_1_coords[1]):
            print("That position is taken, choose another one.\n")
            continue
        break

    return p_1_coords


def ask_p_2():
    while 1:
        p_2_choice = input("\nPlayer 2, where would you like to place your 0? (Format: 'x,y')\n")
        p_2_coords = get_p_coordinates(p_2_choice)
        if check_repeat_position(p_2_coords[0], p_2_coords[1]):
            print("That position is taken, choose another one.\n")
            continue
        break

    return p_2_coords


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
flat_board = [element for row in board for element in row]

while " " in flat_board: # While board is not empty
    # If the end of this loop is reached, the game is a draw
    p_1_coords = ask_p_1()
    board = update_board(board, p_1=True, x=p_1_coords[0], y=p_1_coords[1])
    flat_board = [element for row in board for element in row]
    if " " not in flat_board:
        draw_board(board)
        break

    p_2_coords = ask_p_2()
    board = update_board(board, p_1=False, x=p_2_coords[0], y=p_2_coords[1])
    flat_board = [element for row in board for element in row]

    draw_board(board)