# Ви маєте список [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]],
# дістаньте з нього значення 'Win' та переведіть його у новий список. Результат має бути  ['Win']

lst_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
lst_2 = lst_1[-1][-1]

print(lst_2)
