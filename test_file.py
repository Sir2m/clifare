import file
import pytest
from objects import *


def test_inter():
    assert inter('5') == 5
    assert inter('"5"') == '"5"' 
    assert inter("hey") == "hey"
    assert inter('60') == 60


def test_pay_setting(monkeypatch):
    """
    testing different values set for pay attribute
    """
    
    inputs = iter(["This", [5, 4], -5, 10, "That", [5, 4], -5, 500])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # standard case
    x = Person('test pay 1', 73)
    assert x.pay == 73

    # testing on Wallet, the main setter of pay
    y = Wallet('')
    assert y.pay == 10
    
    # checking that farer needs to settle down the pay before the charge
    z = Farer('test pay 2', '', 50, 5)
    assert z.pay == 500


def test_add():
    """
    testing the __add__ overloading
    """
    
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

def test_name_setting():
    """
    testing different values set for name attribute
    """
    
    names = ["", 5, 'mohab', '\n']
    results = iter(['unknown 1', 'unknown 2', 'mohab', '\n'])
    
    # tests are made only by Person class since its the main setter
    for _ in names:
        x = Person(_, 50)
        assert x.name == next(results)


def test_amount_setting(monkeypatch):
    """
    testing different values set for amount attribute
    """

    inputs = iter(["100", "'5'", None, -5, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    x = Farer("test amount 1", 1000, 1, "")
    y = Farer("test amount 2", 1000, 1, "")
    z = Farer("test amount 3", 1000, 1, "")

    assert x.amount == 100
    assert y.amount == 1
    assert z.amount == 10


def test_charge_setting(monkeypatch):
    """
    testing different values set for price attribute in 'Farer'
    to see charge implementation
    """
    
    inputs = iter([None, -10, 100, 100, 1, 100])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Farer("test change 1", 10, "", 1)
    y = Farer("test change 2", 168, 10, 10)

    assert x.change == 0
    assert y.change == 68


def testing_men_cls_method(monkeypatch):
    """
    testing both add_item, with add_order method since they are almost related
    """

    inputs = iter(["", None, -10, 50])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    Menue.add_item("Potato")
    assert Menue.MENU["Potato"] == 50


def testing_add_order(monkeypatch):
    """
    testing the add_order method in front of different scenarios
    """

    inputs = iter([
        -5, "hey", None, # first test on quantity
        -8, 10, # second test on quantity
        38
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Menue("test add_order 1")
    y = Menue("test add_order 2")
    
    # scenario 1: problem invalid quantity
    x.add_order('Potato', '') # potato was set in a previous test
    y.add_order('potato', '')

    assert x.order["Potato"] == 1
    assert y.order["Potato"] == 10

    # scenario 2: adding quantity for an order
    x.add_order('potato', 2)
    y.add_order('Potato', 5)

    assert x.order["Potato"] == 3
    assert y.order["Potato"] == 15

    z = Menue('test add_order 3')

    # scenario 3: adding an order of a non existing dish
    z.add_order("fish", 10)

    assert Menue.MENU['Fish'] == 38
    assert z.order['Fish'] == 10


def test_payers():
    ...


def test_getter(monkeypatch):
    """
    testing the get_price function
    """
    inputs = iter(["\n", None, "'5'", "10",
                   'm', None, '', -10, 5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # main test
    x = file.getter("mode: ")
    assert x == 10

    # fare mode test
    y = file.getter(" ",
                          True,
                          lambda x: x > 0,
                          " ")
    assert y == 5


def test_add_fp(monkeypatch):
    """
    """
