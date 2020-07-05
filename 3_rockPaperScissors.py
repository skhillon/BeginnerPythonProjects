import random

# Maps user input to moves.
moves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

# Maps a move to another move that beats it.
defeats = {
    'rock': 'paper',  # Paper beats rock
    'paper': 'scissors',  # Scissors beats paper
    'scissors': 'rock'  # Rock beats scissors
}

def get_user_move() -> str:
    """Prompts user for input. Keeps prompting if format is incorrect."""
    selection = None
    while selection is None or len(selection) != 1 or selection not in moves.keys():
        selection = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()

    return moves[selection]


def did_user_win(user_move, computer_move) -> bool:
    """Checks if the user beat the computer. Returns `None` if no winner."""
    if computer_move == defeats[user_move]:
        return False
    elif user_move == defeats[computer_move]:
        return True
    else:
        return None


def play_again() -> bool:
    """Checks if the user wants to play again."""
    return input('Play again (y/n)? ').lower() == 'y'


# Main program.
play = True
while play:
    user_move = get_user_move()
    computer_move = random.choice(list(moves.values()))

    print(f'\nUser picked {user_move}.')
    print(f'Computer picked {computer_move}.')

    if user_move == defeats[computer_move]:
        print('User wins!')
    elif computer_move == defeats[user_move]:
        print('Computer wins!')
    else:
        print('No winner.')

    print()
    play = play_again()

