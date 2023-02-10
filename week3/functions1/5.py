def permutation(s, index, length):
    if(index == length):
        print(''.join(s))
    else: 
        for i in range(index,length): 
            s[index], s[i] = s[i], s[index] 
            permutation(s, index+1, length) 
            s[index], s[i] = s[i], s[index]  


a = "thanks"
l = len(a)
permutation(a, 0, l)