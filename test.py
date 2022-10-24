
"""
import string

myString = "Hello my name is Yujin Jung!"
new_string = myString.translate(str.maketrans('','',string.punctuation))

print(new_string)
"""


#punctuation = """'~!@#$%^&*(){}-_:;><?\/,."""
"""
myString = "Hello!!!! my name is Yujin Jung!"

no_punc = ""

for i in range(len(myString)):    #why for length? 
	myString[i] = myString[i].lower() #because for index?

	for char in myString:
		if char not in punctuation:
			no_punc = no_punc + char

print(no_punc)
# I don't know how to gather these two chunks

"""

#Version 3

lis = ["TIDFISs!","!SSf@","%%dfe^"]

def remove_punc(string):
	#punc= """'~!@#$%^&*(){}-_:;><?\/,."""
	for ele in string:
		if ele in punc:
			string = string.replace(ele, "")
	return string
def lower_case(string):
	
	for i in range(len(lis)):
		lis[i] = lis[i].lower()
		
lis =[remove_punc(i) for i in lis]
print(lower_case(lis))

"""
