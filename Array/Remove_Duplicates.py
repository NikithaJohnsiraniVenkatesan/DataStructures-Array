element = eval(input("Enter the input: "))
listofele = []

for i in element:
	if i not in listofele:
		listofele.append(i)

print("Results after removing duplicates: ", listofele)