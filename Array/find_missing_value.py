# the program finds one missing number in the given array in ascending order
def getMissingNumber(lst):
    n = len(lst)
    total = (n + 1)*(n + 2)/2
    sum_of_list = sum(lst)
    return total - sum_of_list
 
lst = eval(input("Enter the array: "))

missing_number = getMissingNumber(lst)
print(missing_number)