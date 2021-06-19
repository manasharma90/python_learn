# Filter Prime Numbers
# Loop through the first 1000 numbers and build a list of prime numbers
# First fill out this function definition to check an individual number then use it later

def is_prime(n):
    # Write your code here and return False/True

    if n == 2:
        return True

    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# Code here to build the list of primes from the first 1000 numbers
primes = []

for i in range(1000):
    if is_prime(i) == True:
        primes.append(i)

print(primes)

    
