def filter_prime(numbers):
    for i in numbers:
        a = 0
        if(i!=1):
            for j in range (2, int(i/2)+1):
                if(i%j==0):
                    a = 1
                    break
            if(a==0):
                print(i, " ")
            
filter_prime([1,2,3,4,5,6,7,8,9,10])
            