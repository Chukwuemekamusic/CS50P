from numb3rs import validate 

def test_number_less_than_256():
    assert validate("1.2.3.4") == True
    assert validate("255.203.2.0") == True

def test_less_than_4_numbers():
    assert validate("205.55.101") ==  False
    assert validate("1.2.3") == False

def test_when_1_number_more_than_255():
    assert validate("1.2.3.256") == False
    assert validate("3000.2.3.0") == False

def test_not_numbers():
    assert validate("a.b.c.d") == False
    assert validate("1.2.cat.d") == False

def test_only_zeroes():
    assert validate("0.0.0.0") == True

def test_more_than_4_numbers():
    assert validate("1.2.3.4.5") == False
    assert validate("3.222.111.222.11") == False
