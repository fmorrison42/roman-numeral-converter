"""
roman numeral converter to engic numerals
"""
# list all roman numerals and their engic equivalents
romanEquiv = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""
# ask for the roman numeral
romanInput = str(input("What is your roman number in question?")).upper()
#romanInput.upper()

# split up the roman numeral into individual strings
romanSplit = list(romanInput)


"""
for i in romanSplit
	- convert each list to its own individual string
	- compare the letter to it's counterpart and list them out
	- add each number together
	- output the final number

print (romanSplit)	
"""
engNumeral = 0
# run each letter against the roman numeral equivalent to add it to the final printout number
for i in romanSplit:
	# i.upper()
	# check to see which numeral matches
	if i == "M":
		engNumeral = engNumeral + 1000
	elif i == "D":
		engNumeral = engNumeral + 500
	elif i == "C":
		engNumeral = engNumeral + 100
	elif i == "L":
		engNumeral = engNumeral + 50
	elif i == "X":
		engNumeral = engNumeral + 10
	elif i == "V":
		engNumeral = engNumeral + 5
	elif i == "I":
		engNumeral = engNumeral + 1


print(engNumeral)