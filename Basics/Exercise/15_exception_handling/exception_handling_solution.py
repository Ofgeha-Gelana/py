## Question 1: Using the `finally` Block in Exception Handling
# Write a Python function that reads from a file and handles any potential `FileNotFoundError`. Ensure that the file is always closed, regardless of whether an exception occurs, using the `finally` block.

### Implementation:
# ```python
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')  # Attempt to open the file
        content = file.read()       # Read the content
        print(content)              # Print the content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")  # Handle file not found
    finally:
        if file:
            file.close()           # Ensure the file is closed
            print("File has been closed.")

# Test the function with an existing and a non-existing file
read_file('D:\\input.txt')  # Change to a valid filename to test successful reading



def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))  # Get numerator
        denominator = float(input("Enter the denominator: "))  # Get denominator
        result = numerator / denominator                       # Perform division
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")          # Handle division by zero
    except ValueError:
        print("Error: Please enter valid numeric values!")  # Handle invalid input
    else:
        print(f"The result is: {result}")                   # Print the result if no exception
    finally:
        print("Division operation completed.")               # Final message

# Test the function
divide_numbers()
