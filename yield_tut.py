def fib(n):
    curr = 1
    prev = 1
    yield 1
    while n >0:
        yield curr
        next = curr + prev
        prev = curr
        curr = next
        n += -1


for i in fib(7):
    print i