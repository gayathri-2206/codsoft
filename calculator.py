def calculate(num1, num2, operator):
  """
  Performs the chosen operation on two numbers.

  Args:
      num1: First number (float).
      num2: Second number (float).
      operator: Chosen operation (+, -, *, /).

  Returns:
      The result of the calculation (float) or None if division by zero occurs.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return None  # Handle division by zero
    else:
      return num1 / num2
  else:
    return None  # Invalid operator

while True:
  try:
    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose operation (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operator)

    if result is None:
      if operator == "/":
        print("Error: Division by zero")
      else:
        print("Invalid operator")
    else:
      print(f"{num1} {operator} {num2} = {result}")

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ").lower()
    if choice != 'y':
      break

  except ValueError:
    print("Invalid input. Please enter numbers only.")

print("Calculator closed.")
