from pytest import raises
from jar import Jar

def test_init():
    jar = Jar(15)
    assert jar.capacity ==  15

def test_str():
    jar2 = Jar()
    jar2.deposit(3)
    print(jar2)

def test_deposit():
    jar3 = Jar()
    jar3.deposit(5)
    assert jar3.size == 5
    #HOW TO TEST FOR EXCEPTIONS
    with raises(ValueError):
        jar3.deposit(20)

def test_withdraw():
    jar4 = Jar()
    jar4.deposit(4)
    jar4.withdraw(2)
    assert jar4.size == 2
    with raises(ValueError):
        jar4.withdraw(10)
    