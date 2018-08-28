def reverse_number(x):
    negative = False
    if x < 0:
        x = -x
        negative = True
    new_number = 0
    while x:
        curr = x%10
        new_number = new_number * 10 + curr
        x = x/10
    if negative:
        new_number = -new_number
    return new_number

print reverse_number(-123)

def max_area(height):
    max_so_far = 0
    max_index = 0
    for i, line in enumerate(height):
        area = line*i
        if area > max_so_far:
            max_so_far = area
            max_index = i
    return max_index