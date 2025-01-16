def operation_type():
    """
    This function asks the user to choose a valid.
    Returns the selected operation as a string.
    """
    while True:
        operation = input("Enter the desired operation type(+, -, *, /,).")
        if operation in ["+", "-", "*", "/"]:
            return operation 
        else:
            print (" Error: Invalid operation. Please choose from (+,-,*,/).")
def result_operation (nomber1, nomber2, operation):
    """
    This function performs the requested operation between two numbers.
    :param nomber1: First nomber
    :param nomber2: Second nomber
    :param operation: Type of operation ( +, -, *, /)
    :return: The résult of the operation 
    """
    try:
        if operation == "+":
            return nomber1 + nomber2
        elif operation == "-":
            return nomber1 - nomber2
        elif operation == "*":
            return nomber1 * nomber2
        elif operation == "/":
            if nomber2 == 0:
                raise ValueError("Error. Division by zero.")
            return nomber1 / nomber2
    except ValueError as e:
        print(e)
        return None
def ask_nomber(message):
    """
    This function asks the user for a valid number.
    :param message: Message to display
    :return: A nomber (float)
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error. Please enter a valid number")
def main():
    print("Welcome to the Python calculator.")
    nomber1 = ask_nomber("Enter the first nomber.")
    nomber2 = ask_nomber("Enter the second nomber.")
    operation = operation_type()
    
    result= result_operation ( nomber1, nomber2, operation)
    if result is not None:
        print(f"result  : {result}")
if __name__== "__main__":
    main()



