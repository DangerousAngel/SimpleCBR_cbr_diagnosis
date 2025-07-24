def calculate_similarity(symptoms1, symptoms2):
    """Calculates the similarity between two sets of symptoms."""
    common_symptoms = set(symptoms1).intersection(set(symptoms2))
    total_symptoms = set(symptoms1).union(set(symptoms2))
    if not total_symptoms:
        return 0.0
    return len(common_symptoms) / len(total_symptoms)
