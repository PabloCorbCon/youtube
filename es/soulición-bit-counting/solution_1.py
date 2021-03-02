def bit_counting(n):
	number = '{0:b}'.format(n)
	bits = 0
	for i in number:
		if i == '1':
			bits += 1
	return bits