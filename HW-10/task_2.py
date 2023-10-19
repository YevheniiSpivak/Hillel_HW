number = int(input('Enter a number from 2 to 1000: '))


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    x = 3
    while x * x <= number and number % x != 0:
        x += 2
    return x * x > number

if 2 < number < 1001:
    print(f'{number} is prime: {is_prime(number)}')
else:
    print(f'Please enter a number between 2 and 1000, your nubmer {number} isn\'t suitable')
