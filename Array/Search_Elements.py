arraylist = eval(input("Enter the array of numbers: "))

searchindex = int(input(" Enter number to find the index of it: "))

for i in range(1, len(arraylist), 1):
	if int(searchindex) == arraylist[i]:
		print("The number is stored at index: ", i)