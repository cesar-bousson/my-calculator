import os

def operation_type():
   v= input("operateur: ")
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
                

def math_expression(): #commentaire qui sert à rien
    try: 
        os.system('cls' if os.name == 'nt' else 'clear')
        num_a = float(input("\nChoisissez le premier nombre de votre operation : "))
        v= operation_type()
        num_b = float(input("Choisissez le deuxième nombre de votre operation : "))
        print()
        
        if (type(num_a) == float or type(num_a)== int) and (type(num_b) == float or type(num_b)== int): # or use 'isinstance'
            check_int(num_a)
            check_int(num_b)# marche pas a chequer 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Opération demandée: {num_a} {v} {num_b} \n")
            print("résultat: \n")
               
            if v == "+":
                print(f"                      {num_a + num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "-":
                print(f"                      {num_a - num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "*":
                print(f"                      {num_a * num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "/":
                print(f"                      {num_a / num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "//":
                print(f"                      {num_a // num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "**":
                cloud = print(f"                      {num_a ** num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            elif v == "%":
                print(f"                      {num_a % num_b}")
                print()
                while True:
                    reload = input("Appuyez sur Entrée pour relancer ou tapez Q pour quitter:")
                    if reload == "q" or reload =="Q":
                        break
                    else:
                        if reload != "":
                            print("Saisie incorrecte choisissez Entrée pour continuer ou Q pour arreter.")
                        else:
                            math_expression()
            else:
                print("Résultat impossible, opérateur non conforme.")
                math_expression()
        else: 
            print("Vous pouvez seulement choisir des nombres décimaux ou entiers")
            math_expression()
    except ValueError:
        print ("Erreur: saisie impossible pour opération. Recommencez")
        math_expression()
        
        
math_expression()
#-----------------------------------------------------------------------------------------------------------
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



