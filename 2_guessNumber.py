import random

def get_integer(name: str) -> int:
    num = None
    while num is None:
        try:
            num = int(input(f'Enter {name}: '))
        except ValueError:
            print('Please enter a valid integer')

    return num


def play_again() -> bool:
    return input('Play again (y/n)? ').lower() == 'y'


# Main program
play = True
while play:
    lower_bound = get_integer('lower bound')
    upper_bound = get_integer('upper bound')
    if lower_bound >= upper_bound:
        raise ValueError('Lower bound must be less than upper bound')

    computer_choice = random.randint(lower_bound, upper_bound)
    while True:
        user_choice = get_integer('a number')
        if user_choice == computer_choice:
            print('You got it!')
            break
        elif user_choice < computer_choice:
            print('Higher')
        else:
            print('Lower')

    play = play_again()
