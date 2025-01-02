from rouge_score import rouge_scorer

def calculate_rouge(reference, hypothesis):
    if (len(reference) == 0):
        raise ValueError("Reference is empty")
    if (len(hypothesis) == 0):
        raise ValueError("Hypothesis is empty")

    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    print(f"ROUGE-L Score: {scores['rougeL'].fmeasure}")
    return scores['rougeL'].fmeasure