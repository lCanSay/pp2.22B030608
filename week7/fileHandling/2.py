import os
a = os.access(r"A:\\proga\sem2\week7",os.F_OK)
b = os.access(r"A:\\proga\sem2\week7",os.R_OK)
c = os.access(r"A:\\proga\sem2\week7",os.W_OK)
d = os.access(r"A:\\proga\sem2\week7",os.X_OK)

print(a, b, c ,d)