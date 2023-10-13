family = {'grandpa': ('Alex', 76),
          'grandma': ('Nona', 74),
          'dad': ('Greg', 48),
          'mom': ('July', 45),
          'son_older': ('Bob', 18),
          'son_middle': ('Alex', 15),
          'son_young': ('Mark', 10)}

age = []

for value in family.values():
    age.append(value[1])

print(f'Result: {max(age) - min(age)}')
