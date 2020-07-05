import operator

operations = [operator.add, operator.sub, operator.mul, operator.truediv, operator.pow]
menu = """
Choose from the options, or type anything else to exit:
    (1) Add
    (2) Subtract
    (3) Multiply
    (4) Divide
    (5) Exponent
"""

def get_number(name: str) -> float:
    num = None
    while num is None:
        try:
            num = float(input(f'Enter {name}: '))
        except ValueError:
            print('Please enter a valid number')

    return num


while True:
    first_number = get_number('first number')
    second_number = get_number('second number')

    print(menu)
    try:
        index = int(input('Pick an operation: ')) - 1
        if not (0 <= index < len(operations)):
            break

        op = operations[index]
        print(f'Result: {op(first_number, second_number)}')
    except:
        break

    print()
