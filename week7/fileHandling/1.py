import os
a = os.listdir(r"A:\\proga\sem2\week7")
dirs = []
files = []

for i in a:
    if os.path.isdir(os.path.join("A:\\proga\sem2\week7", i)):
        dirs.append(i)
print(dirs)

for i in a:
    if not os.path.isdir(os.path.join("A:\\proga\sem2\week7", i)):
        files.append(i)
print(files)

for i in a:
    if os.path.isfile(os.path.join("A:\\proga\sem2\week7", i)) or (os.path.isdir(os.path.join("A:\\proga\sem2\week7", i))):
        print(i)

