myFile = open ("SimpleData.csv", "r")

lines = myFile.readlines()[1: ]


lowestRateCounty = ""
lowestRate = 1.1  


#This loop will calculate each counties vax rate

for line in lines:
	line = line.strip()
	lineAsList = line.split(",")
	print(lineAsList)
	
	
	vaxRate = float(lineAsList[2]) / float(lineAsList[1])
	if vaxRate < lowestRate:
		lowestRateCounty = lineAsList[0]
		lowestRate = vaxRate
	
print(("the lowest rate is %0.2f in %s")% (lowestRate, lowestRateCounty))	
	
	
	#print("the vax rate for", lineAsList[0], "is", vaxRate)
	












##Lab warm up find average






























"""



highestRate = -1.0
highestRateCounty = ""

lines = myFile.readlines()[1: ]
#print(lines)


for line in lines:
	tempNumber = int(line.split(' , ')[2]) / int(line.split(' , ')[1])
	if tempNumber > highestRate :
		highestRate = tempNumber
		highestRateCounty = line.split(' , ')[0]



highestRate = str(round(highestRate *100,2))+ " % "

print("The county with the highest vaccination rate is %s, which is %s." % (highestRateCounty, highestRate))
"""
