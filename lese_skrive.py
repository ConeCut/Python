def calculator():
    a = str(input("Put a number in: "))
    if not a or not a.isdigit():
        print("You need a number in bro")
        calculator()
    b = str(input("Put a number in: "))
    if not b or not b.isdigit():
        print("You need a number in bro, we gonna restart the whole thing now")
        calculator()
    operation = str(input("Choose your operation: \n + \n - \n * \n / \n"))


    if(str(operation) == "+"):
        print(int(a) + int(b))
    if(str(operation) == "-"):
        print(int(a) - int(b))
    if(str(operation) == "*"):
        print(int(a) * int(b))
    if(str(operation) == "/"):
        print(int(a) / int(b))
    else:
        print("You must choose between valid operators")
calculator()

def counter():
    
    text = str(input("Type what text you'd like to have counted: "))
    
    letters_count = sum(c.isalpha() for c in text)
    
    numbers_count = sum(c.isdigit() for c in text)
    
    print(f"Letters: {letters_count}, Numbers: {numbers_count}")
    
counter()

def counter_arg(text):
        
    letters_count = sum(c.isalpha() for c in text)
    
    numbers_count = sum(c.isdigit() for c in text)
    
    print(f"Letters: {letters_count}, Numbers: {numbers_count}")
    
"Input text to count it"
"Example"

counter_arg("Hello World 123")