"""
# Translate while loop to for loop


count = 10
while count <= 50:
	count += 1
	print(count)
	
	
count = 10
for i in range (10 , 51):
	count += 1
	print(count)	
"""
"""

#print user name with Hello


firstName = str(input("Enter your first Name : "))
lastName = str(input("Enter your last Name : "))
print("Hello",firstName, lastName)

"""

"""
# Volume of a cylinder

height = float(input("Enter the cylinder height: "))
radius = float(input("Enter the cylinder radius: "))
pi = 3.14

volume = (radius ** 2)*height*pi

print(volume)

"""

"""

# Resting heart rate


userAge = int(input("Enter your Age: "))
athletGoal = str(input("Enter your athleticism goal: "))


if athletGoal == "Above Average":
	if userAge >= 60 and userAge <= 79:
		print("Your resting heart rate should be between 45-70." )
	
	elif userAge >= 40 and userAge <= 59:
		print("Your resting heart rate should be between 46-71.")
	
	elif userAge >= 20 and userAge <= 39:
		print("Your resting heart rate should be between 47-72.")


if athletGoal == "Below Average":
	if userAge >= 60 and userAge <= 79:
		print("Your resting heart rate should be between 71-97." )
	
	elif userAge >= 40 and userAge <= 59:
		print("Your resting heart rate should be between 72-94.")
	
	elif userAge >= 20 and userAge <= 39:
		print("Your resting heart rate should be between 73-93.")	
"""

"""
#pyramid 1
for i in range( 1,6 ):
	for j in range(1, i+1):
		print(j, end = ' ')
		
	print(' ')

"""


"""
#pyramid 2
for i in range( 4 ):
	i += 1
	for j in range (i):
		print("*" ,end = ' ')
	print(' ')

"""


"""
#Horizontal triangle

for i in range (5):
	i += 1
	for j in range (i):
		print("*", end= ' ')
	print(' ')

for i in range (1, 5):
	for j in range (5 - i):
		print(j, end = ' ')
	print(' ')
	
"""


"""
# odd pyramid

for i in range (1,10):
	if i % 2 == 1:
		i += 1
		for j in range (1, i):
			print (j, end = ' ')
		print(' ')
"""

"""
# Alphabet pyramid 2

for i in range(65,70):
	for j in range (65, i+1):
		print(chr(i),end = ' ')
	print()
		
	
	#explain	
for i in range (1,5):
	for j in range (1, i+1):
		print(i,end = ' ')
	print()

"""

"""
# Alphabet pyramid 1

a= 65
for i in range(0,5):
	for j in range(0,i+1):
		print(chr(a),end=' ')
		a = a+1
	print()

	#explain
a= 1
for i in range(0,5):
	for j in range (0,i+1):
		print(a, end = ' ')
		a += 1
	print()

"""

		
		


"""
#supplementary pyramid 1(difficult)
for i in range (1, 6):
	for j in range (1, 6):
		if j > 6 - (i + 1):
			print(j - (6 - (i + 1)), end = " ")
		else:
			print(" ", end = " ")
	print(' ')
"""

"""
for i in range(1,11):
	for j in range (1,i+1):
		print(j,end=' ')
	print()
"""
"""
for i in range(1,51):
	if i % 2 == 0:
		print(i)
"""
"""
theSum = 0
for number in range(4,10):
	theSum += number
	print(number)
"""
	
number = 0
theSum = 0

while number < 10:
	
	
	print(number)


























