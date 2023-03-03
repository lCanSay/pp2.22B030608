import re
a = input()
def sn(l):
    v = re.findall("[a-z]+", a)
    h = ""
    for i in v:
        h += i[0].upper() + i[1 : len(i)]
    return h
print(sn(a))