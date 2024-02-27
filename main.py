# main.py

from calculator.core import add, subtraction, multiplication, divison

def main():
    while True:
        #print("Operaciones disponibles: summa, resta, multiplicacion, division")
        print("1. Add \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
        operation = input("Seleccione una operacion o salir para finalizar: ").strip().lower()
        if operation == '5':
            break
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        if operation == '1':
            print("Result: ", add(a, b))
        elif operation == '2':
            print("Result: ", subtraction(a, b))
        elif operation == '3':
            print("Result: ", multiplication(a, b))
        elif operation == '4':
            try:
                print("Result: ", divison(a, b))
            except ValueError as e:
                print(e)
        else:
            print("Operacion no valida.")

if __name__ == '__main__':
    main()