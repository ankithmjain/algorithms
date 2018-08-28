import sys
def minCost(cost, m, n):
    print m,n
    if m==0 and n ==0:
        return cost[m][n]
    if m ==0 or n ==0:
        return sys.maxint
    return min(minCost(cost, m-1, n-1), minCost(cost, m-1, n), minCost(cost, m, n-1)) + cost[m][n]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]


print(minCost(cost, 2, 2))