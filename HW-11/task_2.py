def my_min(*args):
    if not args:
        raise ValueError('Argument not passed')

    if len(args) == 1:
        return args

    min_num = args[0]

    for number in args[1:]:
        if number < min_num:
            min_num = number

    return min_num


print(my_min(1, 11, 111))
