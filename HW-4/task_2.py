phrase = input('Enter text: ')

if phrase == ''.join(reversed(phrase)):     # We can use: if phrase == phrase[::-1]:
    print('Is a palindrome')
else:
    print('Is not a palindrome')

