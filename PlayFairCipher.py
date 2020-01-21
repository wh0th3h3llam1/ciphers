# PlayFair Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import os
import platform



def find_key_matrix(key):
	key = key.upper()
	result=list()
	flag = k = 0

	# Storing Key
	for c in key:
		if c not in result:
			if c == 'J':
				result.append('I')
			else:
				result.append(c)

	# Storing Other Characters
	for i in range(65,91):
		if chr(i) not in result:
			if i == 73 and chr(74) not in result:
				result.append("I")
				flag=1
			elif flag == 0 and i == 73 or i == 74:
				pass
			else:
				result.append(chr(i))


	e_m = [[0 for _ in range(5)] for _ in range(5)]

	# Making Matrix
	for i in range(5):
		for j in range(5):
			e_m[i][j] = result[k]
			k += 1
	return e_m


def find_local_index(char, matrix):
	location = list()
	if char == 'J':
		char = 'I'

	for i ,j in enumerate(matrix):
		for k,l in enumerate(j):
			if char == l:
				location.append(i)
				location.append(k)
				return location


def encrypt(strng, key):

	# Create Key Matrix as per given key
	matrix = find_key_matrix(key)

	# Making Pairs of Two letters
	for s in range(0, len(strng) + 1, 2):
		if s < len(strng) - 1:
			if strng[s] == strng[s + 1]:
				strng = strng[:s + 1] + 'X' + strng[s + 1:]

	if len(strng) % 2 != 0:
		strng = strng[:] + 'X'
	i = 0
	print("Encrypted Text : ", end="")
	# Finding Position of the Characters in the encrypting matrix
	for i in range(0, len(strng), 2):
		x = strng[i]
		y = strng[i + 1]
		pos_x = find_local_index(x, matrix)
		pos_y = find_local_index(y, matrix)

		# print("Position of x : " + str(pos_x))
		# print("Position of y : " + str(pos_y))

		if pos_x[0] == pos_y[0]:
			# Both characters are in same row
			print("{}{}".format(matrix[pos_x[0]][(pos_x[1] + 1) % 5], matrix[pos_y[0]][(pos_y[1] + 1) % 5]), end=' ')

		elif pos_x[1] == pos_y[1]:
			# Both characters are in same column
			print("{}{}".format(matrix[(pos_x[0] + 1) % 5][pos_x[1]], matrix[(pos_y[0] + 1) % 5][pos_y[1]]), end=' ')

		else:
			# Both characters are not in same row or column
			print("{}{}".format(matrix[pos_x[0]][pos_y[1]], matrix[pos_y[0]][pos_x[1]]), end=' ')


def decrypt(strng, key):
	matrix = find_key_matrix(key)
	i = 0
	print("Decrypted Text : ", end="")
	for i in range(0, len(strng), 2):
		x = strng[i]
		y = strng[i + 1]
		pos_x = find_local_index(x, matrix)
		pos_y = find_local_index(y, matrix)

		if pos_x[0] == pos_y[0]:
			# Both characters are in same row
			print("{}{}".format(matrix[pos_x[0]][(pos_x[1] - 1) % 5], matrix[pos_y[0]][(pos_y[1] - 1) % 5]), end=' ')

		elif pos_x[1] == pos_y[1]:
			# Both characters are in same column
			print("{}{}".format(matrix[(pos_x[0] - 1) % 5][pos_x[1]], matrix[(pos_y[0] - 1) % 5][pos_y[1]]), end=' ')

		else:
			# Both characters are not in same row or column
			print("{}{}".format(matrix[pos_x[0]][pos_y[1]], matrix[pos_y[0]][pos_x[1]]), end=' ')



def playfair_cipher():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\t\tPLAYFAIR CIPHER")
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
			strng = strng.upper()
			strng = strng.replace(" ", "")
			key = key.upper()
			print("----------------------------------------------------")
			encrypt(strng, key)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			strng = strng.upper()
			key = input("Enter Key : ")
			strng = strng.upper()
			strng = strng.replace(" ", "")
			key = key.upper()
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
	playfair_cipher()


#wh0am1
