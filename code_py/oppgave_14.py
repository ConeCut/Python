def lengde():
    s = input('Input anything in here: ')
    a = list(s)
    count = 0
    for characters in a:
        count += 1
    print(count)
    
    
def lengde2():
    s2 = input('Input anything in here: ')
    b2 = input('Search for a specific char: ')
    a2 = list(s2)
    count2 = 0
    for char in a2:
        if char == b2:
            count2 += 1
    print(count2)
    
lengde2()

