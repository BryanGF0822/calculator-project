# calculator/core.py

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divison(a, b):
    if b == 0:
        raise ValueError("It cannot be divided by zero.")
    return a / b