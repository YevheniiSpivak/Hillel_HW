petals = int(input('There is an ancient game with "divining"\n'
                   'Plucking a petal, one of the phrases is pronounced. How many petals?\n'))

lst = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']

if petals > len(lst):
    petals = petals % len(lst)

print(f'Result: {lst[petals - 1]}')
