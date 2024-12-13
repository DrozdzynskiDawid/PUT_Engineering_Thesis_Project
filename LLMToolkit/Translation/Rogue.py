def calculate_rouge(reference, hypothesis):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    print(f"ROUGE-L Score: {scores['rougeL'].fmeasure}")
    return scores['rougeL'].fmeasure