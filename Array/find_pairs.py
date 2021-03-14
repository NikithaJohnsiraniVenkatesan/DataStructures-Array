#How do you find all pairs of an integer array whose sum is equal to a given number?


#traverse each element in the array
#Check if theres another number whoch can be added to produce the GS

def findPairs(arr, n, sum):
    print("The pairs which gives the sum of given number is/ are:")
    for i in range(0,n):
        for j in range(i+1, n):
            if(arr[i]+arr[j] == sum):
                print("(", arr[i], ",", arr[j], ")", sep="")

arr = eval(input("Enter the number of arrays: "))
n= len(arr)

sum = int(input("Enter the number: "))
findPairs(arr, n, sum)