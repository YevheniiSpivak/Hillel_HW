name = input('Enter name: ').title()

roles = {'admin': ['Eva', 'Franklin', 'Willie'],
         'maintainer': ['Carmen', 'Arron'],
         'manager': ['Erica', 'Halle'],
         'developer': ['Joel', 'Shirley', 'Jeremiah']}

role = 'Guest'

for key_role, values in roles.items():
    if name in values:
        role = key_role
        break

print(f'Hello, {role}')
