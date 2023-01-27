from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_higher_numerator_convert():
    convert("5/4") == False

def test_guage():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_convert_exceptions():
    convert("1/0") == False
    convert("1/2/3") == False

def test_type_input():
    convert("cat/dog") == False
    # with pytest.raises(TypeError):
    #     gauge("cat")

# # Run the test
# test_convert_exceptions()


# # Run the test functions
# test_convert()
# test_guage()
