# dp algorithms practice

LookUp = [25,10,5,1]


# i.e. coin changing problem
def DP_MinCount(val, lookup):
    dp = [None]*(val+1)
    decision = [None]*(val+1)
    
    dp[0] = 0

    for i in range(1, val+1):
        solutions = []
        decisions = []
        for j in lookup:
            nextVal = i-j
            if nextVal < 0:
                solutions.append(float('inf'))
            else:
                solutions.append(dp[nextVal]+1)
            decisions.append(j)
        dp[i] = min(solutions)
        if dp[i] != None and dp[i] != float('inf'):
            decision[i] = decisions[solutions.index(dp[i])]

    return (dp, decision)

def TraverseDecisions(val, decision):
    toReturn = []
    currIndex = val
    while (decision[val] != None and currIndex > 0):
        toReturn.append(decision[currIndex])
        currIndex -= decision[currIndex]
    
    return toReturn

dp, decision = DP_MinCount(35, LookUp)
print(TraverseDecisions(35, decision))

print("initialized")