# Pair : Zulayika Nalukenge & Peter Kakuru

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
