# calculator/core.py
import math
from sympy import sympify, SympifyError
# ===================================================
# ===================================================

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def evaluate_expression(expression):
    try:
        return sympify(expression)
    except SympifyError:
        print("Invalid expression.")

# ===================================================
# ===================================================


def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("It cannot be divided by zero.")
    return a / b

def power(base, exponent):
    return math.pow(base, exponent)

def square_root(number):
    return math.sqrt(number)

def logarithm(number, base=math.e):
    return math.log(number, base)

def add_complex(a, b):
    return complex(a) + complex(b)

# ... (definir el resto de las operaciones para números complejos)