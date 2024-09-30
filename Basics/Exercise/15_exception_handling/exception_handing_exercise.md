## Question 1: Using the `finally` Block in Exception Handling
Write a Python function that reads from a file and handles any potential `FileNotFoundError`. Ensure that the file is always closed, regardless of whether an exception occurs, using the `finally` block.

### Expected Behavior:
1. If the file exists, print its content.
2. If the file doesn't exist, print an appropriate error message.
3. Regardless of success or error, ensure that the file is properly closed.

### Sample Code Structure:
<!-- ```python -->
def read_file(filename):
    # Your code here
    pass

# Test the function with an existing and a non-existing file
read_file('example.txt')



2 Write a Python function that accepts two inputs from the user: a numerator and a denominator. Handle ZeroDivisionError (if the user tries to divide by zero) and ValueError (if the user enters a non-numeric value). Ensure the function handles both cases and provides meaningful feedback to the user.


[Solution](https://github.com/Ofgeha-Gelana/py/blob/main/Basics/Exercise/15_exception_handling/exception_handling_solution.py)

