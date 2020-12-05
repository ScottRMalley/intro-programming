import sys


def get_prime_factors(number):
    factors = []
    while number > 1:
        for i in range(2, number + 1):
            if number % i == 0:
                number = number // i
                factors.append(i)
                break
    return factors


if len(sys.argv) < 2:
    print('please input a number')
    sys.exit()

input_number = int(sys.argv[1])
primes = get_prime_factors(input_number)
print(set(primes))
