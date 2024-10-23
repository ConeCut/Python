def show_menu():
    # Display the shop menu with a list of items and their prices
    print("\nWelcome to the shop!")
    print("Here are the items you can buy:")
    print("1. Bread - 20 kr")
    print("2. Milk - 15 kr")
    print("3. Cheese - 40 kr")
    print("4. Yogurt - 12 kr")
    print("5. Proceed to checkout")
    print("")

def calculate_total_price(cart):
    # Dictionary of item prices
    prices = {
        "bread": 20,
        "milk": 15,
        "cheese": 40,
        "yogurt": 12
    }
    
    total = 0  # Initialize total price
    # Calculate the total price based on the items and quantities in the cart
    for item, quantity in cart.items():
        total += prices[item] * quantity
    return total  # Return the total price

def print_receipt(cart):
    # Dictionary of item prices
    prices = {
        "bread": 20,
        "milk": 15,
        "cheese": 40,
        "yogurt": 12
    }
    
    print("\nReceipt:")
    print(f"{'Item':<10}{'Quantity':<10}{'Price':<10}")
    print("-" * 30)
    
    # Print the items in the cart with their quantities and total price per item
    for item, quantity in cart.items():
        if quantity > 0:  # Only print items that were added to the cart
            print(f"{item.capitalize():<10}{quantity:<10}{prices[item] * quantity:<10} kr")
    
def shop():
    # Initialize a shopping cart with zero quantities for each item
    cart = {
        "bread": 0,
        "milk": 0,
        "cheese": 0,
        "yogurt": 0
    }

    while True:  # Start an infinite loop for the shopping process
        show_menu()  # Display the menu to the user
        choice = input("Choose an item by typing the number (1-5): ")

        # Check if the choice is valid (1-4 for items, 5 to checkout)
        if choice in ["1", "2", "3", "4"]:
            # Map the user's choice to the corresponding item
            if choice == "1":
                item = "bread"
            elif choice == "2":
                item = "milk"
            elif choice == "3":
                item = "cheese"
            elif choice == "4":
                item = "yogurt"
                
            # Ask the user how many of the chosen item they want to add to the cart
            quantity = int(input(f"How many {item} would you like to add? "))
            cart[item] += quantity  # Update the cart with the new quantity
            print(f"You added {quantity} {item}(s) to the cart.")
            
        elif choice == "5":
            # If the user chooses to checkout, print the receipt and calculate the total price
            print_receipt(cart)
            total_price = calculate_total_price(cart)
            print(f"\nThe total price for your shopping is: {total_price} kr.")
            
            print("Thank you for shopping with us!")
            break  # Exit the loop and end the shopping process
        else:
            # Handle invalid input by prompting the user to try again
            print("Invalid choice, please try again.")

# Start the shop function to run the shopping simulation
shop()
