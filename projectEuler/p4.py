def pd(n):
	"""
	:type n: number of product length
	"""
	maxRes = maxI = maxJ = 0 
	i = 10**n-1

	while i > 10**(n-1):
		j = 990
		while j > 10**(n-1):
			p = i * j
			if p > maxRes:
				pString = str(p)
				if pString == pString[::-1]:
					maxRes = p
					maxI = i
					maxJ = j
			j -= 11
		i -= 1
	return maxRes , maxI , maxJ
print pd(3)