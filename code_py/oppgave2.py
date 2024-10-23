def yes_or_no():
    # Prompt the user to input their choice
    inp = input("Would you like some coke? Type yes or no ")

    # Check if the input is "yes"
    if inp == "yes":
        # Inform the user that a coke is on its way
        print("You chose yes, one coke is on its way ")
    
    # Check if the input is "no"
    elif inp == "no":
        # Inform the user that they will not receive any coke
        print("You chose no, NO COKE FOR YOU HAHAHA ")
    
    # Handle invalid inputs (anything other than "yes" or "no")
    else:
        # Inform the user of the invalid input and prompt again
        print("You must choose between yes or no ")
        # Recursively call the function to prompt the user again
        return yes_or_no()

# Call the function to execute it
yes_or_no()
