x = int(input('Enter number: '))

lst = list(range(1, 21))

print('Result: ', end='')

for number in lst:
    if number % x == 0:
        print(number, end=' ')
