from plates import is_valid

def test_first_char():
    assert is_valid('CS50') == 'Valid'
def test_length():
    assert is_valid('FOUR') == 'Valid'
def test_num_at_end():
    assert is_valid('ABC0123') == 'Valid'
def test_punc():
    assert is_valid('NO PUNC') == 'Valid'