def is_prime(n: int)-> bool:
    """Return True if n is a prime number, otherwise False."""
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
    """Return the factorial of a non-negative integer."""
    if not isinstance(n,int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative")
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
    
def gcd(a: int, b: int)->int:
    pass

def lcm(a: int, b: int)->int:
    pass