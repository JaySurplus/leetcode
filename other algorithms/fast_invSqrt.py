#!/usr/bin/python

def invSqrt(num):
	xhalf = 0.5*num
	y = num
	
	i = 0x5f3759df - (num>>1)
	num = num * (1.5 - xhalf * num *num)
	return num
print invSqrt(4)