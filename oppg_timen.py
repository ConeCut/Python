# a) Create a dictionary: phone book
phone_book = {
    "H": 46547687,
    "I": 76765769,
    "J": 56959765,
    "K": 86549546
}

# b. The dictionary has been filled with names and phone numbers (done above)
# c. Let the user enter a name and check if it exists in the phone book
name = input("Enter a name: ")

if name in phone_book:
    print(f"The phone number for {name} is {phone_book[name]}.")
else:
    # d. If the name doesn't exist, ask for the phone number and add it to the phone book
    new_number = input(f"The name {name} does not exist. Please enter the phone number for {name}: ")
    
    # Convert the phone number to an int before storing it in the dictionary
    phone_book[name] = int(new_number)
    
    print(f"{name} has been added to the phone book with the number {phone_book[name]}.")

# Display the updated phone book
print("\nUpdated phone book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")

# Define a function to read car information from a file
def read_car_data(filename):
    # Create an empty dictionary
    result = {}

    # Open the file for reading
    with open(filename, 'r') as file:
        # Go through each line in the file
        for line in file:
            # Remove newline characters and split the line by ":"
            columns = line.strip().split(":")
            if len(columns) == 2:
                # Store the first column as key and the second column as value
                result[columns[0]] = columns[1]

    # Return the result
    return result

# Print the result
if __name__ == "__main__":
    car_data = read_car_data("c:/Users/coena002/OneDrive - Osloskolen/Datamaskin sync/code/oppg_timen")
    print(car_data)
