def solve(numheads, numlegs):
    for i in range(numheads+1):
        c = numheads - i
        if(i*4+c*2==numlegs):
            return(i, c)
    return("No solution")

print(solve(35,94))
    