class Planet:
    
    def __init__(mysillyobject, name, moons, size):
        mysillyobject.name = name
        mysillyobject.moons = moons
        mysillyobject.size = size
        
    def myFunc(doit):
        print(f'Hello, I am {doit.name}, I have {doit.moons} moons, and my radius is {doit.size}')
        
