"""
Math Utility Functions
"""
import math

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple."""
    return abs(a * b) // gcd(a, b)

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def prime_factors(n):
    """Get prime factors of a number."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Examples
if __name__ == "__main__":
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"Prime factors of 84: {prime_factors(84)}")
