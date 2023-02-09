def reverse(s):
    a = s.split()
    for i in range(len(a)-1,-1,-1):
        print(a[i], end = " ")

reverse("We live in society")