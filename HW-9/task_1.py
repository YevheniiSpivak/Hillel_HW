with open('readme.txt', 'r', encoding='utf8') as file:
    with open('second_file.txt', 'w') as second_file:
        for line in file:
            second_file.write(line)
