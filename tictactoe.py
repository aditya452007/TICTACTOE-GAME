import random

leaderboard = {}

def hello(skip=False, prev_name1=None, prev_name2=None, mode=None):
    if skip and prev_name1 and prev_name2:
        return prev_name1, prev_name2, mode
    
    print("Welcome To Tic Tac Toe".center(50))
    name1 = input("\nPlease enter your name: ".title())
    print("\nYou are X".title())
    
    while True:
        mode = input("\nChoose mode: (1) Single Player (2) Two Player: ").strip()
        if mode in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1 or 2.")
    
    if mode == "2":
        name2 = input("\nPlease enter opponent's name: ".title())
        print("\nYou are O".title())
    else:
        name2 = "Computer"
    
    return name1.capitalize(), name2.capitalize(), mode

def sum(a, b, c):
    return a + b + c == 3  

def printboard(xstate, zstate):
    board = [
        'X' if xstate[i] else ('O' if zstate[i] else str(i)) for i in range(9)
    ]
    print()
    print("\n" + " " * 10 + " TIC TAC TOE")
    print(" " * 10 + "=============")
    print(f"\n   {board[0]}  |  {board[1]}  |  {board[2]}")
    print("  ----|-----|----")
    print(f"   {board[3]}  |  {board[4]}  |  {board[5]}")
    print("  ----|-----|----")
    print(f"   {board[6]}  |  {board[7]}  |  {board[8]}")

def checkwin(xstate, zstate, name1, name2):
    wins = [
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]):
            print(f"X i.e. {name1} wins the game!!!!")
            leaderboard[name1] = leaderboard.get(name1, {'wins': 0, 'losses': 0})
            leaderboard[name2] = leaderboard.get(name2, {'wins': 0, 'losses': 0})
            leaderboard[name1]['wins'] += 1
            leaderboard[name2]['losses'] += 1
            return 1
        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]):
            print(f"O i.e. {name2} wins the game!!!!")
            leaderboard[name2] = leaderboard.get(name2, {'wins': 0, 'losses': 0})
            leaderboard[name1] = leaderboard.get(name1, {'wins': 0, 'losses': 0})
            leaderboard[name2]['wins'] += 1
            leaderboard[name1]['losses'] += 1
            return 0
    
    if all(xstate[i] or zstate[i] for i in range(9)):
        print("The game is a draw!")
        return 2  
    
    return -1

def get_valid_input(player):
    while True:
        try:
            value = int(input(f"\n{player}, please enter a position (0-8): "))
            if 0 <= value < 9 and xstate[value] == 0 and zstate[value] == 0:
                return value
            else:
                print("Invalid move, try again!")
        except ValueError:
            print("Invalid input! Please enter a number between 0-8.")

def computer_move():
    available_moves = [i for i in range(9) if xstate[i] == 0 and zstate[i] == 0]
    return random.choice(available_moves)

def display_leaderboard():
    if leaderboard:
        print("\nLeaderboard:")
        for player, stats in leaderboard.items():
            print(f"{player}: {stats['wins']} wins, {stats['losses']} losses")

def play_game(skip_intro=False, prev_name1=None, prev_name2=None, prev_mode=None):
    global xstate, zstate
    xstate = [0] * 9 
    zstate = [0] * 9  
    display_leaderboard()
    name1, name2, mode = hello(skip_intro, prev_name1, prev_name2, prev_mode)
    turn = 1
    
    while True:
        printboard(xstate, zstate)
        if turn == 1:
            print("\nX's chance")
            value = get_valid_input(name1)
            xstate[value] = 1
            turn = 0
        else:
            if mode == "2":
                print("\nO's chance")
                value = get_valid_input(name2)
            else:
                print("\nComputer's turn")
                value = computer_move()
                print(f"Computer chose position {value}")
            zstate[value] = 1
            turn = 1
        
        check = checkwin(xstate, zstate, name1, name2)
        if check != -1:
            printboard(xstate, zstate)
            break
        
    while True:
        restart = input("\nDo you want to Continue, Quit, or Play with someone else(pwse)? enter (continue/quit/pwse): ".title()).strip().lower()
        if restart == "continue":
            play_game(True, name1, name2)
            break
        elif restart == "pwse":
            play_game()
            break
        elif restart == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'change'.")

if __name__ == "__main__":
    play_game()
