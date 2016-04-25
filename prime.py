import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        (PM, PN) = (int(i) for i in raw_input().split())

        find_num_of_prime = 0
        i = 0
        while True:
            if isPrime(i):
                find_num_of_prime += 1
            if find_num_of_prime == PM:
                break
            i += 1
        x = []
        find_num_of_prime -= 1
        while True:
            if isPrime(i):
                x.append(i)
                find_num_of_prime += 1
            if find_num_of_prime == PN:
                break
            i += 1
        for j in range(len(x)):
            print x[j],
            if (j+1) % 10 == 0:
                print
        print
    except EOFError:
        break
