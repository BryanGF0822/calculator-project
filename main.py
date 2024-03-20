# main.py

from calculator.core import add, subtraction, multiplication, division, power, square_root, logarithm
from sympy import sympify, SympifyError

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

def main():
    history = []

    while True:
        print("1. Add \n2. Subtraction \n3. Multiplication \n4. Division \n5. Power \n6. Square Root \n7. Logarithm \n8. Evaluate Expression \n9. View History \n10. Exit")
        operation = input("Select an operation or exit to finish: ").strip().lower()

        if operation == '10':
            break

        if operation == '9':
            for record in history:
                print(record)
            continue

        if operation == '8':
            expression = input("Enter the expression: ")
            result = evaluate_expression(expression)
            print("Result: ", result)
            history.append(f"{expression} = {result}")
            continue

        a = get_number("Enter the first number: ")
        
        if operation in ['5', '6', '7']:
            if operation == '5':
                exponent = get_number("Enter the exponent: ")
                result = power(a, exponent)
                print("Result: ", result)
                history.append(f"{a} ^ {exponent} = {result}")
            elif operation == '6':
                result = square_root(a)
                print("Result: ", result)
                history.append(f"sqrt({a}) = {result}")
            elif operation == '7':
                base = get_number("Enter the base (default is e): ")
                result = logarithm(a, base)
                print("Result: ", result)
                history.append(f"log({a}, {base}) = {result}")
        else:
            b = get_number("Enter the second number: ")
            if operation == '1':
                result = add(a, b)
                print("Result: ", result)
                history.append(f"{a} + {b} = {result}")
            elif operation == '2':
                result = subtraction(a, b)
                print("Result: ", result)
                history.append(f"{a} - {b} = {result}")
            elif operation == '3':
                result = multiplication(a, b)
                print("Result: ", result)
                history.append(f"{a} * {b} = {result}")
            elif operation == '4':
                try:
                    result = division(a, b)
                    print("Result: ", result)
                    history.append(f"{a} / {b} = {result}")
                except ValueError as e:
                    print(e)

    # Save history to a file before exiting
    with open('history.txt', 'w') as f:
        for record in history:
            f.write(record + '\n')

if __name__ == '__main__':
    main()