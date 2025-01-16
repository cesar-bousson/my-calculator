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
                

def math_expression(): #commentaire qyui ser a rien
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


# def history():

