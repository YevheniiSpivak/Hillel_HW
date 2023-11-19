import re
from examples import text_to_search

pattern = re.compile(r'abc')

matchers = pattern.findall(text_to_search)
print(matchers)
