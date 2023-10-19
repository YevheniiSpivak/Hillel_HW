number = int(input('Enter a number from 2 to 1000: '))


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    x = 3
    while x * x <= number and number % x != 0:
        x += 2
    return x * x > number


print(f'{number} is prime: {is_prime(number)}')
