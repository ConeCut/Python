# Given list
bokstaver = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# a) Print the first three elements
print(bokstaver[:3])

# b) Print the middle three elements
print(bokstaver[2:5])

# c) Print the list from the third element to the second last element
print(bokstaver[2:-1])

# Given list
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a) Print each number multiplied by 10 using a for-loop
for number in tall:
    print(number * 10)

# b) Create a new list using list comprehension where each element is increased by 10
new_list = [number + 10 for number in tall]
print(new_list)

# Given list
tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Remove every other element
result = tall[::2]
print(result)

# Create a 2D list representing a chessboard
chessboard = [['svart' if (row + col) % 2 == 0 else 'hvit' for col in range(8)] for row in range(8)]

# Print the chessboard row by row
for row in chessboard:
    print(row)

# Initialize an empty list
numbers = []

# Continue to prompt the user to enter numbers until they hit Enter
while True:
    user_input = input("Skriv inn et heltall: ")
    
    if user_input == "":
        break

    number = int(user_input)
    numbers.append(number)
    
    print(f"Summen er nå {sum(numbers)}")

# Remove the largest and smallest numbers
if len(numbers) > 2:
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))

# Calculate and print the average
if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"Listen uten min og maks er {numbers}")
    print(f"Gjennomsnittet av tallene er {avg}")

# Use the Sieve of Eratosthenes to find prime numbers under 100
def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

# Get prime numbers less than 100
prime_numbers = sieve_of_eratosthenes(100)

# Print the prime numbers in 5 columns
for i in range(0, len(prime_numbers), 5):
       print(prime_numbers[i:i + 5])