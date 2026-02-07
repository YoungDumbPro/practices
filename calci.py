# Calculator Application

print("--- Calci by PY ---")

def add( a, b):
   """
    add() takes two inputs, a and b and return their sum.
    
    :param a: first numeric value for addition.
    :param b: second numeric value for addition.
   """
   try:
       return a+b
   except:
       print("Unexpected error happened!")

def subtract(a,b):
    """
    subtract() takes two inputs, a and b and return their difference.
    
    :param a: first numeric value to subtract.
    :param b: second numeric value to subtract.
    """
    return a-b

def multiply(a,b):
    """
    multiply() takes two inputs, a and b and return product.
    
    :param a: first numeric value to multiply.
    :param b: second numeric value to multiply.
    """
    return a*b

def divide(a,b):
    """
    divide() takes two inputs, a and b and return their quotient.
    
    :param a: dividend value.
    :param b: divisor value.
    """
    try:
       return a/b
    except:
       print("Unexpected error happened! Please make sure divisor is not zero.")
       return None
def get_input():
    """
    get_input() prompts the user to enter two numeric values and returns them as floats. 
    It handles invalid input by catching ValueError exceptions and prompting the user to enter numeric values only.
    """
    while True:
        try:
            a = float(input("Enter first numbers: "))
            b = float(input("Enter second numbers: ")) 
            return a, b
        except ValueError:
            print("Please enter numeric values only.")
    

while True:
   operation = input("Select operation: + - * / or type exit to close Calci by Py./ \nEnter operation to perform: ")

   if operation == "+":
      a,b = get_input()
      result = add(a,b)
      print(result)

   elif operation == "-":
      a,b = get_input()
      result = subtract(a,b)
      print(result)
   elif operation == "*":
      a,b = get_input()
      result = multiply(a,b)
      print(result)
   elif operation == "/":
      print("Note: Divisor should not be zero.\n First numbers will be dividend and second numbers will be divisor.")
      a,b = get_input()
      result = divide(a,b)

      if result is not None:
       print(result)

   elif operation.lower() == "exit":
       break
   else:
    print("invalid input, please choose from +, -, * or /.")