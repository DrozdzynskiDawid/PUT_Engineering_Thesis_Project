def getDivideByZeroError():
    raise ZeroDivisionError("Error: Division by zero. Length of text mustn't be zero.")


def getTypeError():
    raise ValueError("Error: Type must be text")


def getStatisticError(textError:str):
    raise Exception("Error: Text fewer than "+textError+" are statistically invalid.")
