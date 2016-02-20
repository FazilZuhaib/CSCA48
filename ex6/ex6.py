def rsum(input_list):
	'''(list) -> int
	Returns the sum of all the elements in the list
	'''
	if len(input_list) == 1:
		if isinstance(input_list[0], list):
			result = rsum(input_list[0])
		else:
			result = input_list[0]
	else:
		curr = input_list[0]
		first = rsum(input_list[1:])
		if isinstance(curr, list):
			curr = rsum(curr)
		result = first + curr
	return result

thing = [[1,1], []]
s = rsum(thing)
print(s)