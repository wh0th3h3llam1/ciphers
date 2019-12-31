# Atbash Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
import platform


letters = "abcdefghijklmnopqrstuvwxyz"
reverse_letters = "zyxwvutsrqponmlkjihgfedcba"


def encrypt(strng):

	encrypted = ""

	for i in strng:
		if(ord(i) not in range(97,123)):
			encrypted += i
		else:
			# Find i in letter array
			pos = letters.find(i)
			encrypted += reverse_letters[pos]

	print("Encrypted String : " + encrypted)


def decrypt(strng):

	decrypted = ""

	for i in strng:
		if(ord(i) not in range(97,123)):
			decrypted += i
		else:
			# Find i in letter array
			pos = reverse_letters.find(i)
			decrypted += letters[pos]

	print("Decrypted String : " + decrypted)


def atbash_cipher():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tATBASH CIPHER")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			strng = input("Enter String to Encrypt : ")
			strng = strng.lower()
			print("----------------------------------------------------")
			encrypt(strng)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			strng = strng.lower()
			print("----------------------------------------------------")
			decrypt(strng)

		elif choice == 0:
			print("\t\tBYE.....")
			print("----------------------------------------------------")
			exit(0)

		else:
			# print("Invalid Choice, Try Again.")
			pass

		x = input()



if __name__ == '__main__':
	atbash_cipher()


#wh0am1
