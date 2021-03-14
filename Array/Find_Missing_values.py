# How do you find the missing number in a given integer array of 1 to 100?

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

lst = eval(input("Enter the array of numbers: "))
print("The missing numbers in the array are: ", find_missing(lst))