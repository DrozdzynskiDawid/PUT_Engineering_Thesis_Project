def calculate_meteor(reference, hypothesis):
    score = meteor_score(reference, hypothesis)
    print(f"Meteor Score: {score}")
    return score