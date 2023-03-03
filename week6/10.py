import re
a = input()
res=re.findall(r"[A-Z][a-z]*", a)
newlist=[]
for i in res:
    newlist.append(i.lower())
print('_'.join(newlist))