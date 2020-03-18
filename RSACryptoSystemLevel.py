# RSA with 4 Levels of Encryption Using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import math
import secrets
import random


def gcd(a, b):
	if  a == 0:
		return b

	return gcd(b % a, a)


def phi_function(p):
	if p == 1:
		return 0

	ans = 1
	for i in range(2, p):
		if gcd(i, p) == 1:
			ans += 1
	return ans


def inverse(a, n):
	r1 = n
	r2 = a
	t1 = 0
	t2 = 1
	while r2 > 0:
		q = int(r1 / r2)
		r = r1 - (q * r2)
		t = t1 - (q * t2)
		r1 = r2
		r2 = r
		t1 = t2
		t2 = t

	if r1 == 1:
		t1 = t1 % n
		return t1


def rsa(n):

	phi_n = phi_function(n)

	# Generate a random number between 0 and phi_n
	while 1:
		while 1:
			e = secrets.randbelow(phi_n)
			if gcd(e, phi_n) != 1:
				pass
			elif e == (phi_n - 1):
				pass
			else:
				break

		d = inverse(e, phi_n)

		if d != e:
			break

	print("p : ", p)
	print("q : ", q)
	print("n = p * q : ", n)
	print("phi(n) : ", phi_n)
	print("e : ", e)
	print("d : ", d)
	print("Public Key : {0}, {1}".format(e, n))
	print("Private Key : {0}".format(d))

	public_key = [e, n]
	private_key = d

	return public_key, private_key


# Check if n is a prime number
def miller_rabin(n):

	# Function returns True is n is Prime
	# Function returns False is n is Composite

	if n == 2:
		return True

	if n % 2 == 0:
		return False

	m = x = n - 1
	k = 0

	while (m % 2 == 0):
		k += 1
		m /= 2
	m = int(m)
	T = int(pow(2, m) % n)

	if T == x:
		return True

	if T == 1 or T == -1:
		return True

	for _ in range(1, k):

		T = (T * T) % n
		if T == x:
			return True
		if T == 1:
			return False
		if T == -1:
			return True
	return False


def fastExponential(a, x, n):
	y = 1
	while x > 0:
		if x & 1:
			y = (a * y) % n
		a = (a * a) % n

		x //= 2

	return y


def generateNum(level='mid'):

	if level == 'low':
		return random.randrange(16, 32)

	if level == 'mid':
		return random.randrange(64, 128)

	if level == 'high':
		return random.randrange(512, 1024)

	if level == 'very high':
		return random.randrange(2048, 4096)


if __name__ == '__main__':

	enc_level = int(input("Enter Level of Encryption [Low=0, Mid=1, High=2, Very_High=3] : "))
	enc_level_list = ['low', 'mid', 'high', 'very high']
	level = enc_level_list[enc_level]
	print('Selected Level of Encryption : {0}'.format(enc_level_list[enc_level]))
	while 1:
		p = generateNum(level)
		q = generateNum(level)

		if miller_rabin(p) and miller_rabin(q):
			if p != q:
				break

	n = p * q

	public_key, private_key = rsa(n)

	while 1:
		strng = int(input("Enter String to Encrypt : "))
		if strng < n:
			break

		print("Input should be less than : ", n)

	y = fastExponential(strng, public_key[0], n)

	print("--------------------------------------------")
	print("Encrypted Message : ", y)

	z = fastExponential(y, private_key, n)

	print("Decrypted Message : ", z)
	print("--------------------------------------------")


#wh0am1
