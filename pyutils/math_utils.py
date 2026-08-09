def is_prime(n: int)-> bool:
    """
    Return True if n is a prime number, otherwise False.
    Args:
        n: Integer to test.
    Returns:
        True if n is prime, otherwise False.
    Raises:
        TypeError: If n is not an integer.
    """
    if not isinstance(n,int):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True
      

def factorial(n: int)->int:
    """
    Return the factorial of a non-negative integer.
    Args:
        n: Non-negative integer whose factorial is to be computed.
    Returns:
        The factorial of n.
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n,int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
    
def gcd(a: int, b: int)->int:
    """Return the greatest common divisor of two integers.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The greatest common divisor of a and b.
    Raises:
        TypeError: If a or b is not an integer.
    """
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("a and b must be integers")
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    return a
    

def lcm(a: int, b: int)->int:
    """
    Return the least common multiple of two integers.
    Args:
        a: First integer.
        b: Second integer.
    Returns:
        The least common multiple of a and b.
    Raises:
        TypeError: If a or b is not an integer.
        ValueError: If both a and b are zero.
    """
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("a and b must be integers")
    
    if a == 0 and b == 0:
        raise ValueError("lcm of 0 and 0 is undefined")
    
    if a == 0 or b == 0:
        return 0
    return abs(a*b)//gcd(a,b)
    