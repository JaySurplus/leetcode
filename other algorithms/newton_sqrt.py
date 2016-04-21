#!/usr/bin/python
import math
def newton_sqrt(num):
	res = num
	while True:
		last = res
		res = (res + 1.0*num/res)/2
		if abs(res - last) < 0.00000001:
			return res
print newton_sqrt(123134)
