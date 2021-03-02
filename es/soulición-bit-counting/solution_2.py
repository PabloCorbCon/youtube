def bit_counting(n):
	return len(list(filter(lambda y: y=='1', '{0:b}'.format(n))))