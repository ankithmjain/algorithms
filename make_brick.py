def firstDuplicate(a):
    num_dict = {i:0 for i in range(1, len(a))}
    #print num_dict
    for num in a:
        num_dict[num] +=1
        #print num_dict
        if num_dict[num] >= 2:
            return num
    return -1

print firstDuplicate([2, 3, 3, 1, 5, 2])

def firstNotRepeatingCharacter(s):
    chardict = {i:0 for i in s}
    for char in s:
        chardict[char] += 1
    for character in s:
        if chardict[character] >=2:
            continue
        else:
            return character
    return '_'

print firstNotRepeatingCharacter("abacabad")

def rotateImage(a):
    for i in range(0, len(a)/2):
        a[i], a[-1-i] = a[-1-i], a[i]
    print a
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j], a[j][i] = a [j][i], a[i][j]
    print a

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
rotateImage(a)

import collections
def groupingDishes(dishes):
    d = collections.OrderedDict()
    dish_dict = {}
    for dish in dishes:
        dish_name = dish.pop(0)
        for incredients in dish:
            if dish_dict.get(incredients) is None:
                dish_dict[incredients] = [dish_name]
            else:
                dish_dict[incredients].append(dish_name)
    print dish_dict
    mylist = []
    dish_incredients = sorted(dish_dict.keys())
    for incredient in dish_incredients:
        d[incredient] = dish_dict[incredient]
    for i in d:
        if len(d[i]) >=2:
            row = [i]
            row.extend(d[i])
            mylist.append(row)
    return mylist

dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]

print groupingDishes(dishes)