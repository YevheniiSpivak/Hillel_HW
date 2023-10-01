first_number = int(input('Enter first number: '))
action = input('Action: ')
second_number = int(input('Second number: '))

result = 0

if action == '+':
    result = first_number + second_number
elif action == '-':
    result = first_number - second_number
elif action == '*':
    result = first_number * second_number
elif action == '/':
    result = first_number / second_number
else:
    print('Wrong action')

print(f'Result: {result}')
