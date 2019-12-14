# Caesar Cipher (Additive Cipher) using Python
# Case Sensitive



import os
import platform

def encrypt(strng, key):

	enc = []

	for i in range(len(strng)):
		if ord(strng[i]) in range(97, 122):
			# Small Letter
			# print("Small Letter : " + strng[i])
			t = (ord(strng[i]) - 97 + key) % 26 + 97
			enc.append(chr(t))

		elif ord(strng[i]) in range(65, 90):
			# Capital Letter
			# print("Capital Letter : " + strng[i])
			t = (ord(strng[i]) - 65 + key) % 26 + 65
			enc.append(chr(t))

		elif ord(strng[i]) in range(48, 57):
			# Numbers
			# print("Num : " + strng[i])
			t = (ord(strng[i]) - 48 + key) % 10 + 48
			enc.append(chr(t))

		else:
			enc.append(strng[i])
	encrypted = ""
	print(encrypted.join(enc))
	return encrypted


def decrypt(strng, key):
	dec = []

	for i in range(len(strng)):
		if ord(strng[i]) in range(97, 122):
			# Small Letter
			# print("Small Letter : " + strng[i])
			t = (ord(strng[i]) - 97 - key) % 26 + 97
			dec.append(chr(t))

		elif ord(strng[i]) in range(65, 90):
			# Capital Letter
			# print("Capital Letter : " + strng[i])
			t = (ord(strng[i]) - 65 - key) % 26 + 65
			dec.append(chr(t))

		elif ord(strng[i]) in range(48, 57):
			# Numbers
			# print("Num : " + strng[i])
			t = (ord(strng[i]) - 48 - key) % 10 + 48
			dec.append(chr(t))

		else:
			dec.append(strng[i])
	decrypted = ""
	print(decrypted.join(dec))
	return decrypted


def brute_force(strng):
	key = 26
	print("Brute Forcing the String...")

	for k in range(key):
		print("Key : " + str(k) + " | Decrypted String : ", end="")
		decrypt(strng, k)


def main():
	while True:
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')

		print("****************************************************")
		print("\tCAESAR CIPHER (ADDITIVE CIPHER) USING PYTHON")
		print("****************************************************")

		print("1. Encrypt")
		print("2. Decrypt")
		print("3. Brute-Force")
		print("0. Exit")
		print("Enter Your Choice : ", end="")
		choice = int(input())

		print("----------------------------------------------------")

		if choice == 1:
			strng = input("Enter String to Encrypt : ")
			key = int(input("Enter Key : "))
			key = key % 26
			print("----------------------------------------------------")
			encrypt(strng, key)

		elif choice == 2:
			strng = input("Enter String to Decrypt : ")
			key = int(input("Enter Key : "))
			key = key % 26
			print("----------------------------------------------------")
			decrypt(strng, key)

		elif choice == 3:
			strng = input("Enter String to Brute-Force : ")
			print("----------------------------------------------------")
			brute_force(strng)

		elif choice == 0:
			print("BYE...")
			print("----------------------------------------------------")
			exit(0)

		else:
			# print("Invalid Choice, Try Again.")
			pass

		x = input()


if __name__ == "__main__":
	main()