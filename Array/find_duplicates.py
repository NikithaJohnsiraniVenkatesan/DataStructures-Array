# How do you find the duplicate number on a given integer array?  
#Traverse the array once. 
#While traversing, keep track of count of all elements in the array using a temp array count[] of size n,
#when you see an element whose count is already set, print it as duplicate.
# This method uses the range given in the question to restrict the size of count[], 
#but doesn’t use the data that there are only two repeating elements. 


def findduplicate(arr, arraysize):
    count = [0] * arraysize
    print("Repeating numbers are: ", end = " ")
    for i in range(0, arraysize):
        if(count[arr[i]] == 1):
            print([arr[i]], end = " ")
        else:
            count[arr[i]] = count[arr[i]]+1


arr = [2,2,3,4,5,6,6]
arraysize = len(arr)
findduplicate(arr, arraysize)