def my_max(*args):
    if not args:
        raise ValueError('Argument not passed')

    if len(args) == 1:
        return args

    max_num = args[0]

    for numbers in args[1:]:
        if numbers > max_num:
            max_num = numbers

    return max_num


print(my_max(1, 11, 111))
