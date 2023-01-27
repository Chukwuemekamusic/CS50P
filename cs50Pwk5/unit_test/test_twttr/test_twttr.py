from twttr import shorten


def test_lower_case_shorten():
    assert shorten("twitter") == "twttr"

def test_upper_case_shorten():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case_shorten():
    assert shorten("TWITter") == "TWTtr"

def test_sentence_shorten():
    assert shorten("I am A BOy") == " m  By"

def test_string_number_shorten():
    assert shorten("4445") == "4445"

def test_punctuation_shorten():
    assert shorten("Twi.TTEr") == "Tw.TTr"

# def test_number_shorten():
#     assert shorten(415) == 415