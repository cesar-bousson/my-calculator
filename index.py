def operation_type():

    """
    Cette fonction demande à l'opérateur de choisir une fonction valide.
    Retourne l'opération choisi sous forme de chaîne.
    """
    while True:
        operation = input("Entrez le type d'operation souhaitée(+, -, *, /,).")
        if operation in ["+", "-", "*", "/"]:
            return operation 
        else:
            print (" Erreur. Operation invalide. Veuillez choisir parmi (+,-,*,/).")

def resultat_operation (nombre1, nombre2, operation):
    """
    Cette fonction effectue l'opération demandée entres deux nombres
    :param nombre1: Premier nombre
    :param nombre2: Second nombre
    :param operation: Type d'operation ( +, -, *, /)
    :return: Le résultats de l'opération 
    """
    try:
        if operation == "+":
            return nombre1 + nombre2
        elif operation == "-":
            return nombre1 - nombre2
        elif operation == "*":
            return nombre1 * nombre2
        elif operation == "/":
            if nombre2 == 0:
                raise ValueError("Erreur. Division par zéro")
            return nombre1 / nombre2
    except ValueError as e:
        print(e)
        return None

def demander_nombre(message):
    """
    Cette fonction demande a l'utilisateur un nombre valide
    :param message: Message à affciher
    :return: Un nombre (float)
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erreur. Entrez un nombre valide")

def main():
    print("Bienvenue dans la calculatrice.")

    nombre1 = demander_nombre("Entrez le premier nombre.")
    nombre2 = demander_nombre("Entre le deuxième nombre.")

    operation = operation_type()
    
    résultat= resultat_operation ( nombre1, nombre2, operation)
    if résultat is not None:
        print(f"Resultat  : {résultat}")

if __name__== "__main__":
    main()







 