# Pair : Zulayika Nalukenge & Peter Kakuru
from fibonacci import fibonacci

def test_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_small_numbers():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5

def test_larger_number():
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610

def test_negative_number():
    try:
        fibonacci(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        assert True

