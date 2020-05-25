def draw_horizontal_line(length):
    print(" ---" * length + " ")


def draw_vertical_line(length):
    print("|   " * length + "|")


def draw_rectangular_board(x, y):
    """#### 1 dimension ####
    print(" --- ")
    print("|   |")
    print(" --- ")

    #### 2 dimensions ####
    print(" --- --- ")
    print("|   |   |")
    print(" --- --- ")
    print("|   |   |")
    print(" --- --- ")"""

    if x == 0 or y == 0:
        return None

    #### n dimensions ####
    for i in range(x): # Loop through the rows
        print("\n ", end="")
        for j in range(y): # Loop through the columns
            print("--- ", end="")

        print("\n|", end="")
        for k in range(y):
            print("   |", end="")

    # Print bottom line
    print("\n ", end="")
    for i in range(y):
        print("--- ", end="")
    print("\n")


def draw_square_board(dimensions):
    for i in range(dimensions):
        draw_horizontal_line(dimensions)
        draw_vertical_line(dimensions)
    # Print bottom line
    draw_horizontal_line(dimensions)


if __name__ == "__main__":
    choice = input("Square [s] or rectangular [r]?\n").lower()

    if choice == 'r':
        num_rows = int(input("How many rows?\n"))
        num_cols = int(input("How many columns?\n"))
        draw_rectangular_board(num_rows, num_cols)
    elif choice == 's':
        board_size = int(input("How many dimensions?\n"))
        draw_square_board(board_size)