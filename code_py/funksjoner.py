alive = True

def die():
    print('Bang!')
    alive = False

def kms():
    if(alive):
        die()

kms()

























def invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of £{amount} is due for {due_date}")
    
print(invoice("Cosmin", "40kr", "20 sept"))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full = create_name("spongeboob", "squarepants")

print(full)