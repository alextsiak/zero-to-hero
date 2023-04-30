def print_board():
    return f"{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}"

def player_symbol():
    made_choice = False
    while made_choice == False:
        p1_symbol = input("Player 1, choose 'X' or 'O': ")
        if p1_symbol == 'X':
            made_choice = True
            p2_symbol = 'O'
        elif p1_symbol == 'O':
            made_choice = True
            p2_symbol = 'X'
    return p1_symbol, p2_symbol

def play_round():
    #Player inputs choice
    valid_choice = False
    while valid_choice == False:
        choice = int(input(f"Player {current_player}, make your move (1-9): "))
        if choice in range(1,10) and choice not in p1_moves and choice not in p2_moves:
            if current_player == 1:
                board[choice-1] = p1_symbol
                p1_moves.add(choice)
            else:
                board[choice-1] = p2_symbol
                p2_moves.add(choice)
            valid_choice = True

def check_win():
    #Checks if someone won or if there's a draw (if statements are separate for readability)
    #Checks if horizontal win
    if set([1,2,3]).issubset(p1_moves) or set([1,2,3]).issubset(p2_moves):
        return True
    elif set([4,5,6]).issubset(p1_moves) or set([4,5,6]).issubset(p2_moves):
        return True
    elif set([7,8,9]).issubset(p1_moves) or set([7,8,9]).issubset(p2_moves):
        return True
    #Checks if vertical win
    elif set([1,4,7]).issubset(p1_moves) or set([1,4,7]).issubset(p2_moves):
        return True
    elif set([2,5,8]).issubset(p1_moves) or set([2,5,8]).issubset(p2_moves):
        return True
    elif set([3,6,9]).issubset(p1_moves) or set([3,6,9]).issubset(p2_moves):
        return True
    #Checks if diagonal win
    elif set([1,5,9]).issubset(p1_moves) or set([1,5,9]).issubset(p2_moves):
        return True
    elif set([3,5,7]).issubset(p1_moves) or set([3,5,7]).issubset(p2_moves):
        return True

board = [" "," "," "," "," "," "," "," "," "]
p1_moves = set()
p2_moves = set()
current_player = 1

print("Welcome to Tic Tac Toe!")
p1_symbol, p2_symbol = player_symbol()
print(f"Player 1 is {p1_symbol}. Player 2 is {p2_symbol}.")
print("Use a number (1-9) to make your choice. Here's a reference for the board: ")
print("[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]")

while not check_win():
    if len(p1_moves) == 5 or len(p2_moves) == 5:
        print("It's a draw!")
        break
    play_round()
    print(print_board())
    if check_win():
        print(f"Congratulations Player {current_player}!")
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
