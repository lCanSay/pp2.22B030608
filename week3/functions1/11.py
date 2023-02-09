def palindrome(stroka):
    strcopy = ""
    for i in range(len(stroka)-1,-1,-1):
        strcopy += stroka[i]
    if(strcopy == stroka):
        print("Yes")
    else:
        print("No")

a = str(input())
palindrome(a)