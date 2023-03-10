f1=open("A.txt", "r")
f2=open("B.txt", "w")
for i in f1:
    f2.write(i)