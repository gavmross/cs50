from seasons import birthday
#do not put __init__.py in a test folder, it doesnt work with pytest
def test_birthday():
    assert birthday('2001-02-21') == 'one trillion one hundred  nineteen billion eight hundred  eighty-eight million minutes'
    assert birthday('Feb 21, 2001') == 'Wrong format'
