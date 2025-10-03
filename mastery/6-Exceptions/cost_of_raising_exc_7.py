from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age must be greater than zero.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

print(timeit(code1, number=1000))