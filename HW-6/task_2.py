expression = 'hello 1 one three 15 world'

count_word = 0
answer = 'not contains'

# Check three words in a row
for word in expression.split(' '):
    count_word += 1
    if word.isdigit():
        count_word = 0
    elif count_word == 3:
        answer = 'contains'
        break

print(f'The string "{expression}" {answer} three words in a row')
