import re
a = input()
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, a)
for match in matches:
    print(match)