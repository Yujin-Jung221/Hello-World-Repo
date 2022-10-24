# Loop ex 1
# print each value using two types of for loop
"""
myList = [4,3,8,4,9]

for i in myList:
	print(i, end = ' ')


for i in range(len(myList)):
	print(myList[i],end = ' ')
	
"""

# Loop ex 2
"""
name1 = "Mahlet"
vowels = "aeiou"
result = []

for char in name1:
	if char in vowels:
		char = "*"
	print(char) 

ans = ""
vowels = ["a","e","i","o","u"]
for i in name1:
	if i in vowels:
		ans += "*"
	else:
		ans += i

print(ans)



#
word = "Programming"
print(word[4:7])





# Reverse string
myS = "Abebe"
print(myS[ : : -1])


"""
"""
#
myList = [1,4.6,"hey"]

for i in range(len(myList)):
	myList[i] = str(myList[i])
	
"""
names = ["Jake", "Abby", "Matt", "Jake", "Mahlet", "Abby","Jake"]

count_name = {}

for key in names:
	if key not in count_name:
		count_name[key] = 1
	else:
		count_name[key] += 1

print(count_name.items())

	
