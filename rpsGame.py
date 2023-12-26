import random, sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of the number of wins, losses, or ties.
wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input().lower()
        if player_move == 'q':
            sys.exit()
        if player_move in ['r', 'p', 's']:
            break
        print('Type one of: r, p, s, or q.')

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display computer choice:
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    if random_number == 2:
        computer_move = 'p'
        print('PAPER')
    if random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/ite
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print("You win!")
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print("You win!")
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print("You win!")
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print("lose win!")
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print("lose win!")
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print("lose win!")
        losses += 1