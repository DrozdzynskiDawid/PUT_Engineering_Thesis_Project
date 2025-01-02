from nltk.translate.bleu_score import sentence_bleu


def calculate_bleu(reference, hypothesis, weights=None):
    if (len(reference) == 0):
        raise ValueError("Reference is empty")

    if (len(hypothesis) == 0):
        raise ValueError("Hypothesis is empty")

    if type(reference) is list:
        reference = [reference]

    if (type(reference) is not list):
        reference = [reference.strip().split()]

    if type(hypothesis) is not list:
        hypothesis = hypothesis.strip().split()

    if weights is None:
        hypothesis_len = len(hypothesis) - 1
        weights = tuple([1. / hypothesis_len for _ in range(hypothesis_len)])
        bleu_score = sentence_bleu(reference, hypothesis,weights=weights)
        print(f"BLEU Score: {bleu_score}")
        return bleu_score

    # Use BLEU-1 (unigrams only)
    bleu_score = sentence_bleu(reference, hypothesis, weights=weights)  # BLEU-1
    print(f"BLEU-1 Score: {bleu_score}")
    return bleu_score
