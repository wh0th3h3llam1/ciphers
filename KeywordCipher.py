# Keyword Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
import platform


letters = "abcdefghijklmnopqrstuvwxyz"


def encrypt(strng, key):

	keyword = ""

	# To put key in encrypting keyword
	for k in key:
		if len(keyword) >= 26:
			break
		if k not in keyword:
			keyword += k

	# To remove duplicates from letters string.
	for i in letters:
		if len(keyword) >= 26:
			break
		if i not in key:
			keyword += i

	# print("Encrypting Letters : " + letters)
	# print("Encrypting Keyword : " + keyword)

	encrypted = ""
	for i in strng:
		if(ord(i) not in range(97,123)):
			encrypted += i
		else:
			# Find i in letter array
			pos = letters.find(i)
			encrypted += keyword[pos]

	print("Encrypted String : " + encrypted)


def decrypt(strng, key):

	keyword = ""

	# To put key in encrypting keyword
	for k in key:
		if len(keyword) >= 26:
			break
		if k not in keyword:
			keyword += k

	# To remove duplicates from letters string.
	for i in letters:
		if len(keyword) >= 26:
			break
		if i not in key:
			keyword += i

	decrypted = ""
	for i in strng:
		if(ord(i) not in range(97,123)):
			decrypted += i
		else:
			# Find i in letter array
			pos = keyword.find(i)
			decrypted += letters[pos]

	print("Decrypted String : " + decrypted)


def keyword_cipher():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tKEYWORD CIPHER")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			strng = input("Enter String to Encrypt : ")
			key = input("Enter Keyword : ")
			strng = strng.lower()
			key = key.lower()
			print("----------------------------------------------------")
			encrypt(strng, key)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			key = input("Enter Keyword : ")
			strng = strng.lower()
			key = key.lower()
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
	keyword_cipher()


#wh0am1
