# Function to check if a number is prime
def is_prime(num):
    # Check if the number is less than 2, as numbers < 2 are not prime
    if num < 2:
        return False
    # Check divisibility by all numbers from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible, it's not a prime number
            return False
    return True

# Function to generate a list of prime numbers up to 'n'
def list_primes(n):
    prime_numbers = []  # List to store prime numbers

    # Loop through numbers from 2 to 'n' and check if they're prime
    for num in range(2, n + 1):
        if is_prime(num):  # If the number is prime, add it to the list
            prime_numbers.append(num)

    # Return the list of prime numbers
    return prime_numbers

# Call the list_primes function to get all primes up to 50
print(list_primes(50))
