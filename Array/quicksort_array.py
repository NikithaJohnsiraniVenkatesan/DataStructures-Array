#Quicksort

def sort(array):
    less = []
    equal = []
    great = []
    
    if len(array)>1:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                great.append(i)
        return sort(less) + equal + sort(great)
    else:
        return array

    
array = [2,45,1,56,7,6,3,2,1,4]
sort(array)