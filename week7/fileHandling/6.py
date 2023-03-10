import os
for i in range(26):
    f = open("{}.txt".format(chr(65+i)), "x")
    f.close()
