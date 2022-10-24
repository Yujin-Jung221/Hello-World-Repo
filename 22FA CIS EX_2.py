# List 1
# at least Three different ways to create a list containing 100 zeros

"""

def ZeroMaker(n):
	#listOfZeros1 = []
	listOfZeros1 = [0]*n
	return listOfZeros1
print(ZeroMaker(100))		


listOfZeros = []
for i in range(0,100):
	listOfZeros.append(0)
print(listOfZeros)


import itertools
zeroList = list(itertools.repeat(0,100))
print(zeroList)
"""	


# List 2
# add 3 to every number in a list

myListOfNumbers = [1,2,3,4,5]
result = []
for num in myListOfNumbers:
	result.append(num+3)
print(result)

"""

myListOfNumbers = [1,2,3,4,5]
result = [num+3 for num in myListOfNumbers]
print(result)

"""


# List 3
# removes all the even numbers out of a list

"""

myList = [1,2,3,4,5,6]
for num in myList:
	if num % 2 == 0:
		myList.remove(num)	
print(myList)

"""

# List 4
# removes all the odd numbers out of a list

# Type 1
"""

myList = [1,2,3,4,5,6,7]
for num in myList:
	if num % 2 != 0:
		myList.remove(num)
print(myList)

"""

"""

myList = []

listNumber = int(input("Enter the total list items = "))
for i in range(1, listNumber +1 ):
	listValue = int(input("Enter the %d list item = "%i))
	myList.append(listValue)

print(myList)

i = 0
while(i < len(myList)):
	if (myList[i]%2 == 0):
		myList.remove(myList[i])
	i = i+1  #why?
print(myList)

"""

# List 5
# what is the value of list1[2]?

"""
List1 = [1,3,5,7]
List2 = List1
List2[2] = 10
print(List1[2])

"""

# List 6
# what is difference between list and tuple?
# list is mutable, tuple is immutable

# List 7 (page 196)
# replace each number with absolute value in list

"""

myList = [1,-1,-2.2,-3,-4.3,-5]

result = []
for num in myList:
	if num > 0:
		result = list(map(abs, myList))
print(result)

"""


"""

myList = [1,-1,-2.2,-3,-4.3,-5]
result = []

for num in myList:
	if num < 0:
		x = num * -1
		result.append(x)
print(result)		

"""



# List 8
# function takes list and integer as argument
# shift content of list to right by integer amount
# ex) [a,b,c,d,e,f,g] integer 2
# → [f,g,a,b,c,d,e]



def rotate(n):
	#if len(myList) == 0:
		#return myList
	#n = n % len(myList)
	return myList[-n:] + myList[:-n]
	
myList = ['a','b','c','d','e','f','g']
n = 3

print(rotate(n))



# List 9
# make a list of words in a sentence
# no punctuation "hello!" → "hello"
# should distinguish capital and lowercase


punctuation = """'~!@#$%^&*(){}-_:;><?\/,."""

"""

x = "SFDF!@$$"
x = x.lower()

emptyList = []

for i in punctuation:
	x = x.replace(i,' ')

emptyList.append(x)

print(emptyList)

"""


# List 10
# make a list of words in a sentence
# no punctuation "hello!" → "hello"
# should "not" distinguish capital and lowercase


#punctuation = """'~!@#$%^&*(){}-_:;><?\/,."""

"""

for i in punctuation:
	x = x.replace(i,'')

emptyList.append(x)

print(emptyList)

"""


# List 11
# print all words from speech
# Address at Rice University on the Nation's space effort
# Print just Unique words
"""

speech_file = open("speech.txt","r")
lines = speech_file.readlines()


print(lines)

"""

# Dictionary 1
# myDict = {"a" : 10, "b" : 30, "c" : 20}
# a) the value associate with "b"
#b) the key associate with 20

myDict = {"a" : 10, "b" : 30, "c" : 20}

print(myDict.get("b"))

for key, val in myDict.items():
	if val == 20:
		print(key)



"""
# Dictionary 2
# myDict2 = {90:"A", 80:"B", 70:"C"}


# a) the keys



myDict2 = {90:"A", 80:"B", 70:"C"}
for key in myDict2.keys():
	print(key, end = ' ')


myDict2 = {90:"A", 80:"B", 70:"C"}
print(myDict2.keys())

# b) the values



myDict2 = {90:"A", 80:"B", 70:"C"}
for val in myDict2.values():
	print(val, end = ' ')	



# c) the key value pairs



myDict2 = {90:"A", 80:"B", 70:"C"}
for key, value in myDict.items():
	print(key, value)




# d) the key value pairs in ascending order based on key



myDict2 = {90:"A", 80:"B", 70:"C"}

sorted_dict = sorted(myDict2.items()) #Tuple
print("key value asceding",sorted_dict)


#TUPLE PAIR FOR LIST
print(myDict2.items())


#PRINT AS LIST DESCENDING
sorted_desc_dict = sorted(myDict2.keys(), reverse = True)
print("key value descending",sorted_desc_dict)




# e) the key value pairs in ascending order based on value


		
myDict3 = {90: 1, 80: 2, 70: 3}
sorted_values = sorted(myDict3.values())
sortedDic3 = {}

for i in sorted_values:
	for j in myDict3.keys():
		if myDict3[j] == i:
			sortedDic3[j] = myDict3[j]

print("based on value in ascending",sortedDic3.items())


# Dictionary 3
# the amount of times each word appears



myFile = open("speech.txt","r")
word_dict = {}

#loop through each line of the file
for line in myFile:
	#remove leading spaces and new line character
	line = line.strip()
	
	#convert the characters in line to
	#lowercase to avoid case mismatch
	line = line.lower()
	
	#split the line into words
	words = line.split(" ")
	
	#iterate over each word in line
	for word in words:
		#check if the words is already in dictionary
		if word in word_dict:
			#increment count of word by 1
			word_dict[word] = word_dict[word]+1
			
		else:
			#add the word to dictionary with count 1
			word_dict[word] = 1
#print the contents of dictionary

for key in list(word_dict.keys()):
	print(key, ":", word_dict[key])



# dinner

myFile = open("DinnerData.txt","r")
dinner_amount = []
theSum = 0
for line in myFile:
	lineAsList = line.split(" ")
	dinner_amount.append(int(lineAsList[1]))
	
for i in dinner_amount:
	theSum += i

outFile = open("out.txt","w")
outFile.write("output is" + str(theSum))

outFile.close()	
"""
		
	
	
