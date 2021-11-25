# funktion to test
# run test with pytest
def inc(x):
    return x + 1

# run test on funktion inc
def test_inc():
    assert inc(3) == 5