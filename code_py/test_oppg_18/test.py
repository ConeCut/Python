import pytest
from karakter import karakter

def test_karakter():
    assert karakter(45) == "Ikke bestått"
    assert karakter(65) == "Bestått"
    assert karakter(80) == "Godt bestått"
    assert karakter(95) == "Meget godt bestått"
    assert karakter(110) == "Ikke gyldig poengsum!"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    