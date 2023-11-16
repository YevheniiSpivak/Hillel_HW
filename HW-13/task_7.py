import re
from examples import urls

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matchers = pattern.finditer(urls)
for el in matchers:
    print(el.group())

subbed_str = pattern.sub(r'\2\3', urls)
print(subbed_str)
