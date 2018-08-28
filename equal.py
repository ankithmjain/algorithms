rest = [0, 1, 1, 2, 2]

def subtract_count(a):
	count = a / 5
	return count + rest[a % 5]

print subtract_count(5)