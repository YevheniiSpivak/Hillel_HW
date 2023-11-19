import re
from examples import text_to_search

pattern = re.compile(r'\d{3}-\d{3}-\d+')

matchers = pattern.findall(text_to_search)
print(matchers)
