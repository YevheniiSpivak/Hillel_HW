def square_of_even_numbers(start, end):
    for numbers in range(start, end, 2):
        yield numbers ** 2


start_value = 0
end_value = 1_000_000_000

generation = square_of_even_numbers(start_value, end_value)

for i in range(10):
    print(next(generation))
