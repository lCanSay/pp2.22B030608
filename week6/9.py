import re
a = input()
m = re.findall("[A-Z][a-z]*", a)
print(' '.join(m))