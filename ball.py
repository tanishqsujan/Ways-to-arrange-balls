MAX = 100

#table to store to store results of subproblems
dp = [[[[-1] * 4 for i in range(MAX)]
                 for j in range(MAX)]
                 for k in range(MAX)]

#Returns count of arrangements where last placed ball is 'last'. 'last' is 0 for  'p', 1 for 'q', 2 for 'r'
def countways(p, q, r, last):
    
    #if number of balls of any color becomes less than 0 the number of ways arrangements is 0
    if (p < 0 or q < 0 or r < 0):
        return 0
    
    #if last ball required is of type P and the number of balls of P type is 1 while number of balls of other color is 0 the number of ways is 1
    if (p == 1 and q == 0 and r == 0 and last == 0):
        return 1
    
    #same case as above for 'q' and 'r'
    if (p == 0 and q == 1 and r == 0 and last == 1):
        return 1
    
    if (p == 0 and q == 0 and r == 1 and last == 2):
        return 1
    
    #if this subproblem is already evaluated
    if (dp[p][q][r][last] != -1):
        return dp[p][q][r][last]
    
    #if last ball required is P and the number of ways is the sum of numbers of ways to form sequence with 'p-1' P balls, and q Q balls and r R balls ending with Q and R
    if (last == 0):
        dp[p][q][r][last] = (countways(p - 1, q, r, 1) + countways(p - 1, q, r, 2))
        
    #same as above case for 'q' and 'r'
    elif (last == 1):
        dp[p][q][r][last] = (countways(p, q -1, r, 0) + countways(p, q - 1, r, 2))
        
    else:
        
        #(last==2)
        dp[p][q][r][last] = (countways(p, q, r - 1, 0) + countways(p, q, r - 1, 1))
        
    return dp[p][q][r][last]

#returns count of required arrangements
def countuntil(p, q, r):
    
    #Three cases arise:
    #Last required balls is type P
    #Last required balls is type Q
    #Last required balls is type R
    return (countways(p, q, r, 0) + countways(p, q, r, 1) + countways(p, q, r, 2))

p, q, r = 2, 2, 2
print(countuntil(p, q, r))



