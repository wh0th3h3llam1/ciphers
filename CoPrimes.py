# Find if two given numbers are co-prime
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import math
import os
import platform
import random
import string



def co_primes(n1, n2):
	if (n1 == 0 or n2 == 0):
		return 0

	if (n1 == n2):
		return n1

	if (n1 > n2):
		return co_primes(n1 - n2, n2)

	return co_primes(n1, n2 - n1)


def main():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tCo-Primes")
		print("****************************************************")
		print("---------------------------------------")
		print("Find If Two Given Numbers are Co-Prime.")
		print("---------------------------------------")
		n1 = int(input("Enter First Number : "))
		n2 = int(input("Enter Second Number : "))
		print("---------------------------------------")
		if ( co_primes(n1, n2) == 1 ):
			print("Co-Prime")
		else:
			print("Not Co-Prime")

		x = input()


if __name__ == '__main__':
	main()
