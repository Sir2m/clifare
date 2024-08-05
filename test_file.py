import file
from objects import *

def test_add():
    """testing is the __add__ overwrite is working with all objects, the parent, children and grandchildren"""
    x = Wallet(10)
    y = Person('Test Person', 50)
    z = Menue("Test Menue")
    w = Farer("Test Farer", 50, 5, 4)
    assert type(z + w) == Wallet 
    assert (z + w).pay == 50   # between Menue and Farer
    assert (x + z).pay == 10   # between Wallet and Menue
    assert (x + w).pay == 60   # between Wallet and Farer
    assert (x + y).pay == 60   # between Wallet and Person
    assert (y + z).pay == 50   # between Person and Menue
    assert (y + w).pay == 100  # between Person and Farer
