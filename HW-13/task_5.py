import re
from examples import text_to_search

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')


matchers = pattern.findall(text_to_search)
print(matchers)
