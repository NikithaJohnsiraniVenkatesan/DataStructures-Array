#How do you find the largest and smallest number in an unsorted integer array?

#Use sort function to sort the input array
#Then using the position we can print the smallest and largest number

def FindLength(lst):
    LengthofList = len(lst)
    lst.sort()
    print("The largest element is: ", lst[LengthofList -1])
    print("The smallest element is: ", lst[0])
    print("The second largest element is: ", lst[LengthofList-2])
    print("The second smallest element is: ", lst[1])
    
lst = eval(input("enter the list of numbers: "))
FindLength(lst)