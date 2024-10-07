def getDivideByZeroError():
    raise ZeroDivisionError("Error: Division by zero. Length of text mustn't be zero.")


def getTypeError():
    raise ValueError("Error: Type must be text")


def getStatisticError():
    raise Exception(
        "Error: Text fewer than 30 sentences are statistically invalid, because the formula was normed on 30-sentence "
        "samples")
