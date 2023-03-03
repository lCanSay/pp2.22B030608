import re
a = input()
pattern = "ab{2,3}"
m = re.findall(pattern, a)
print(m)