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
prev_result = None

def get_number(name: str):
    num = None
    while num is None:
        try:
            num = input(f'Enter {name}: ')
            if num == 'p':
                return prev_result

            num = float(num)
        except ValueError:
            print('Please enter a valid number')

    return num


# Main
while True:
    if prev_result is not None:
        first_number = get_number('first number (or "p" to use previous result)')
    else:
        first_number = get_number('first number')

    second_number = get_number('second number')

    print(menu)
    try:
        index = int(input('Pick an operation: ')) - 1
        if not (0 <= index < len(operations)):
            break

        op = operations[index]
        prev_result = op(first_number, second_number)
        print(f'Result: {prev_result}')
    except:
        break

    print()
