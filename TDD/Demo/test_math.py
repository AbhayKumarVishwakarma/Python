from main import factorial


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def test_add():
    result = add(3, 3)
    assert result == 6


def test_subtraction():
    result = sub(5, 3)
    assert result == 2


def test_factorial():
    result = factorial(5)
    assert result == 120
