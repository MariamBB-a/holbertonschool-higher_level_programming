#!/usr/bin/python3
"""
Module 1-write_file
Contains a function that writes a string to a  file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a file (UTF8) returns the n of characters ."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
