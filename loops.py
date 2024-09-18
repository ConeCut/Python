"""
print(range(1,10))

print("\n")

print(list(range(1, 10)))

for i in range(1, 10):
    print(i, end=",")
    
print("\n")
    
for bokstav in "Stine":
    print(bokstav, end=",")
    
print("\n")

liste = ["apple", "banana", "kiwi", "plum"]

for frukt in liste:
    print(frukt)
    
print("\n")

for i in range(1, 11, 3):
    print(i)
    
print("\n")
for i in range(1, 51, 2):
    print(i)
print("\n")
for i in range(0, 51, 2):
    print(i)
print("\n")
for i in range(10, 0, -1):
    print(i)
print("\n")
for i in range(7, 42, 3):
    print(i)


for i in range(1, 5):
    print()
    for j in range(1, 5):
        print(f"{i*j}", end=" ")
"""

for i in range(1, 11):
    print(i**3)
    
    

size = 5
 
print("   |", end=" ")
for i in range(1, size + 1):
    print(f"{i:2}", end=" ")  
print("\n---+" + "---" * size) 
 
for i in range(1, size + 1):
    print(f"{i:2} |", end=" ")
   
    for j in range(1, size + 1):
        print(f"{i * j:2}", end=" ")
    print()  
    
    
terms = int(input('Number of terms in Fibonacci sequence: '))
count = 0
n1 = 0
n2 = 1
fibonacci_sequence = []

while count < terms:
    fibonacci_sequence.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

for i in range(0, len(fibonacci_sequence), 5):
    row = fibonacci_sequence[i:i+5]
    print(" ".join("{:<10}".format(num) for num in row))