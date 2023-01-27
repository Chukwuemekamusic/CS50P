from um import count

def test_single_um():
    assert count("um") == 1

def test_single_um_with_space():
    assert count("    um  ") == 1

def test_single_um_with_words():
    assert count("um child") == 1
    assert count("child um") == 1

def test_um_part_of_a_word():
    assert count("um, thanks for the album") == 1
    assert count("umbrella is the sum of things") == 0

def test_multiple_um():
    assert count("um, I have a way um... that is open free, um!") == 3

