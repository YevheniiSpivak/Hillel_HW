key = input('Enter key: ')

course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    print(f'Value: {course[key]}')
except KeyError:
    print('Key error')
