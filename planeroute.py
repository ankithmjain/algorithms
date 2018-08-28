'''
input:  route = [ [0,   2, 10], --- 10
                  [3,   5,  0], 10  20
                  [9,  20,  6], 4   14
                  [10, 12, 15], -5   5
                  [10, 10, 20] ] -10 0
output: 10                 

sorted(route)


'''
route = [[0, 2, 10],
         [3, 5, 0],#10
         [9, 20, 6],
         [10, 12, 15],
         [10, 10, 20]]
def calcDroneMinEnergy(route):
    fuel = 0
    min_fuel = 0
    fuel_needed = 0
    previous_point = route.pop(0)
    for point in route:
        diff = previous_point[2] - point[2]
        fuel += diff
        print point[2], diff, fuel
        if fuel < 0:
            fuel_needed += fuel
            fuel = 0
        previous_point = point
    fuel_needed = 0 if fuel_needed > 0 else fuel_needed
    print fuel, abs(fuel_needed)
    pass  # your code goes here


calcDroneMinEnergy(route)