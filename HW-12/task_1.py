def logger(func):
    def wrapper(*args):
        print(f'Function {func.__name__} starting')
        result = func(*args)
        return result

    return wrapper


@logger
def my_max(*args):
    if not args:
        raise TypeError('my_max expected at least 1 argument, got 0')

    if len(args) == 1:
        return args

    max_num = args[0]

    for number in args[1:]:
        if number > max_num:
            max_num = number

    return max_num


@logger
def my_min(*args):
    if not args:
        raise TypeError('my_min expected at least 1 argument, got 0')

    if len(args) == 1:
        return args

    min_num = args[0]

    for number in args[1:]:
        if number < min_num:
            min_num = number

    return min_num


print(my_max(1, 11, 111))
print(my_min(1, 11, 111))
