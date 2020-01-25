# To Get Prime Factors of a Number Using Python
# Author : wh0am1
# GitHub : https://github.com/wh0th3h3llam1


import math


def primeFactors(n):

    while n % 2 == 0:
        print(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i)
            n = n / i

    if n > 2:
        print(int(n))


if __name__ == '__main__':

	x = int(input())

	primeFactors(x)

#wh0am1
