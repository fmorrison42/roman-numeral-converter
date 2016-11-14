
# list all roman numerals and their engic equivalents
romanEquiv = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


def romanConvert():
	#ask for the roman string
	romanInput = str(input("What is your roman number in question?")).upper()

	romanSplit = list(romanInput)

	engNumeral = 0
	# run each letter against the roman numeral equivalent to add it to the final printout number
	for i in romanSplit:
		print(i)
		if i in romanEquiv:
			engNumeral = engNumeral + romanEquiv[i]

	# check to see which numeral matches
	"""
	keeping this to show the change from many lines to just a few using loops
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
"""

	print(engNumeral)

romanConvert()	