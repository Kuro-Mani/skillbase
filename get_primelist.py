def get_primelist(upper):
	result = []
	for cp in range ( 2, upper + 1 ):
		for i in range ( 2, cp ):
			if ( cp % i == 0 ):
				break
		else:
			result.append(cp)
	return result
mathint = input('int only::')
upper = int(mathint)
print(get_primelist(upper))
print(len(get_primelist(upper)))