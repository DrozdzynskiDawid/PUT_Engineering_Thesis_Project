from nltk.translate.meteor_score import meteor_score
import nltk
nltk.download('wordnet')

def calculate_meteor(reference, hypothesis):
    if (len(reference) == 0):
        raise ValueError("Reference is empty")

    if (len(hypothesis) == 0):
        raise ValueError("Hypothesis is empty")

    if type(reference) is list:
        reference = [reference]

    if type(reference) is not list:
        reference = [reference.strip().split()]
        
    score = meteor_score(reference, hypothesis)
    print(f"Meteor Score: {score}")
    return score