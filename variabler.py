# Task 1
# Print a greeting message to the user
print("Hi Cosmin!")

# Task 2 and 3
# Ask the user for their name and store it in the variable 'name'
name = str(input("Hei, what's your name? "))

# Print a personalized greeting using the user's name
print("Hei " + name + "!")

# Task 4
# Ask the user for two numbers and convert them to integers
a = int(input("Put a number in: "))
b = int(input("And another "))

# Print the two numbers entered by the user
print(a)
print(b)

# Task 5
# Calculate the difference between the two numbers
c = a - b

# Check if the difference is positive
if c > 0:
    # Print the positive difference
    print("What's crazy is that the difference between the two is just " + str(c))
    
# Check if the difference is negative
elif c < 0:
    # Make the difference positive by multiplying it by -2 
    c = c + c * -2
    # Print the positive difference
    print("What's crazy is that the difference between the two is just " + str(c))

# Task 6
# Ask the user for another name and store it in the variable 'newname'
newname = str(input("Put another name in: "))

# Task 7 + Printing for tasks 6/7
# Combine the original name and the new name into a single string
sammen = str(name + " og " + newname)

# Print the combined names
print(sammen)
