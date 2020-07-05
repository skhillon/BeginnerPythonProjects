from typing import Set
import random
import string

special_symbols = set(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'])
hard_to_read_symbols = set(['L', 'I', 'O', '0'])


def ask_required_length() -> int:
    error_message = 'Length must be a positive integer.'

    while True:
        try:
            length = int(input('Length: '))
            if length <= 0:
                print(error_message, end = ' ')
                continue

            return length
        except ValueError:
            print(error_message, end = '')


def ask_require(field_name: str) -> bool:
    error_message = "Please enter either 'y' for yes or 'n' for no."

    while True:
        preference = input(f'Require {field_name} (y/n)? ').lower()
        if preference == 'y':
            return True
        elif preference == 'n':
            return False


def ask_password_restrictions() -> str:
    error_message = "Please enter 's' for easy to say, 'r' for easy to read, or 'a' for all characters."

    while True:
        preference = input('Easy to say (s), easy to read (r), or allow all characters (a)? ').lower()
        if preference in ('s', 'r', 'a'):
            return preference


def make_symbol_set(
    require_uppercase: bool,
    require_lowercase: bool,
    require_number: bool,
    require_symbol: bool,
    restriction_type: str
) -> Set[str]:
    symbols = set()

    if require_lowercase:
        symbols.update(string.ascii_lowercase)
    
    if require_uppercase:
        symbols.update(string.ascii_uppercase)
    
    if require_number and restriction_type in ('r', 'a'):
        symbols.update(string.digits)
    
    if require_symbol and restriction_type in ('r', 'a'):
        symbols.update(special_symbols)

    if restriction_type == 'r':
        symbols.difference_update(hard_to_read_symbols)

    return symbols


def make_password(length: int, symbols: Set[str]) -> str:
    symbol_bank = tuple(symbols)  # Can't randomly sample from set, need to convert.
    return ''.join(random.choice(symbol_bank) for _ in range(length))


def ask_generate_another_password() -> bool:
    return input('Generate another password (y/n)? ').lower() == 'y'


# Main program.
run = True
while run:
    print('Please enter your preferences.')
    
    length = ask_required_length()
    uppercase = ask_require('an uppercase letter')
    lowercase = ask_require('a lowercase letter')
    number = ask_require('a number')
    symbol = ask_require('a symbol')
    restriction = ask_password_restrictions()

    symbol_set = make_symbol_set(uppercase, lowercase, number, symbol, restriction)
    print(f'Your generated password is: {make_password(length, symbol_set)}')

    print()
    run = ask_generate_another_password()
