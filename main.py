from expression_converter import expression_converter
from postfix_calculator import calculator

while(True):
    try:
        converted_expression = expression_converter()
        result = calculator(converted_expression)
    except ZeroDivisionError:
        print("We can't divide by zero!")
        continue

    print(f"Converted Expression is : {converted_expression}")
    print(f"Result is : {result}")

