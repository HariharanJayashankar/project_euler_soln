'''
Find a triplet (a, b, c)
[a, b, c are natural numbers]

such that:

i)	a^2 + b^2 = c^2
ii) a + b + c = 1000

'''

import numpy as np

for a in range(1, 1000):
	for b in range(a+1, 1000-a):
		c = 1000 - b - a
		if a**2 + b**2 == c**2:
			print('The triple:', a, b, c)
			print('The product:', a * b * c)
			break
