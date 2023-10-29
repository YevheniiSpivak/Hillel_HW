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


print(my_max(1, 11, 111))
