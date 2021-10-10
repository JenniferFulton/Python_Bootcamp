# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for i in range(0,len(list)):
        if list[i] > 0:
            list[i] = "BIG"
        else:
            pass
    return list
print(biggie_size([2,-1,-4,6,7]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(_list):
    sum = 0
    for i in range(0,len(_list)):
        if _list[i] > 0:
            sum +=1
        else:
            pass
    _list[len(_list)-1] = sum 
    return _list
print(count_positives([-1,2,3,4,-5,6]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list_):
    sum = 0
    for i in range(0,len(list_)):
        sum = sum + list_[i]
    return sum
print(sum_total([1,2,4,7,3,-6]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum = 0
    for i in range(0,len(list)):
        sum = sum + list[i]
    average = sum / len(list)
    return average
print(average([1,2,4,7,3,-5]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    if len(list) == 0:
        return False
    else:
        return len(list)
print(length([1,6,3,8,9,10]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def mini(list):
    if len(list) == 0:
        return False
    else:
        for i in range(0,len(list)):
            if list[i] <= list[0]:
                minimum = list[i]
            else:
                pass
    return minimum
print(mini([]))
print(mini([-5,7,-6,3,0,10]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def max(list):
    if len(list) == 0:
        return False
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum

print(max([]))
print(max([-5,7,100,3,300,10]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

dictionary = {}
def ultimate_analysis(ultimate_list):
    dictionary["SumTotal :"] = sum_total(ultimate_list)
    dictionary["Average: "] = average(ultimate_list)
    dictionary["Minimum: "] = mini(ultimate_list)
    dictionary["Maximim: "] = max(ultimate_list)
    dictionary["Length: "] = length(ultimate_list)
    return dictionary

print(ultimate_analysis([37,2,1,-9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
