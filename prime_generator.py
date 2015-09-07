# Helper function.
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


# This is a generator function for finding prime numbers.
def primes(number=1):
    while True:
        if is_prime(number):
            yield number
        number += 1

for num in primes():
    if num > 100:
        break
    print(num)