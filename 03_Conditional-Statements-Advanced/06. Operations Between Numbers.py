first_number = int(input())
second_number = int(input())
operator = input()
operation_type_1 = ["+", "-", "*"]
division_operation = "/"
modular_division_operation = "%"
result = 0
even_odd = ""
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
if operator in operation_type_1:
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
if operator == division_operation and second_number != 0:
    result = first_number / second_number
elif operator == modular_division_operation and second_number != 0:
    result = first_number % second_number
if operator in operation_type_1:
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
elif operator == division_operation:
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        print(f"{first_number} / {second_number} = {result:.2f}")
elif operator == modular_division_operation:
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        print(f"{first_number} % {second_number} = {result}")


