myFile = open("randomValues.txt","r")
data = myFile.readlines()		
digit = []
letter = []
myResult = []
for line in data:
	lineAsList = line.split()
	
	for strings in lineAsList:
		try:
			strings.isdigit
			digit.append(int(strings))
		except ValueError:
			letter.append(strings)
			
digit = sorted(digit)



def minima(n,digit):
	if n <= 1:
		return digit[0]
	else:
		if digit[0] > minima(n-2,digit):
			return minima(n-2,digit)
		else:
			return digit[0]

		
print(minima(len(digit),digit))
	


def maxima(n,digit):
	if n <= 1:
		return digit[n-1]
	else:
		if digit[n-1] > maxima(n-2,digit):
			return digit[n-1]
		else:
			maxNum = maxima(n-2, digit)
			return maxNum

print(maxima(len(digit),digit))


#myData = [minima(len(digit),digit),maxima(len(digit),digit)]

#print(myData)

def extrema(digit,minNum = True , maxNum = True):
	if minNum == False:
		if maxNum == False:
			pass
		else:
			return maxima(len(digit),digit)
	else:
		return (minima(len(digit),digit),maxima(len(digit),digit))
	

print(extrema(myResult))	
print(extrema(myResult, False))
print(extrema(myResult, False, False))

