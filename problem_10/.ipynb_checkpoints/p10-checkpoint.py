'''
Find the sum of all the primes below two million.

Current method being tried:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
+
A composite number cant have a prime factor greater than its
square root

'''

import numpy as np
from numba import jit, njit, prange

@njit
def eratos(max = 2e6):

	# we use 'max - 1' for arrays because 1 isnt 
	# going to be a prime
	# This consequently means that when assigning
	# numbers to arrays, we need to specify the position
	# as 'number - 2', because of 0 indexing and starting
	# from the number 2
	# For example, the number 2 is referenced as array[0]
	max = float(max)

	is_prime = np.ones(int(max-1))
	primes = np.zeros(int(max-1)) #initialize empty array
	primes[0] = 2.0 #first prime is 2

	for i in prange(3, max, 2):
		if is_prime[i-2] == 1:
			primes[i-2] = i

			for j in prange(i*i, max, i):
				is_prime[j-2] = 0

	return(np.sum(primes))