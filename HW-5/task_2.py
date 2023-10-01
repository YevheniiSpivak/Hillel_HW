lst = [1, 2, 5, 68, 0]      # False
# lst = [1, 2, 3, 4, 5]     # True

for i in range(len(lst)-1):
    if lst[i] + 1 != lst[i+1]:
        print(f'The number {lst[i+1]} is not consecutive')
        break
else:
    print('Number is consecutive')
