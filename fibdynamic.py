# Python program for Memoized version of nth Fibonacci number

# Function to calculate nth Fibonacci number
def fib(n, lookup):
    print "printing n and lookup {} {}".format(n, lookup)
    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n

	# If the value is not calculated previously then calculate it
	if lookup[n] is None:
		lookup[n] = fib(n-1 , lookup) + fib(n-2 , lookup)
    # return the value corresponding to that value of n
    return lookup[n]
# end of function

# Driver program to test the above function
def main():
	n = 34
	# Declaration of lookup table
	# Handles till n = 100
	lookup = [None]*(n+1)
	print "Fibonacci Number is ", fib(n, lookup)

def fibdun(n):
    if n in [0, 1]:
        return n
    fib_list = [0, 1]
    i = 1
    while len(fib_list) < n+1:
        print fib_list
        next = fib_list[i] + fib_list[i-1]
        fib_list.append(next)
        i +=1
    return fib_list[n-1]

print fibdun(6)
if __name__=="__main__":
	main()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
