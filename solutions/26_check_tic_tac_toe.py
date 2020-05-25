####################
#### TEST CASES ####
####################
game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]

no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

also_no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]

def check_tic_tac_toe(board):
    # Rows
    for x in range(0,3):
        row = set([board[x][0], board[x][1], board[x][2]])
        if len(row) == 1 and board[x][0] != 0:
            return board[x][0]

    # Columns
    for x in range(0,3):
        column = set([board[0][x], board[1][x], board[2][x]])
        if len(column) == 1 and board[0][x] != 0:
            return board[0][x]

    # Diagonals
    diag_1 = set([board[0][0], board[1][1], board[2][2]])
    diag_2 = set([board[0][2], board[1][1], board[2][0]])
    if len(diag_1) == 1 or len(diag_2) == 1 and board[1][1] != 0:
        return board[1][1]

    return 0


if __name__ == "__main__":
    print(check_tic_tac_toe(game))
    print(check_tic_tac_toe(winner_is_2))
    print(check_tic_tac_toe(winner_is_1))
    print(check_tic_tac_toe(winner_is_also_1))
    print(check_tic_tac_toe(no_winner))
    print(check_tic_tac_toe(also_no_winner))