#!/usr/bin/python

import sys
import random

num = int(sys.argv[1])

def RM1(n,s,h):
	# Returns True if num is a prime number.

	for trials in range(5): # try to falsify num's primality 5 times
		a = random.randrange(2, n - 1)
		v = pow(a, s, n)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (n - 1):
				if i == h - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % n
	return True

def RM2(n,s,h):
	# Returns how many a's in {2,...,n-1} are good witnesses of
	# being composite (only run this for composites)

	w = 0 # number of good witnesses

	for a in range(2,n): # check all witnesses in {2,...,n-1}
		v = pow(a, s, n)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (n - 1): # n-1 is -1 mod n
				if i == h - 1:
					w += 1
					break
				else:
					i = i + 1
					v = (v ** 2) % n
	return w

def sh(n):
	# compute the s,h value so that n-1=s*2^h where s is odd
	s = n - 1
	h = 0
	while s % 2 == 0:
		# keep halving s while it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		h += 1
	return s,h

print("Composite \t\t Witnesses")
for n in range (5,num,2):
	s,h = sh(n)
	if (not RM1(n,s,h)):
		print(n, "\t\t\t", RM2(n,s,h))
