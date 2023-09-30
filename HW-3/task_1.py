phrase = input('- Hi, please enter some text\n- ')
char = input('- You are wonderful, write a letter or text and I\'ll remove it from the previous text\n- ')

print('- Result is –', '\"' + phrase.replace(char, '').strip() + '\"', ':)')
