from bank import value

def test_hello_value():
    assert value("hello") == 0
    assert value("hello madam") == 0

def test_capital_hello_value():
    assert value("HELLO") == 0
    assert value("hELLo madam") == 0

def test_starts_with_h_value():
    assert value("h groove") == 20
    assert value("hiya") == 20

def test_starts_with_CAPITAL_h_value():
    assert value("H groove") == 20
    assert value("HIYA") == 20

def test_starts_with_space_value():
    assert value(" hello sir") == 0
    assert value(" hiya sir") == 20

def test_starts_with_others_value():
    assert value("sirs") == 100

def test_starts_with_number_value():
    assert value("5hello ma") == 100

def test_hello_with_extra_value():
    assert value("hellos madam") == 0
    assert value("") == 100