import os
a = r"A:\\proga\sem2\week7"
if os.path.exists(a):
    print(os.path.basename(a))
    print(os.path.dirname(a))
