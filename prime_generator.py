# Helper function.
def is_prime(n):
    if n == 1:  # One is never prime.
        return False
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor, not prime.
    else:
        return True


def primes(number=1):
    while True:
        if is_prime(number):
            yield number  # yield makes this a generator.
        number += 1

for num in primes():  # Generate a list of prime numbers.
    if num > 100:
        break
    print(num)