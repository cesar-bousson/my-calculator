def operation_type():
    # ask user operator choice and check input as operator
    while True:
        operation = input("Enter the desired operation type(+, -, *, /, %, //, **).")
        if operation in ["+", "-", "*", "/", "%", "//", "**"]:
            return operation 
        else:
            print (" Error: Invalid operation. Please choose from (+,-,*,/).")
            
            
# def result_operation (nomber1, nomber2, operation):
#     # check operator
#     try:
#         if operation == "+":
#             return nomber1 + nomber2
#         elif operation == "-":
#             return nomber1 - nomber2
#         elif operation == "*":
#             return nomber1 * nomber2
#         elif operation == "/":
#             if nomber2 == 0:
#                 raise ValueError("Error. Division by zero.")
#             return nomber1 / nomber2
#     except ValueError as e:
#         print(e)
#         return None
    
    
# def ask_number(message):
#     # """
#     # This function asks the user for a valid number.
#     # :param message: Message to display
#     # :return: A nomber (float)
#     # """
#     while True:
#         try:
#             return float(input(message))
#         except ValueError:
#             print("Error. Please enter a valid number")
            
            
# def main():
#     print("Welcome to the Python calculator.")
#     number1 = ask_number("Enter the first number.")
#     number2 = ask_number("Enter the second number.")
#     operation = operation_type()
    
#     result= result_operation ( number1, number2, operation)
#     if result is not None:
#         print(f"result  : {result}")
# if __name__== "__main__":
    main()



