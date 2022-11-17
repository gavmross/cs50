from twttr2 import shorten 

def test_all_vowels():
    assert shorten('aeoiu') == ''

def test_normal():
    assert shorten('gavin ross') == 'gvn rss'
