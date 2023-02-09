def unique(nums):
    a = []
    for i in nums:
        if(i not in a):
            a.append(i)
    print(a)
        

unique([1,2,3,4,5,3,4,5,2,4,1])