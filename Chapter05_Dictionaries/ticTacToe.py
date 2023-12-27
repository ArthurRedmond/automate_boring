"""Simple Tic Tac Toe."""

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    """Prints the game board."""
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('--+---+--')
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('--+---+--')
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")


def main():
    """Main function."""
    turn = 'X'
    for _ in range(9):
        print_board(the_board)
        print(f'Turn for {turn}. Move on which space?')
        move = input()
        the_board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print_board(the_board)

if __name__ == '__main__':
    main()
