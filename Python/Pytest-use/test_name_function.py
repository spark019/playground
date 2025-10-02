# pytests searches for files and functions starting with 'test_'

# Import functions for testing
from name_function import get_formatted_name, get_formatted_name_2

# Define test functions
def test_first_last_name():
    """Do names like 'Peter Lustig' work?"""
    formatted_name = get_formatted_name('peter', 'lustig')
    assert formatted_name == 'Peter Lustig' # assumption for testing

def test_full_name():
    """Do names like 'Peter Lustig' work?"""
    formatted_name = get_formatted_name_2('peter', 'lustig')
    assert formatted_name == 'Peter Lustig'

def test_first_last_middle_name():
    """Do names like 'Peter Nicht Lustig' work?"""
    formatted_name = get_formatted_name_2('peter', 'lustig', 'nicht')
    assert formatted_name == 'Peter Nicht Lustig'