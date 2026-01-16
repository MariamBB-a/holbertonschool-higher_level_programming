#!/usr/bin/python3
def pow(a, b):
    """Return a raised to the power b."""
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result
