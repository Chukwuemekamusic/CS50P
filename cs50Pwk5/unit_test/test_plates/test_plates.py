from plates import is_valid

def test_greater_than_six_characters_is_valid():
    assert is_valid("ebubeevan") == False
    assert is_valid("anyae123") == False

def test_less_than_sixletters_is_valid():
    assert is_valid("ebube") == True
    assert is_valid("ebu") == True

def test_equal_to_six_is_valid():
    assert is_valid("ebubes") == True


def test_less_than_orEqual_endWith_number_is_valid():
    assert is_valid("eb34") == True
    assert is_valid("ebub34") == True


def test_number_between_letters_is_valid():
    assert is_valid("eb234hi") == False
    assert is_valid("e234r") == False

def test_inside_number_starts_with_zero_is_valid():
    assert is_valid("ebu034") == False
    assert is_valid("eb044") == False

def test_starts_with_number_is_valid():
    assert is_valid("4ebub") == False