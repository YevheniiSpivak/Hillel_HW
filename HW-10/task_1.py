first_number = float(input('Enter first number: '))
operation = input('Operation: ')
second_number = float(input('Second number: '))


def calculate(first_number, second_number, operation):
    result = f'Not known operation: {operation}'

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number

    return result


print(calculate(first_number, second_number, operation))
