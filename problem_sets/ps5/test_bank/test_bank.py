from bank import value

def test_hello():
    assert value('Hello') == '$0'

def test_h():
    assert value('Hey') == '$20'

def test_none():
    assert value('Whats up') == '$100'

#test file must be in own directory with __init__ file in same directory. File that needs to be tested must be in one directory above, in same directory 
# as the test directory is in.