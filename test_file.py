import file
import pytest
from objects import *


def test_pay_setting(monkeypatch):
    """
    testing the handling of pay setter of different invalid values
    like strings, non positive numbers, and other classes
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
    testing the __add__ overloading made in 'Wallet' for the
    different children and grand children 
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
    testing the handling of name setter of non given values, non
    string objects and normal values
    """
    
    names = ["", 5, 'mohab', '\n']
    results = iter(['unknown 1', 'unknown 2', 'mohab', '\n'])
    
    # tests are made only by Person class for easier implementing of the for loop
    for _ in names:
        x = Person(_, 50)
        assert x.name == next(results)


def test_amount_setting(monkeypatch):
    """
    testing the handling of amount setter of non positive values
    and the defaulting of 1 in empty given amounts
    """

    inputs = iter(["100", "'5'", None, -5, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    x = Farer("test amount 1", 1000, 1, "")
    y = Farer("test amount 2", 1000, 1, "")
    z = Farer("test amount 3", 1000, 1, "")

    assert x.amount == 100
    assert y.amount == 1
    assert z.amount == 10


def test_change_setting(monkeypatch):
    """
    testing the handling of 'Farer' change setter of different
    givens and checks the change to be a non negative value
    """
    
    inputs = iter([None, -10, 100, # setting the price correctly
                   100, 1, 100]) # "change" managing a negative charge
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Farer("test change 1", 10, "", 1)
    y = Farer("test change 2", 168, 10, 10)

    assert x.change == 0
    assert y.change == 68


def test_change_pay(monkeypatch):
    """ testing the applying of change_pay method """

    inputs = iter(['m', 200, # sets the pay correctly
                   20, 100, 10, 5]) # checks the change
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Farer("test change_pay 1", 100, 60, 1)
    y = Farer("test change_pay 2", 200, 5, 5)

    x.change_pay(inter('_'))
    y.change_pay(inter('_'))
    assert x.pay == 200
    assert y.pay == 100
    assert y.amount == 10
    assert y.price == 5


def test_change_amount(monkeypatch):
    """ testing the applying of change_amount method """

    inputs = iter(['m', 20, # sets the pay correctly
                   20, 100, 10, 5]) # checks the change
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Farer("test change_amount 1", 100, 1, 5)
    y = Farer("test change_amount 2", 50, 5, 5)

    x.change_amount(inter('_'))
    y.change_amount(inter('_'))
    assert x.amount == 20
    assert y.pay == 100
    assert y.amount == 10
    assert y.price == 5


def test_str():
    """ it tests the f-string to work as expected when turing 'Farer' into string """
    
    x = str(Farer("test str 1", 50, 2, 5))
    y = str(Farer('test str 2', 200, 6, 5))
    
    assert x == "Name: test str 1\nPaid: 50\nFor: 5\nChange: 40\nPrice: 2"
    assert y == "Name: test str 2\nPaid: 200\nFor: 5\nChange: 170\nPrice: 6"


def test_add_item(monkeypatch):
    """ testing add_item class method """

    inputs = iter(["", None, -10, 50])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    Menue.add_item("Potato")
    assert Menue.MENU["Potato"] == 50

    # trying to add and already existed dish
    x = Menue.add_item("Potato")
    assert x == None


def test_del_menu():
    """ checks that the del_menu class method works for further tests """

    Menue.del_menu() # there was potato in the menu from previous tests
    assert Menue.MENU == {}


def test_edit_price(monkeypatch):
    """
    test edit_price method, sets the two dishes then sets the new
    price with checking some scenarios
    """
    Menue.del_menu()
    inputs = iter([80, 15, # price for the added items
                   'Chicken', -5, 75,
                   'Fries', None, 13])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    Menue.add_item("chicken")
    Menue.add_item('fries')
    Menue.edit_price()
    Menue.edit_price()

    assert Menue.MENU["Chicken"] == 75
    assert Menue.MENU['Fries'] == 13


def test_add_tax(monkeypatch):
    """
    testing the ability to add and remove the taxes set to the
    prices of the menu with different values
    """

    Menue.del_menu()
    inputs = iter(["10%", 10, 50, 0.05, 0])
    monkeypatch.setattr('builtins.input', lambda _:next(inputs))
    
    Menue.add_tax()
    assert Menue.TAX == 0.05
    Menue.add_tax()
    assert Menue.TAX == 0


def test_add_order(monkeypatch):
    """
    testing the add_order method in its main scenarios, wether
    setting or adding for the object's order or even setting the
    dish into the menue
    """

    inputs = iter([
        -5, "hey", None, # first test on quantity
        50, # price of potato
        -8, 10, # second test on quantity
        38 # price of fish
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = Menue("test add_order 1")
    y = Menue("test add_order 2")
    
    # scenario 1: problem invalid quantity, non existing order first time
    x.add_order('Potato', '')
    y.add_order('potato', '')

    assert x.order["Potato"] == 1
    assert y.order["Potato"] == 10

    # scenario 2: adding quantity for an order
    x.add_order('potato', 2)
    y.add_order('Potato', 5)

    assert x.order["Potato"] == 3
    assert y.order["Potato"] == 15


@pytest.fixture
def set_menu(monkeypatch):
    """ A fixture to set a test menu made to simplify testing steps """

    Menue.del_menu()

    inputs = iter([20, 70, 15, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    Menue.add_item("Potato")
    Menue.add_item("Chicken")
    Menue.add_item("Fries")
    Menue.add_item("Cans")


@pytest.fixture
def menu_ord1(set_menu):
    """ fixture sets a character using the set_menu fixture """
    char = Menue('test 1')
    char.add_order("Potato", 2)
    char.add_order("Chicken", 1)
    char.add_order('cans', 2)
    return char


@pytest.fixture
def menu_ord2(set_menu):
    """ fixture sets a character using the set_menu fixture """
    char = Menue('test 1')
    char.add_order("Fries", 1)
    char.add_order("Chicken", 2)
    char.add_order('cans', 4)
    return char


def test_get_cost(menu_ord1, menu_ord2):
    """ testing the get_cost method """

    x = menu_ord1
    x.get_cost()
    y = menu_ord2
    y.get_cost()

    assert x.cost == 130
    assert y.cost == 195


def test_to_pay_get_change(monkeypatch, menu_ord1, menu_ord2):
    """
    testing to_pay and get_change methods, both are in one test
    since the to_pay method do call get_change automatically after
    pay is set
    """

    inputs = iter([100, 150, 200])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = menu_ord1
    x.to_pay()
    x.to_pay()
    y = menu_ord2
    y.to_pay()

    assert x.pay == 150
    assert x.change == 20
    assert y.pay == 200
    assert y.change == 5


def test_inter():
    """ testing the inter function """
    assert inter('5') == 5
    assert inter('"5"') == '"5"' 
    assert inter("hey") == "hey"
    assert inter('60') == 60


def test_getter(monkeypatch):
    """ testing the get_price function """
    inputs = iter(["\n", None, "'5'", "10",
                   'm', None, '', -10, 5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # main test
    x = file.getter("mode: ")
    assert x == 10

    # fare mode test
    y = file.getter(" ", True,
                    lambda x: x > 0, " ")
    assert y == 5


@pytest.fixture
def far_char_d():
    """ this fixture made to set a zack payer in the add_fp cli interface """
    
    operations = ['David', 50, 5, 2, # setting the character
                  1, "Zack", # change name
                  2, 'm', 100, # change paying, including an error 
                  3, 1, # changing amount
                  4, 5, 6] # character deleted, returned none
    return operations


@pytest.fixture
def far_char_k():
    """
    this fixture made to set a kevin payer in the add_fp cli
    interface, this fixture is set to the special add_fp (with
    price passed) only
    """
    
    operations = ['Kevin', 100, 7, # set character with preset price
                  3, 15, 100, 5, 10, # changing amount, including an error
                  7] # return character
    return operations


@pytest.fixture
def far_char_s():
    """ this fixture made to set a sam payer in the add_fp cli interface """
    
    operations = ["Sam", 200, 60, 3, 7] # sets and save the character
    return operations


def test_add_fp(monkeypatch, far_char_d, far_char_k):
    """
    tests the adding of both characters, in both modes of add_fp
    (passing a price and not) and checks some error handlings

    it uses two fixtures zack, which test the normal mode of
    add_fp, and kevin, which is made for the other mode
    """

    inputs = iter([*far_char_d, *far_char_k])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    x = file.add_fp()
    assert x == None

    y = file.add_fp(10)
    assert type(y).__qualname__ == Farer.__qualname__
    assert y.name == "Kevin"
    assert y.pay == 100
    assert y.amount == 5
    assert y.price == 10
    assert y.change == 50


@pytest.fixture
def mFare_op(far_char_d, far_char_s):
    """
    this fixture is made to combine both zack and sam operation
    order with the general operations of mFare general cli
    interface to test it generally
    """

    operations = [1, *far_char_d, # sets david character
                  1, *far_char_s, # sets sam character
                  2, 3, 4] # do rest of operations successfully and quits
    return operations


def test_mFare(mFare_op, monkeypatch):
    """
    test the whole mFare cli interface by adding two payers and
    testing all available options using the preset mFare_op fixture
    """

    inputs = iter(mFare_op)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        file.mFare()


@pytest.fixture
def man_char_r(set_menu):
    """ fixture made for a Menu customer operation inside the add_mp interface """

    operations = ["max",
                  1, "chicken", 2,
                  1, "potato", 2,
                  1, "fries", 1,
                  2, "Rex",
                  3, 4, 150,
                  8, 4, 200,
                  5, 6, 8]
    return operations


@pytest.fixture
def man_char_p(set_menu):
    """ fixture made for a Menu customer operation inside the add_mp interface """

    operations = ["Paul",
                  1, "chicken", 1,
                  1, "fries", 1,
                  7]
    return operations


@pytest.fixture
def man_char_c(set_menu):
    """ fixture made for a Menu customer operation inside the add_mp interface """

    operations = ["Conan",
                  1, "chicken", 1,
                  1, "Cans", 2,
                  1, "fries", 1,
                  3, 4, 200,
                  8]
    return operations


def test_add_mp(monkeypatch, man_char_r, man_char_p):
    """
    testing add_mp cli interface using the rex and paul customers
    fixture and test all operations with all possible errors
    """

    inputs = iter([*man_char_r, *man_char_p])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    x = file.add_mp()
    assert x.change ==  5
    assert x.cost == 195
    assert x.pay == 200
    y = file.add_mp()
    assert y == None


@pytest.fixture
def Menu_op(man_char_r, man_char_c):
    """
    fixture set all operations to deal with Menu interface checking
    all possible operations and testing possible errors using both
    rex and conan customer fixture, it also deletes the MENU class
    attribute to make sure that program starts from 0 in testings 
    """

    operations = [3, 'potato', 20,
                  3, 'Chicken', 70,
                  3, 'Fries', 13,
                  3, 'Cans', 10,
                  4, 6, 100, 1, 0.14, 6, 0,
                  5, 'fries', 15,
                  1, *man_char_r,
                  1, *man_char_c,
                  2, 7, 8, 9]
    Menue.del_menu()
    return operations


def test_Menu(monkeypatch, Menu_op):
    """
    applies the Menu_op operations list on the Menu interface and
    checks if the programs quits safely
    """

    inputs = iter(Menu_op)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        file.Menu()
