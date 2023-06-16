def flatten_an_array(array):
	res = []
	for i in array:
		if type(i) == list:
			res.extend(flatten_an_array(i))
		else:
			res.append(i)
	return res




exampleArray = [1,2,[3,4, [5,6,7,[5,6,[5,6,7],7]], 8], 9, 10]
print(flatten_an_array(exampleArray))