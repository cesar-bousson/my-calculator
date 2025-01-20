import os

#SAMY'S FUNCTIONS --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def error_management(a,b,operator):
    if operator == "/" and b == 0 or a == 0:
        print("!!!!!! Error: division by zero impossible !!!! xO \n\n")
        stop_relaunch()
    elif operator == "%" and b == 0 or a == 0 :
        print("!!!!!!! Error: modulo by zero impossible !!!! xO \n\n")
        stop_relaunch()
        #raise ZeroDivisionError (I know this typeError message but i prefer print so i can relaunch the program)
    elif operator == "//" and b == 0 or a == 0:
        print("!!!!!!! Error: division by zero impossible !!!! xO \n\n")
        stop_relaunch()
    else:
        return
    #or : if operator in ["/", "%", "//"] and b == 0:

def check_int(a):
    # float(a)
    # if a % 2 == 0:
    #     return int(a)
    # if a % 3 == 0:
    #     return int(a)
    # if a % 5 == 0:
    #     return int(a)
    # if a % 7 == 0:
    #     return int(a)
    # else:
    #     pass
    # return a
    return int(a) if a.is_integer() else a

#Balqiss'S FUNCTIONS --------------------------------------------------------------------------------------------------------------------------------------------------------------

def operation_type():
    while True:
        operator= input("Choose operator (+, -, *, /, %, //, **) : ")

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
    
    print ("result: ")    
    return check_int(result)
    # math_expression() cleaned & optimized by this function 


# Cesar's functions: -------------------------------------------------------------------------------------------------------------------------------------------------------- 

#historic
def write_historic(operation_h, result_h, namefile="historic_result.txt"):
    with open(namefile, "a", encoding="utf-8") as file: # "a" add content
        file.write(f"{operation_h} = {result_h} \n")

def read_historic(namefile="historic_result.txt"):
    with open(namefile, "r", encoding="utf-8") as file: # "r" read all
        content = file.read()
    return content if content else " historic empty... "
    
def erase_historic(namefile = "historic_result.txt"):
    with open(namefile, "w") as file: # "w" write by erasing all
        file.write("") 
    
# menu ----------------------------------------------------   
def stop_relaunch():
    while True:
        relaunch = input("     *_*_*_*_*_*_*_*_*_*_*_*_*_   Press [ENTER]: relaunch   |||   Press [Q] + enter: quit   |||   Press [E] + enter: erase historic *_*_*_*_*_*_*_*_*_*_*_*_*_  \n")
        if relaunch == "q" or relaunch =="Q":
            break
        elif relaunch == "e" or relaunch == "E":
            erase_historic()
            print("historic erased")
            pass
        else:
            if relaunch != "":
                print("------>")
            else:
                math_expression()
                
#operation--------------------------------------------------             
def math_expression(): # main loop
    
    try: 
        os.system('cls' if os.name == 'nt' else 'clear')
        
        num_a = float(input("\nChoose first number to operate : "))
        operator = operation_type()
        num_b = float(input("Choose second number : "))
                 
        #verif int or float / no str permitted:       
        # if (type(num_a) == float or type(num_a)== int) and (type(num_b) == float or type(num_b)== int):
            
        os.system('cls' if os.name == 'nt' else 'clear')
            
        operation_h = f"{check_int(num_a)} {operator} {check_int(num_b)}"
        print(f"Asked operation : {operation_h} \n")
            
        result_h = result_expression(num_a, num_b, operator)
        print(f"{result_h}\n")
        # result with 'int' return checking for return an int result if result is not a float.
         # optimized by function ! I saveeed so much liiiiiiines xO
             
        write_historic(operation_h, check_int(result_h))    # Écrit dans l'historique.
        print("historic : \n")
        print(f"{read_historic()} \n ")

        stop_relaunch()                      
        # else: 
        #     print("You can only choose floats or integers.\n")
        #     stop_relaunch()
    except ValueError:
        print ("\n                                                     Error : Invalid syntax for operation. Please Retry.\n")
        stop_relaunch()   
math_expression()

