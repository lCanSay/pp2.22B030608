import re
a = input()
matches = re.findall(r'[A-Z][a-z]+', a)
print(matches)