def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)

print fact(5)

def sumn(n):
    if n ==1 :
        return 3
    return sumn(n-1) + 3

print sumn(5)

def pascal(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    previousline = pascal(n-1)
    newline = []
    newline.append(1)
    print previousline
    for i in range(len(previousline) -1):
        newline.append(previousline[i] + previousline[i+1])
    newline.append(1)
    return newline

print pascal(5)