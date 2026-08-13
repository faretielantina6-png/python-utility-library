"""Examples of the mathematical utilities provided by pyutils."""

from pyutils.math_utils import factorial, gcd, is_prime, lcm


def main() -> None:
    """Run examples for the math utilities."""

    # Prime number detection
    print("Prime number detection:")
    print(f"is_prime(17) -> {is_prime(17)}")
    print(f"is_prime(20) -> {is_prime(20)}")
    print()

    # Factorial
    print("Factorial:")
    print(f"factorial(5) -> {factorial(5)}")
    print(f"factorial(7) -> {factorial(7)}")
    print()

    # Greatest common divisor
    print("Greatest common divisor:")
    print(f"gcd(48, 18) -> {gcd(48, 18)}")
    print(f"gcd(84, 36) -> {gcd(84, 36)}")
    print()

    # Least common multiple
    print("Least common multiple:")
    print(f"lcm(12, 18) -> {lcm(12, 18)}")
    print(f"lcm(8, 12) -> {lcm(8, 12)}")


if __name__ == "__main__":
    main()