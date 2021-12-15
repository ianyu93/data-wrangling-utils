from data_wrangling_utils import __version__
from data_wrangling_utils import utils

def test_version():
    assert __version__ == '0.0.1'


# test normalize_text
# test printmd

def test_replace_all():
    assert utils.replace_all('aabbcc', {'a':['b']}) == 'aaaacc'
    assert utils.replace_all('today is a beautiful day', {'a':['b', 'd'], 's': ['u', 't']}) == 'soaay is a aeassifsl aay'

def test_flatten():
    assert utils.flatten([[1,2],[3,4]]) == [1,2,3,4]
    assert utils.flatten(((1,2),(3,4))) == [1,2,3,4]

 
def test_break_nest():
    assert utils.break_nest([[(1,2),(3,4)],[(5,6),(7,8)]]) == [1,2,3,4,5,6,7,8]
    assert utils.break_nest((((1,2),(3,4)),((5,6),(7,8)))) == [1,2,3,4,5,6,7,8]

# test find_columns

    


