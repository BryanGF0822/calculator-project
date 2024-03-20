# Advanced Python Calculator

This repository contains an advanced command-line calculator written in Python. It has been updated to perform not only basic arithmetic operations but also more complex mathematical functions. The project is structured to allow for easy maintenance and future improvements.

## Project Structure

The project is organized as follows:
```sh
calculator_project/
│
├── main.py
├── calculator/
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

- Advanced mathematical operations:
  - Power
  - Square root
  - Logarithm
  - Expression evaluation

- Unit tests for the arithmetic operations

## How to Use

To use this calculator, follow these steps:

1. Clone the repository to your local machine or download the source code.
2. Navigate to the project directory in your terminal or command prompt.
3. (Optional) Creates and activates a virtual environment:
  ```sh
   python -m venv venv
   ```
   Activate the virtual environment with the following command:
   ```sh
   .venv\Scripts\activate
   ```
4. Install the dependencies:
  ```sh
   pip install -r requirements.txt
   ```
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
   python3 -m unittest discover tests
  ```
## Future Improvements

- [ ] Implement a graphical user interface (GUI)
- [x] Add support for more complex mathematical operations
- [ ] Improve error handling and input validation
- [ ] Optimize performance and refactor code for better maintainability

## Contributions

Contributions are welcome! If you have suggestions or want to improve the calculator, feel free to fork the repository and submit a pull request with your changes.
