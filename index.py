import os

#SAMY'S FUNCTIONS ------------------------------------------------------------------------------------------------------

def error_management(a,b,operator):
    # if type(a) not in [int, float] or type(b) not in [int, float]:
    #     print("Error: a and b must be numbers")
    #     stop_reload()
    # elif operator not in ["+", "-", "*", "/","//","%","**"]:
    #     print("Error: operator must be '+' or '-' or '*' or '/' or '//' or '%' or '**'")
    
    if operator == "/" and b == 0 or a == 0:
        print("!!!!!! Error: division by zero impossible !!!! xO \n\n")
        stop_reload()
        #raise ZeroDivisionError (I know this typeError message but i prefer print so i can reload the program)
    elif operator == "%" and b == 0 or a == 0 :
        print("!!!!!!! Error: modulo by zero impossible !!!! xO \n\n")
        stop_reload()
        #raise ZeroDivisionError (I know this typeError message but i prefer print so i can reload the program)
    elif operator == "//" and b == 0 or a == 0:
        print("!!!!!!! Error: division by zero impossible !!!! xO \n\n")
        stop_reload()
        #raise ZeroDivisionError (I know this typeError message but i prefer print so i can reload the program)
    else:
        return

def clear_history(history:list):
    history.clear()
    return "History cleared."

def check_int(a):
    float(a)
    if a % 2 == 0:
        return int(a)
    if a % 3 == 0:
        return int(a)
    if a % 5 == 0:
        return int(a)
    if a % 7 == 0:
        return int(a)
    else:
        pass
    return a

#Balqiss'S FUNCTIONS ------------------------------------------------------------------------------------------------------

def operation_type():
    while True:
        operator= input("Choose operator (+, -, *, /, %, //, **) : ")
        #return error_management(1,1,operator)
        if operator in ["+", "-", "*", "/", "%", "//", "**"]:
           return operator
        else:
            print("Error : invalid choice. Please choose between (((  +, -, *, /, %, //, ** ))) only.\n")


def result_expression(num_a,num_b, operator):
    
    error_management(num_a, num_b, operator)
    
    if operator == "+":
        result = num_a + num_b
    elif operator == "-":
        result = num_a - num_b
    elif operator == "*":
        result = num_a * num_b
    elif operator == "**":
        result = num_a ** num_b
    elif operator == "/":
        result = num_a / num_b
    elif operator == "//":
        result = num_a // num_b
    elif operator == "%":
        result = num_a % num_b
    else:      
        return
    
    
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print (f"                                                                  [[[[[  RESULT: {check_int(result)}  ]]]]]")               
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \n\n")
    stop_reload()
    # math_expression() cleaned & optimized by this function 

# Cesar's functions: ---------------------------------------------------------------------------------------  
        
def stop_reload():
    while True:
        reload = input("                              *_*_*_*_*_*_*_*_*_*_*_*_*_   Press [ENTER]: RELOAD / Press [Q]: QUIT   *_*_*_*_*_*_*_*_*_*_*_*_*_  \n")
        if reload == "q" or reload =="Q":
            break
        else:
            if reload != "":
                print("------>")
            else:
                math_expression()
                
                
def math_expression():
    
    try: 
        os.system('cls' if os.name == 'nt' else 'clear') # refresh terminal
        
        num_a = float(input("\nChoose first number to operate : "))
        operator = operation_type()
        num_b = float(input("Choose second number : "))
                 
        #verif int or float no str permitted:       
        if (type(num_a) == float or type(num_a)== int) and (type(num_b) == float or type(num_b)== int):
            
            os.system('cls' if os.name == 'nt' else 'clear')  # refresh terminal
            
            print(f"Asked operation : {check_int(num_a)} {operator} {check_int(num_b)} \n")
            
            print(f" {result_expression(num_a, num_b, operator)}\n")
            # result with 'int' return checking for return an int result if result is not a float.
             # optimized by function ! I saveeed so much liiiiiiines xO
                                  
        else: 
            print("You can only choose floats or integers.\n")
            stop_reload()
    except ValueError:
        print ("\n                                                     Error : Invalid syntax for operation. Please Retry.\n")
        stop_reload()   
math_expression()

