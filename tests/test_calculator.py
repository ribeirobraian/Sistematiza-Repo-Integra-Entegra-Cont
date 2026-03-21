from src.calculator import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(10, 4) == 6


def test_multiply() -> None:
    assert multiply(6, 7) == 42


def test_divide() -> None:
    assert divide(12, 3) == 4


def test_divide_by_zero() -> None:
    try:
        divide(1, 0)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "division by zero is not allowed"
