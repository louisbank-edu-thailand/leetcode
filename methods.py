def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

#test change