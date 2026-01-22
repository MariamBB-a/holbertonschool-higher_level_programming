#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

    return sum(
        -roman_map[c] if roman_map[c] < roman_map.get(n, 0) else roman_map[c]
        for c, n in zip(roman_string, roman_string[1:] + ' ')
    )
