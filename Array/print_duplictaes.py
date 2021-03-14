def findDuplicates(array, arraySize):
    ifPresent = False
    a1 = []
    for i in range(arraySize - 1):
        for j in range(i + 1, arraySize):
            if (array[i] == array[j]):
                if array[i] in a1:
                    break
                else:
                    a1.append(array[i])
                    ifPresent = True
    if (ifPresent):
        print(a1, end = " ")
    else:
        print("No duplicates present in arrays")
 
array = [1,2,2,2,3,4,5,5,5,5] 
arraySize = len(array)
 
findDuplicates(array, arraySize)