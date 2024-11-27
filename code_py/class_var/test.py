from medlem import Medlem

n1 = Medlem('Me', 'Maw', 16)
n2 = Medlem("Mawh", "Meeh", 16)
n3 = Medlem('Maw', 'Maw', 36)

def test():
    assert n1.getId() == 1, f"{n1.getName()} with ID {n1.getId()} does NOT have the expected ID, 1 expected"
    print(f"{n1.getId()} \n{n2.getId()} \n{n3.getId()}")
    print(n1 == n3)
    
test()