import os


#SAMY'S FUNCTIONS ------------------------------------------------------------------------------------------------------


def error_management(a,b,operator):
    if type(a) not in [int, float, complex] or type(b) not in [int, float,complex]:
        return ("Error: a and b must be numbers")
    elif operator not in ["+", "-", "*", "/","//","%","**"]:
        return ("Error: operator must be '+' or '-' or '*' or '/' or '//' or '%' or '**'")
    elif operator == "/" and b == 0:
        raise ZeroDivisionError
    else:
        pass

def clear_history(history:list):
    history.clear()
    return "History cleared."

def check_int(a):
    float(a)
    if a % 2 == 0:
        int(a)
    if a % 3 == 0:
        int(a)
    if a % 5 == 0:
        int(a)
    if a % 7 == 0:
        int(a)
    else:
        pass
    return a


#CESAR'S FUNCTIONS ------------------------------------------------------------------------------------------------------
def operation_type():
   v= input("operator: ") 
   return v

def check_int(x):    
        if x %2 == 0:
            int(x)
        elif x %3 == 0:
            int(x)
        elif x %5 == 0:
            int(x)
        elif x %7 == 0:
            int(x)
        else:
            float(x)
                



def math_expression(num_a, num_b, v):
    try: 
        os.system('cls' if os.name == 'nt' else 'clear')
        num_a = float(input("\nChoose first number to operate : "))
        v= operation_type()
        num_b = float(input("Choose second number : "))
        print()
        
        if (type(num_a) == float or type(num_a)== int) and (type(num_b) == float or type(num_b)== int): # or use 'isinstance'
            check_int(num_a)
            check_int(num_b) #Don't work (check) 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Asked operation : {num_a} {v} {num_b} \n")
            print("result : \n")
               
            if v == "+":
                print(f"                      {num_a + num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "-":
                print(f"                      {num_a - num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "*":
                print(f"                      {num_a * num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "/":
                print(f"                      {num_a / num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "//":
                print(f"                      {num_a // num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "**":
                cloud = print(f"                      {num_a ** num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif v == "%":
                print(f"                      {num_a % num_b}")
                print()
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            else:
                print("Impossible result, non compliant operator.")
                math_expression()
        else: 
            print("You can only choose des float or integers.")
            math_expression()
    except ValueError:
        print ("Error : Invalid syntax for operation. Retry lad.")
        math_expression()
        
        
math_expression()