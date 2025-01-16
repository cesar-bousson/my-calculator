import os

def operation_type():
    while True:
        operator= input("Entrez le type d'opération désiré (+, -, *, /, %, //, **) : ")
        if operator in ["+", "-", "*", "/", "%", "//", "**"]:
            return operator
        else:
            print("Erreur : opération invalide. Veuillez choisir parmi (+, -, *, /, %, //, **).")

# ---------------------------------------------------------------------------------------
def math_expression():
    try: 
        
        os.system('cls' if os.name == 'nt' else 'clear') #refresh terminal
        
        num_a = float(input("\nChoose first number to operate : "))
        operator = operation_type()
        num_b = float(input("Choose second number : "))
        print()
        
        #verif int or float not str
        if (type(num_a) == float or type(num_a)== int) and (type(num_b) == float or type(num_b)== int): # or use 'isinstance'
            
            os.system('cls' if os.name == 'nt' else 'clear')  # refresh terminal
            
            print(f"Asked operation : {num_a} {operator} {num_b} \n")
            
            #---------------------------------------------------------------------
            # result with 'int' return checked
            print("result : \n")
            if operator == "+":
                result = num_a + num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a + num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif operator == "-":
                result = num_a - num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a - num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif operator == "*":
                result = num_a * num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a * num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif operator == "/": # need to fix /0 value impossible
                result = num_a / num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a / num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()            
            elif operator == "//":
                result = num_a // num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a // num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif operator == "**":
                result = num_a ** num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a ** num_b} \n")               
                
                # stop program or reload 
                while True:
                    reload = input("Press enter to reload or press Q to quit:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Incorrect entry. Press Enter to continue or Q to stop.")
                        else:
                            math_expression()
            elif operator == "%": # need to fix 0 value and float value impossible
                result = num_a % num_b               
                if isinstance(num_a, float) and isinstance(num_b, float):
                    print (f"                  {int(result) if result.is_integer else result} \n")                   
                elif isinstance(num_a, int) and isinstance(num_b, int):
                    print(f"                      {num_a % num_b} \n")               
                
                # stop program or reload 
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
# --------------------------------------------------------------------------------------------------

