import pytest
from pyutils.math_utils import factorial, gcd, is_prime, lcm

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True

def test_is_prime_edge_cases():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False

def test_is_prime_invalid_types():
    with pytest.raises(TypeError):
        is_prime("17") # type: ignore[arg-type]
    with pytest.raises(TypeError):
        is_prime(3.5)   # type: ignore[arg-type]

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_invalid_inputs():
    with pytest.raises(TypeError):
        factorial("5")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        factorial(3.5)   # type: ignore[arg-type]
    with pytest.raises(ValueError):
        factorial(-1)

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(12, 8) == 4
    assert gcd(15, 10) == 5
    assert gcd(7, 3) == 1

def test_gcd_edge_cases():
    assert gcd(0, 5) == 5
    assert gcd (5, 0) == 5
    assert gcd(0,0) == 0
    assert gcd(-12, 8) == 4
    assert gcd(12, -8) == 4
    assert gcd(-12, -8) == 4

def test_gcd_invalid_types():
    with pytest.raises(TypeError):
        gcd(12.5, 5)   # type: ignore[arg-type]
    with pytest.raises(TypeError):
        gcd("12", 5)   # type: ignore[arg-type]

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(3, 5) == 15
    assert lcm(12, 18) == 36
    assert lcm(10, 15) == 30


def test_lcm_edge_cases():
    assert lcm(-4, 6) == 12
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0

def test_lcm_invalid_types():
    with pytest.raises(TypeError):
        lcm(3.5, 5)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        lcm("4", 5)  # type: ignore[arg-type]

def test_lcm_zero_zero():
    with pytest.raises(ValueError):
        lcm(0, 0)