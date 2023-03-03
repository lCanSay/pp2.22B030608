import re
a = input()
pattern = "ab*"
m = re.findall(pattern, a)
print(m)