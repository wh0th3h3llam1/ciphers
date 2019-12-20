# Affine Cipher using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


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
		# print(q, r1, r2, r, t1, t2, t)
	
	if (r1 == 1):
		t1 = t1 % n
		return t1
	else:
		return -1
		

def encrypt(strng, k1, k2):
	encrypted = ""
	for k in strng:
		l = ord(k) - 97
		t = (((l * k1) + k2) % 26 + 97)
		encrypted += (chr(t))
	
	print("Encrypted Text : " + encrypted)
	

def decrypt(strng, k1, k2):
	
	i_key = inverse(k1, 26)
	
	decrypted = ""
	
	for k in strng:
		l = ord(k) - 97
		t = (((l - k2) * i_key ) % 26 ) + 97
		decrypted += chr(t)
	
	print("Decrypted Text : " + decrypted)	


def affine_cipher():
	print("****************************************************")
	print("\t\tAFFINE CIPHER")
	print("****************************************************")

	print("1. Encrypt")
	print("2. Decrypt")
	print("0. Exit")
	print("Enter Your Choice : ", end="")
	choice = int(input())
	print("----------------------------------------------------")

	if choice == 1:
		strng = input("Enter String to Encrypt : ")
		k1 = int(input("Enter k1 : "))
		k2 = int(input("Enter k2 : "))
		strng = strng.lower()
		print("----------------------------------------------------")
		encrypt(strng, k1, k2)
		print("----------------------------------------------------")
		
	elif choice == 2:
		strng = input("Enter String to Decrypt : ")
		k1 = int(input("Enter k1 : "))
		k2 = int(input("Enter k2 : "))
		strng = strng.lower()
		print("----------------------------------------------------")
		decrypt(strng, k1, k2)
		print("----------------------------------------------------")
		
	elif choice == 0:
		print("BYE...")
		print("----------------------------------------------------")
		exit(0)

	else:
		print("Invalid Choice, Try Again.")



if __name__ == '__main__':
	affine_cipher()
	

#wh0am1
