numbers = list(input('Enter some numbers: ').split(' '))

print(f'Result: {len(numbers) == len(set(numbers))}')
