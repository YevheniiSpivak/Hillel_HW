import re

pattern = re.compile(r'\d{3}-\d{3}-\d+')

with open('data.txt', 'r') as file:
    content = file.read()
    matchers_1 = pattern.findall(content)
    print(matchers_1)
