def calculate_bleu(reference, hypothesis, weights=None):

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
