"""
Problem 20: https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(num: int) -> int:
    """Find the factorial of a given number n"""
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def split_and_add(number: int) -> int:
    """Split number digits and add them."""
    sum_of_digits = 0
    while number > 0:
        last_digit = number % 10
        sum_of_digits += last_digit
        number //= 10
    return sum_of_digits


def solution(num: int = 100) -> int:
    """Returns the sum of the digits in the factorial of num
    >>> solution(100)
    648
    >>> solution(50)
    216
    >>> solution(10)
    27
    >>> solution(5)
    3
    >>> solution(3)
    6
    >>> solution(2)
    2
    >>> solution(1)
    1
    """
    nfact = factorial(num)
    return split_and_add(nfact)


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
