import os
p=(r"A:\proga\sem2\C.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("doesnt exist")