import re

pattern = re.compile(r'\w+@\w+\.\w+')

with open('data.txt', 'r') as file:
    content = file.read()
    matchers = pattern.findall(content)
    print(matchers)
