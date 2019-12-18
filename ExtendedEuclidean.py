# Extended Euclidean Algorithm (Multiplicative Inverse) using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


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
		print("a^(-1) : " + str(t1))


def main():
	print("****************************************************")
	print("\t\tEXTENDED EUCLIDEAN ALGORITHM")
	print("To find the Multiplicative Inverse of given Numbers")
	print("****************************************************")
	print("\tFormula : a^(-1) mod n")
	print("----------------------------------------------------")

	a = int(input("Enter a : "))
	n = int(input("Enter n : "))

	extended_euclidean(a, n)


main()


#wh0am1
