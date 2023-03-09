a = input()
u = 0
l = 0
for i in a:
    if(i.islower()):
        l += 1
    elif(i.isupper()):
        u += 1
print("Lowercase", l)
print("Uppercase", u)
