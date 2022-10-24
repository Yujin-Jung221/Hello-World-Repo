groceryList = []
costOfItem = []

# STEP 1
# Use while loop to make each list to get user input

while True:
	
	itemName = input("Enter your groceryList item: ")
	if itemName == "DONE":
		break
	
	else:
		itemName not in groceryList
		groceryList.append(itemName)
	
	itemCost = int(input("Enter greceryList Cost in Dollars : "))
	if itemCost not in costOfItem:
		costOfItem.append(itemCost)

	
print("My grocery list is ", groceryList)
print("Cost for each item ", costOfItem)


# STEP 2
# Creat dictionary as pair

dataDict = {}
for key in groceryList:
	for value in costOfItem:
		dataDict[key] = value
		#costOfItem.remove(value)
		break
print(dataDict)


# STEP 3
# Calculate total amount for grocery shopping

totalCost = 0
for cost in costOfItem:
	totalCost += int(cost)

print("Total amount spent on grocery shopping is : ", totalCost)

# STEP 4
# Make second dictionary about grocery purchase.

myDict = {'banana' : 2, 'grape':6,'apple':5}

dataDict_len = len(dataDict)


def findSamePair(dataDict,myDict):
	samePair = {}
	for key,val in dataDict.items():
		for keys,values in myDict.items():
			if key in myDict.keys():
				samePair[key] = dataDict[key]
		
				
print(findSamePair(dataDict,myDict))
				
