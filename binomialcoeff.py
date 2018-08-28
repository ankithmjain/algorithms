def binomialCoeff(n, k):
    if k ==0 or n==k:
        return 1
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

n = 5
k = 2
print "Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k))