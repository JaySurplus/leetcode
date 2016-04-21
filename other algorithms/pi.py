#!/usr/bin/python
import math
def pi(n):
	a = 1.
	b = 1./2**0.5
	t = 1./4
	p = 1
	while n > 0:
		at ,bt,tt,pt = a , b ,t ,p
		a = (at + bt)/2
		b = math.sqrt(at*bt)
		t = tt - pt*(at-a)**2
		p = 2 *pt
		n -= 1
	return (a+b)**2/(4*t)

print pi(10)