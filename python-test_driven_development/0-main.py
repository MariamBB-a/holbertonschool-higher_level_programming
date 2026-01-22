#!/usr/bin/python3

# Load the 0-add_integer.py code
with open("0-add_integer.py") as f:
    code = f.read()
exec(code)

# Now add_integer is available in this namespace
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))

try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)

try:
    print(add_integer(None))
except Exception as e:
    print(e)

