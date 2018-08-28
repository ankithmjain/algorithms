def climbingStairs(n):
    if n == 1 or n == 2:
        return n
    first = 1
    second = 2
    for i in range(2, n):
        temp = second
        curr = first + second
        second = curr
        first = temp
    return curr

print climbingStairs(5)