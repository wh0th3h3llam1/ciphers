# RailFence Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import math
import os
import platform
import random
import string


def encrypt(strng, rails):

	strng = strng.replace(" ", "")

	len_enc = math.ceil(len(strng) / rails)

	w, h = len_enc, rails

	encrypted = [[0 for x in range(w)] for y in range(h)]

	count = 0
	for i in range(len_enc):
		for h in range(rails):
			if count < len(strng):
				encrypted[h][i] = strng[count]
				count += 1

	for _ in range(h, rails):
		encrypted[h][i] = random.choice(string.ascii_lowercase)

	print("Encrypted Message : ", end="")
	for i in range(h+1):
		for j in range(w):
			print(encrypted[i][j], end="")


def decrypt(strng, rails):

	strng = strng.replace(" ", "")

	len_dec = int(len(strng) / rails)

	w, h = len_dec, rails

	decrypted = [[0 for x in range(w)] for y in range(h)]

	count = 0
	for i in range(rails):
		for j in range(len_dec):
			if count < len(strng):
				decrypted[i][j] = strng[count]
				count += 1

	print("Decrypted Message : ", end="")
	for i in range(w):
		for j in range(h):
			print(decrypted[j][i], end="")


def rail_fence():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tRAILFENCE CIPHER")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			strng = input("Enter String to Encrypt : ")
			rails = int(input("Enter No. of Rails : "))
			strng = strng.lower()
			print("----------------------------------------------------")
			encrypt(strng, rails)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			rails = int(input("Enter No. of Rails : "))
			print("----------------------------------------------------")
			decrypt(strng, rails)

		elif choice == 0:
			print("BYE...")
			print("----------------------------------------------------")
			exit(0)

		else:
			# print("Invalid Choice, Try Again.")
			pass

		x = input()



if __name__ == '__main__':
	rail_fence()
