from math import sqrt

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if (number_of_primes <= 0):
        raise ValueError("Number of primes must be positive!")
    list = []
    i = 2
    while len(list) < number_of_primes:
        may_be_prime = True
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                may_be_prime = False
                break
        if may_be_prime:
            list.append(i)
        i = i + 1

    return list
