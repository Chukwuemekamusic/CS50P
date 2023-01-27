from working import convert
import pytest

def test_AM_PM_time_without_minute():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_AM_PM_time_with_minute():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:24 PM") == "09:00 to 17:24"

def test_PM_AM_time():
    assert convert("10 PM to 10 AM") == "22:00 to 10:00"

def test_put_0_before_single_numbers():
    assert convert("9 PM to 8 AM") == "21:00 to 08:00"
    assert convert("7:05 AM to 8:02 AM") == "07:05 to 08:02"

def test_minutes_greater_than_59():
    with pytest.raises(ValueError):
        convert("7:60 PM to 8:22 AM")

def test_hr_greater_than_12():
    with pytest.raises(ValueError):
        convert("7:00 PM to 15:22 AM")

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("7:22 PM - 8:22 AM")
        convert("cat")

def test_12AM():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"