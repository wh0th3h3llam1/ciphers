# Knapsack Cryptosystem Using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import math
import secrets
import random


def co_primes(n1, n2):
	if (n1 == 0 or n2 == 0):
		return 0

	if (n1 == n2):
		return n1

	if (n1 > n2):
		return co_primes(n1 - n2, n2)

	return co_primes(n1, n2 - n1)


def generateNum():

	return random.randrange(10, 100)


def generate_super_increasing_vector():
	setA = set()

	return setA

def knapsack():

	# Message is of 8 bits
	tuple_A = tuple(map(int, input("Enter Super Increasing Vector : ").split()))

	q = int(input("Enter q : "))
	r = int(input("Enter r : "))

	B = list()

	for i in range(len(tuple_A)):
		x = (tuple_A[i] * r) % q
		B.append(x)

	public_key = B
	private_key = [tuple_A, q, r]

	return public_key, private_key


def extended_euclidean(a, n):
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


def encrpyt(B):
	pt = int(input("Plain Text : "))
	b = bin(pt)[2:]
	ct = 0
	for i in range(len(b)):
		if b[i] == '1':
			ct += B[i]

	print("Cipher Text : {0}".format(ct))


def decrpyt():
	ct = int(input("Cipher Text : "))
	tuple_A = tuple(map(int, input("Enter Super Increasing Vector : ").split()))
	q = int(input("Enter q : "))
	r = int(input("Enter r : "))

	r_inv = extended_euclidean(r, q)

	c_new = (ct * r_inv) % q

	pt = [None] * len(tuple_A)

	for i in range(len(tuple_A) - 1, -1, -1):
		if c_new >= tuple_A[i]:
			pt[i] = 1
			c_new -= tuple_A[i]
		else:
			pt[i] = 0

	temp = ""
	temp += ''.join(str(e) for e in pt)

	plain_text = int(temp, 2)

	print("Plain Text : {0}".format(plain_text))


if __name__ == '__main__':

	public_key, private_key = knapsack()

	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tKNAPSACK CRYPTOSYSTEM")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			encrpyt(public_key)

		elif choice == 2:
			decrypt()

		elif choice == 0:
			print("\t\tBYE.....")
			print("----------------------------------------------------")
			exit(0)

		else:
			# print("Invalid Choice, Try Again.")
			pass

		x = input()


