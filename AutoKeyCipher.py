# AutoKey Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
import platform


def encrypt(strng, key):

	enc = []
	p_t = []

	enc.append(int(key))

	for i in range(len(strng)):
		x = strng[i]
		p_t.append(int(ord(x) - 97))
		enc.append(int(ord(x) - 97))

	final = ""

	for i in range(len(strng)):
		y = (p_t[i] + enc[i]) % 26 + 97
		final += chr(y)

	print("Encrypted String : " + final)
	print("Key : " + str(enc))


def decrypt(strng, key):

	c_t = []

	for i in range(len(strng)):
		x = strng[i]
		c_t.append(int(ord(x) - 97))

	final = ""

	for i in range(len(strng)):
		y = (c_t[i] - key[i]) % 26 + 97
		final += chr(y)

	print("Decrypted String : " + final)


def autokey_cipher():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tAUTOKEY CIPHER")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			strng = input("Enter String to Encrypt : ")
			key = input("Enter Key : ")
			strng = strng.lower()
			key = key.lower()
			print("----------------------------------------------------")
			encrypt(strng, key)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			strng = strng.lower()
			key = list(map(int,input("Enter Key (Space Separated Values): ").split()))
			print("----------------------------------------------------")
			decrypt(strng, key)

		elif choice == 0:
			print("\t\tBYE.....")
			print("----------------------------------------------------")
			exit(0)

		else:
			# print("Invalid Choice, Try Again.")
			pass

		x = input()


if __name__ == '__main__':
	autokey_cipher()


#wh0am1
