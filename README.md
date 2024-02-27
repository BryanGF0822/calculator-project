# Basic Python Calculator

This repository contains a simple command-line calculator written in Python. It is designed to perform basic arithmetic operations like addition, subtraction, multiplication, and division. The project is structured to allow for easy maintenance and future improvements such as adding a graphical user interface, implementing threading, and more.

## Project Structure

The project is organized as follows:
```sh
calculadora/
│
├── main.py
├── calculadora/
│   ├── __init__.py
│   ├── core.py
│   └── ui.py
└── tests/
    ├── __init__.py
    └── test_core.py
```

## Features

- Basic arithmetic operations:
  - Addition (`sumar`)
  - Subtraction (`restar`)
  - Multiplication (`multiplicar`)
  - Division (`dividir`) with zero-division error handling

- Unit tests for the arithmetic operations

## How to Use

To use this calculator, follow these steps:

1. Clone the repository to your local machine or download the source code.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the `main.py` script using Python. For example:

   ```sh
   python main.py
   ```
   or if you have multiple versions of Python installed:
   ```sh
   python3 main.py
   ```

## How to Run Tests

To ensure the mathematical operations are working correctly, you can run the included unit tests. In the project directory, execute the following command:

  ```sh
   python -m unittest discover tests
  ```
or for specific Python versions:
  ```sh
   python -m unittest discover tests
  ```
## Future Improvements

- [ ] Implement a graphical user interface (GUI)
- [ ] Add support for more complex mathematical operations
- [ ] Improve error handling and input validation
- [ ] Optimize performance and refactor code for better maintainability

## Contributions

Contributions are welcome! If you have suggestions or want to improve the calculator, feel free to fork the repository and submit a pull request with your changes.
