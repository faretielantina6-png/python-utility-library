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
    pass
def gcd(a: int, b: int)->int:
    pass

def lcm(a: int, b: int)->int:
    pass